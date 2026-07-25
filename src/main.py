from machine import Pin, I2C
import time

# Configuração de Hardware
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
MPU_ADDR = 0x68

# Botão: 1 = pressionado (porta fechada), 0 = solto (porta aberta)
btn = Pin(4, Pin.IN, Pin.PULL_UP)

# Parâmetros do Sistema
LIMITE_TEMPO_X = 3500        # ms - tempo máximo com a porta aberta
LIMITE_VARIACAO_Y = 3.0      # °C - variação térmica máxima aceitável

# Estado do Sistema
porta_aberta_desde = None
alarme_porta_ativo = False
alarme_termico_ativo = False
temperatura_referencia = None


def mpu_init():
    # Tira o MPU6050 do modo sleep (registrador PWR_MGMT_1 = 0x6B)
    i2c.writeto_mem(MPU_ADDR, 0x6B, b"\x00")


def ler_temperatura():
    # Registrador TEMP_OUT_H/L = 0x41
    dados = i2c.readfrom_mem(MPU_ADDR, 0x41, 2)
    bruto = (dados[0] << 8) | dados[1]
    if bruto > 32767:
        bruto -= 65536
    # Fórmula padrão do MPU6050
    return (bruto / 340.0) + 36.53


def porta_fechada():
    return btn.value() == 0


# Inicialização
mpu_init()
print("Sistema de Monitoramento Inicializado")

# Loop Principal (não bloqueante)
while True:
    agora = time.ticks_ms()
    fechada = porta_fechada()
    temp_atual = ler_temperatura()

    # Captura a referência na primeira vez que a porta estiver fechada, sem bloquear o loop
    if fechada and temperatura_referencia is None:
        temperatura_referencia = temp_atual

    # Enquanto não há referência ainda, considera delta seguro (sem alarme térmico)
    delta_t = (temp_atual - temperatura_referencia) if temperatura_referencia is not None else 0.0

    # Tempo de porta aberta
    if not fechada:
        if porta_aberta_desde is None:
            porta_aberta_desde = agora
        elif (not alarme_porta_ativo and
              time.ticks_diff(agora, porta_aberta_desde) >= LIMITE_TEMPO_X):
            alarme_porta_ativo = True
            print("ALERTA: Porta aberta por muito tempo!")
    else:
        porta_aberta_desde = None

    # Variação térmica
    if temperatura_referencia is not None and delta_t >= LIMITE_VARIACAO_Y and not alarme_termico_ativo:
        alarme_termico_ativo = True
        print("ALERTA: Degradacao termica detectada!")

    # Normalização (as duas condições precisam estar OK ao mesmo tempo)
    if (alarme_porta_ativo or alarme_termico_ativo) and fechada and delta_t < LIMITE_VARIACAO_Y:
        alarme_porta_ativo = False
        alarme_termico_ativo = False
        print("Status: Sistema Normalizado.")

    time.sleep_ms(50)