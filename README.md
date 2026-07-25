# Processo Seletivo – Intensivo Maker | IoT

## Etapa Prática – Sistemas Embarcados

Bem-vindo(a) à **etapa prática do processo seletivo para o Intensivo Maker | IoT**.

Esta atividade tem como objetivo avaliar suas competências em **Sistemas Embarcados**, com foco em **organização de projeto, lógica de firmware e simulação de hardware**, a partir da aplicação prática dos conhecimentos adquiridos nos cursos EAD da etapa anterior.

> **Objetivo principal**  
> Avaliar sua capacidade de **planejar, estruturar e desenvolver** uma solução funcional de sistemas embarcados, seguindo boas práticas de engenharia.

---

## Antes de Tudo

Se você **nunca utilizou Git ou GitHub**, não se preocupe.  
Siga atentamente os passos abaixo.

---

### 1 - Criação de Conta no GitHub

1. Acesse: <https://github.com>
2. Clique em **Sign up**
3. Crie sua conta gratuita seguindo as instruções da plataforma

> O GitHub será utilizado para:
>
> - Envio do seu projeto
> - Versionamento do código
> - Correção e validação automática via GitHub Actions

---

### 2 - Instalação do Git

O **Git** é a ferramenta responsável pelo controle de versões do seu código.

### Windows

Baixe e instale o **Git Bash**:  
<https://git-scm.com/downloads>

### Linux / macOS

Verifique se o Git já está instalado:

```bash
git --version
```

> Caso não esteja, instale pelo gerenciador de pacotes do seu sistema.

## Preparando o Ambiente

Para desenvolver o desafio, você deverá criar uma cópia deste repositório no seu GitHub.

### 1 - Fork do Repositório

No canto superior direito desta página, clique em Fork

<img width="219" height="45" alt="image" src="https://github.com/user-attachments/assets/5d629626-513a-445c-ba0f-e5bb3e225187" />

Uma cópia do repositório será criada no seu perfil do GitHub

> O Fork permite que você trabalhe de forma independente, sem alterar o repositório original do processo seletivo.

### 2 - Clone do Repositório

No repositório do seu Fork, clique em **<> Code**

<img width="149" height="52" alt="image" src="https://github.com/user-attachments/assets/abbd331b-a005-4633-89c6-afd16acbe828" />

Copie a URL e execute no terminal:

```bash
git clone https://github.com/SEU_USUARIO/nome-do-repositorio.git
cd nome-do-repositorio
```

> O comando git clone cria uma cópia local do repositório para desenvolvimento.

### 3 - Preparação do Ambiente de Execução

Você pode executar o projeto de duas formas. Escolha apenas uma.

#### Opção A – Ambiente Python Local

**Requisitos:**

- Python 3.10 ou 3.11
- pip

**Instale as dependências:**

```bash
pip install -r requirements.txt
```

#### Opção B – Dev Container (Recomendado)

Este repositório inclui um Dev Container, garantindo um ambiente padronizado.

**Requisitos:**

- VS Code
- Docker instalado
- Extensão Dev Containers

**Passos:**

1. Abra o repositório no VS Code
2. Clique em “Reopen in Container”
3. Aguarde a criação automática do ambiente

> Todas as dependências serão instaladas automaticamente.

## Criando sua API Key do Wokwi

A simulação do projeto será executada automaticamente via GitHub Actions, utilizando o Wokwi CLI.

Para isso, você precisa gerar uma API Key.

1. Acesse: <https://wokwi.com/dashboard/ci>
2. Faça login (Google ou GitHub)
3. Clique em Generate API Token
4. Copie a chave gerada (exemplo: wokwi-xxxxxxxx)

> Importante

- Nunca faça commit dessa chave
- Ela deve ser armazenada apenas como secret no GitHub

## Configurando a API Key no GitHub (Secrets)

**No repositório do seu Fork:**

1. Vá em Settings
2. Acesse Secrets and variables → Actions
3. Clique em New repository secret
4. Nome: WOKWI_CLI_TOKEN
5. Valor: sua chave gerada
6. Salve

> As GitHub Actions do template já estão preparadas para usar essa variável automaticamente.

## Desafio Técnico

Você deverá desenvolver um projeto de sistemas embarcados simulados, utilizando Python e Wokwi.

### Estrutura mínima esperada

```text
/project
 ├── src/
 │   └── main.py        # Código principal do projeto
 ├── wokwi.toml         # Configuração da simulação
 ├── diagram.json       # Circuito no Wokwi
 └── README.md          # Explicação do seu projeto
```

> Você pode expandir essa estrutura se desejar, desde que mantenha os arquivos essenciais.

### Escolha do cenário

No diretório "scenarios" existem arquivos .md e pastas referentes a diferentes desafios. Selecione apenas um deles e mantenha apenas a pasta e .md referente ao desafio a ser desenvolvido, deletando os demais. Isso fará com o que o fluxo de testes automáticos selecione o fluxo de acordo com o desafio escolhido.

### Como Desenvolver seu Projeto

O desenvolvimento acontece principalmente nos arquivos abaixo:

#### src/main.py

- Código Python executado na simulação
- Implementa a lógica do sistema embarcado
- Exemplos: controle de LEDs, leitura de sensores, estados, temporizações, etc.

#### diagram.json

- Define o hardware virtual do projeto
- Componentes como:
  - LEDs
  - Botões
  - Sensores
  - Placa microcontroladora

#### wokwi.toml

- Configura a simulação:
  - Tipo de placa
  - Framework
  - Dependências adicionais
 
#### Rodando localmente

Para executar o seu projeto locamente, é necesário preparar a imagem docker local, e após isso
utiliza-la para gerar o arquivo que conterá o seu código para o projeto, para isso, execute os 
seguintes códigos:

1. Prepara a imagem docker (Necessário rodar apenas 1 vez)

```bash
docker build -t esp32-builder -f Dockerfile .
```

2. Prepara o arquivo de memória fs.bin (Necessário a cada iteração)

```bash
docker run --rm -v "$(pwd)/src:/mnt/src" -v "$(pwd):/mnt/out" esp32-builder bash -c "mkdir -p /tmp/fs && cp -r /mnt/src/* /tmp/fs/ && /mklittlefs/mklittlefs -c /tmp/fs -b 4096 -p 256 -s 0x200000 /mnt/out/fs.bin"
```

#### Commit e Push

Após suas alterações:

```bash
git add .
git commit -m "Descrição clara do que foi feito"
git push
```

### Execução Automática (GitHub Actions)

A cada push, o GitHub Actions irá automaticamente:

- Executar o pipeline de build
- Rodar a simulação via Wokwi CLI
- Validar que o projeto executa sem erros

### Caso algo falhe

- Vá até a aba Actions
- Analise os logs da execução
- Corrija e envie novamente

## Critérios de Avaliação

Esta etapa será avaliada considerando:

- Funcionamento correto da simulação
- Código organizado e legível
- Estrutura de arquivos correta
- Uso adequado do Wokwi
- Commits claros e bem descritos
- Projeto executando sem falhas nas Actions

---

## Submissão Final

Após concluir o desenvolvimento:

1. Verifique se o projeto **executa sem erros** nas GitHub Actions
2. Confirme que todos os arquivos obrigatórios estão presentes
3. Copie o link do **seu repositório no GitHub**

Envie o link conforme as orientações do processo seletivo na plataforma do **PNAAT**.

---

## Relatório do Candidato

O arquivo **`README.md` do seu repositório** deve ser utilizado como o  
**relatório final do desafio técnico**.

Preencha todas as seções abaixo de forma **clara, objetiva e técnica**.

> **Dica importante**  
> Não é necessário um relatório extenso.  
> O principal critério é demonstrar **clareza nas decisões técnicas**, organização e entendimento do sistema embarcado desenvolvido.
> Não mantenha os demais conteúdos escritos nesse arquivo README, aqui devem ser concentradas apenas informações referentes ao projeto desenvolvido.

---

### Identificação do Candidato

- **Nome completo:** João Pedro de Oliveira Dias
- **GitHub:** https://github.com/ojoaopedrodias

---

## Visão Geral da Solução

Este projeto implementa um Sistema de Monitoramento de Temperatura e Abertura de Porta, voltado para controle de qualidade e auditoria em ambientes refrigerados, estufas ou painéis elétricos.
O sistema monitora, em paralelo e de forma não bloqueante, duas condições de risco:

**Tempo de exposição**: quanto tempo a porta/tampa permanece aberta.

**Degradação térmica**: variações abruptas de temperatura em relação a uma referência estável, coletada com a porta fechada.

Quando qualquer uma das duas condições ultrapassa o limite parametrizado, o sistema emite um alerta específico via Serial. O sistema só retorna ao estado normal quando ambas as condições voltam a ficar dentro do esperado, de forma estável, ao mesmo tempo.
A interação do usuário (ou do simulador, no caso dos testes automatizados) acontece por meio de dois componentes: um botão que simula o estado da porta e um sensor de temperatura (MPU6050), ambos lidos continuamente pelo firmware.

---

## Arquitetura do Sistema Embarcado

O firmware (src/main.py) roda em MicroPython sobre um ESP32, seguindo uma arquitetura de loop principal único, não bloqueante, sem uso de sleep() prolongado nem funções bloqueantes que pudessem quebrar a sincronia com o simulador.

**Fluxo principal**

Inicialização

  └─ Configura I2C e tira o MPU6050 do modo sleep
  
  └─ Imprime "Sistema de Monitoramento Inicializado"
  
Loop principal (a cada ~50ms):

  ├─ Lê o estado do botão (porta aberta/fechada)

  ├─ Lê a temperatura atual via I2C
  
  ├─ Captura a temperatura de referência na primeira vez que a porta
  
  │   estiver fechada (sem bloquear o loop, mesmo que a porta comece aberta)
  
  ├─ Calcula o delta de temperatura (atual - referência)
  
  ├─ Verifica tempo de porta aberta → dispara alerta se ultrapassar o limite X
  
  ├─ Verifica variação térmica → dispara alerta se ultrapassar o limite Y
  
  └─ Verifica normalização → exige que ambas as condições estejam OK de
      forma ESTÁVEL por um pequeno intervalo (debounce) antes de declarar
      o sistema normalizado

**Estados e variáveis de controle**

**porta_aberta_desde**: marca temporal de quando a porta começou a ficar aberta (usada para o timeout).

**alarme_porta_ativo / alarme_termico_ativo**: flags que indicam se cada tipo de alarme está ativo.

**temperatura_referencia**: capturada dinamicamente na primeira vez que a porta fecha — não é fixa em tempo de compilação, o que permite que o sistema funcione mesmo que a porta comece aberta.

**normalizando_desde**: marca temporal usada no debounce da normalização (ver "Decisões Técnicas Relevantes").

---

## Componentes Utilizados na Simulação

Definidos no diagram.json:

| Componente |	ID |	Função |
|:---------- |:--:| ------:|
| ESP32 DevKit C v4 |	esp |	Microcontrolador principal |
| MPU6050 (IMU) |	imu1 |	Sensor de temperatura, lido via I2C (registrador de temperatura do chip) |
| Botão (fim de curso) |	btn1 |	Simula o estado da porta — pressionado = fechada, solto = aberta |
| Serial Monitor |	— |	Saída de logs, alertas e telemetria |

Fiação: MPU6050 conectado via I2C (SCL→GPIO22, SDA→GPIO21, VCC→3V3, GND→GND); botão conectado a GPIO4 com pull-up interno, outra perna ao GND.

---

## Decisões Técnicas Relevantes

Foram realizadas melhorias no sistema para corrigir falhas de funcionamento e aumentar sua confiabilidade. A captura da temperatura de referência passou a ocorrer de forma não bloqueante dentro do loop principal, evitando deadlocks quando a porta inicia aberta. A lógica de detecção da porta foi ajustada para a polaridade correta do botão configurado com PULL_UP. Também foi implementado um mecanismo de debounce na normalização, exigindo que as condições seguras permaneçam estáveis por um curto período antes de confirmar o estado, prevenindo oscilações e condições de corrida nos testes. Por fim, a leitura da temperatura do MPU6050 passou a ser feita diretamente pelo registrador TEMP_OUT (0x41) via I2C, eliminando a dependência de bibliotecas externas no MicroPython.

---

## Resultados Obtidos

Os três cenários de teste automatizados (Wokwi CI) executam com sucesso:

**Alarme por Porta Aberta**: o sistema inicializa corretamente e emite o alerta de porta aberta após o tempo limite configurado.

**Alarme por Elevação Térmica**: o sistema detecta corretamente o gradiente de temperatura acima do limite de tolerância e emite o alerta térmico.

**Retorno ao Estado Normal**: após os alarmes serem disparados, o sistema reconhece corretamente quando ambas as condições voltam ao normal e emite a mensagem de normalização.

Todas as mensagens Seriais batem exatamente com o especificado, e o firmware não utiliza nenhuma função bloqueante no loop principal.

---

## Comentários Adicionais (Opcional)

Durante o desenvolvimento, o maior desafio não foi a lógica em si, mas sim o processo de debugging de infraestrutura.
Identificar por que o firmware não inicializava corretamente.
Corrigir a fiação incorreta no diagram.json (nomes de pino), corrigir a polaridade do botão, e por fim identificar uma condição de corrida sutil entre o firmware e o harness de testes automatizados do Wokwi CI, que exigiu a introdução de um debounce na lógica de normalização.
Com mais tempo, uma melhoria possível seria expor os parâmetros LIMITE_TEMPO_X e LIMITE_VARIACAO_Y como valores configuráveis externamente.
Principal aprendizado: em sistemas embarcados simulados com testes automatizados, nem toda falha é um bug de lógica, parte considerável do trabalho foi entender o comportamento real da ferramenta de simulação e teste (Wokwi CI) para alinhar o timing do firmware com as expectativas do harness de validação.

---

> Este relatório faz parte da avaliação técnica.  
> Clareza, objetividade e organização são tão importantes quanto o funcionamento do código.

---

## Especificação dos Testes Automatizados (Wokwi CI)

Para que o projeto seja validado com sucesso na esteira de integração contínua (CI), o firmware escrito em MicroPython deve interagir corretamente com as leituras dos sensores descritos em cada cenário e enviar as mensagens de status exatas.

### Requisitos Críticos de Implementação

1. **Casamento Exato de Strings:** O Wokwi CI faz uma verificação estrita caractere por caractere. Se houver divergência em maiúsculas/minúsculas, acentuação ou falta de pontuação, o teste irá falhar.
2. **Arquitetura Não-Bloqueante:** Evite o uso de funções bloqueantes. Elas podem fazer com que o firmware perca a janela de tempo em que o simulador altera o peso, quebrando a sincronia do teste automatizado.

---

## Suporte

Em caso de dúvidas:

- Consulte o material dos cursos EAD
- Leia atentamente este README
- Analise os logs das GitHub Actions
- Utilize os canais oficiais para contato com os instrutores
