# 🐍 PyCalc — Calculadora Simples em Python & Projeto GitHub

> Uma calculadora modular, robusta e elegante desenvolvida em Python com foco em boas práticas de engenharia de software, separação estrita de responsabilidades, suíte avançada de porcentagem com visualização de dados (*Donut Chart* e *Barra 100%*), testes unitários automatizados e interfaces gráfica (Tkinter) e de terminal (CLI).

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Tests](https://img.shields.io/badge/tests-16%2F16%20passing-brightgreen.svg?logo=pytest&logoColor=white)](#-testes-unitários)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)](#-como-executar)

---

## 📋 Sumário

- [Visão Geral](#-visão-geral)
- [Arquitetura & Decisões de Design](#-arquitetura--decisões-de-design)
- [Funcionalidades](#-funcionalidades)
- [Visualização de Dados (Porcentagens & Proporções)](#-visualização-de-dados-porcentagens--proporções)
- [Estrutura do Repositório](#-estrutura-do-repositório)
- [Pré-requisitos](#-pré-requisitos)
- [Como Executar](#-como-executar)
  - [1. No Windows (2 Cliques Rápidos)](#1-no-windows-execução-em-2-cliques-sem-terminal)
  - [2. Pelo Terminal (Python Direto)](#2-pelo-terminal)
- [Utilizando como Módulo Python](#-utilizando-como-módulo-python)
- [Testes Unitários](#-testes-unitários)
- [Publicação no GitHub (Passo a Passo)](#-publicação-no-github-passo-a-passo)
- [Contribuindo](#-contribuindo)
- [Licença](#-licença)

---

## 💡 Visão Geral

O **PyCalc** é um projeto construído para demonstrar padrões profissionais de desenvolvimento em Python, fugindo do modelo de script único e implementando uma **arquitetura em camadas desacoplada**:

* **Zero dependências externas obrigatórias:** O projeto roda nativamente utilizando apenas a biblioteca padrão do Python (`math`, `tkinter`, `unittest`, `argparse`).
* **Tratamento defensivo de exceções:** Operações matematicamente inválidas (divisão por zero ou raiz quadrada de número negativo nos reais) disparam exceções tipadas tratadas amigavelmente sem derrubar a aplicação.
* **Múltiplas formas de interação:** Suporte a interface gráfica de desktop (GUI), linha de comando interativa (CLI), flags diretas de terminal e importação programática como biblioteca.

---

## 🏗️ Arquitetura & Decisões de Design

O projeto aplica o **Princípio da Responsabilidade Única (SRP)**:

```
[ Usuário ]
    │
    ▼
┌─────────────────────────┐       ┌──────────────────────────┐
│  Camada de Apresentação │       │    Camada de Domínio     │
│                         │       │                          │
│  • gui.py (Tkinter)     │ ────> │  calculator.py           │ <──── test_calculator.py
│  • cli.py (Terminal)    │       │  (Classe Calculator)     │       (16 Testes Unitários)
│  • executar.py (Menu)   │       │                          │
└─────────────────────────┘       └──────────────────────────┘
```

1. **Lógica de Negócio Pura (`calculator.py`):** Não contém comandos de `print()`, `input()` ou widgets visuais. Apenas recebe valores, processa cálculos matemáticos, registra histórico e retorna resultados ou lança exceções.
2. **Interfaces Desacopladas (`gui.py` e `cli.py`):** Consomem a classe `Calculator`. Se a interface visual for trocada por um bot do Telegram ou uma página web, a lógica matemática permanece intacta.
3. **Qualidade Contínua (`test_calculator.py` e GitHub Actions):** Cada alteração de código é testada automaticamente em múltiplos ambientes Python (3.8 a 3.13).

---

## ✨ Funcionalidades

### 1. Quatro Operações Básicas
- ➕ **Adição** (`calc.add(a, b)`)
- ➖ **Subtração** (`calc.subtract(a, b)`)
- ✖️ **Multiplicação** (`calc.multiply(a, b)`)
- ➗ **Divisão Segura** (`calc.divide(a, b)`) com proteção contra `ZeroDivisionError`

### 2. Suíte Avançada de Porcentagem & Proporção
- **Valor Percentual:** Calcula $P\%$ de um total ($Total \times \frac{P}{100}$). Ex: $15\%$ de $200 = 30.0$.
- **Proporção Relativa:** Descobre quantos por cento uma parte representa de um total ($\frac{Parte}{Total} \times 100$). Ex: $50$ em $200 = 25.0\%$.
- **Acréscimo Percentual:** Aplica aumentos percentuais (ex: $R\$\;100 + 15\% = R\$\;115.0$).
- **Desconto Percentual:** Aplica descontos percentuais (ex: $R\$\;200 - 20\% = R\$\;160.0$).
- **Gráfico de Barra ASCII:** Gera uma barra horizontal de progresso em texto puro para visualização no terminal.

### 3. Operações Complementares & Memória
- ⚡ **Potência** (`calc.power(base, expoente)`)
- 📐 **Raiz Quadrada** (`calc.square_root(valor)`) com validação no domínio real
- 🔢 **Módulo / Resto de Divisão** (`calc.modulo(a, b)`)
- 🧠 **Memória de Cálculo:** Funções `memory_store()`, `memory_add()`, `memory_subtract()` e `memory_clear()`
- 📜 **Histórico de Execução:** Gravação e recuperação cronológica de cálculos realizados em tempo de execução

---

## 📊 Visualização de Dados (Porcentagens & Proporções)

Segundo especialistas renomados em visualização de dados — como **Cole Nussbaumer Knaflic** (*Storytelling with Data*) e **Stephen Few** (*Show Me the Numbers*) —, a mente humana apresenta dificuldade para discernir diferenças em ângulos e áreas curvas (como fatias de gráficos de pizza tradicionais).

Para representar com exatidão relações de **Parte vs. Todo (porcentagens)**, a literatura recomenda:

1. **Barra 100% Empilhada Horizontal (100% Horizontal Stacked Bar / Progress Bar):**
   - É o gráfico mais intuitivo para o cérebro humano, pois compara comprimentos lineares ao longo de um eixo comum.
   - Implementado no terminal via método `render_ascii_bar()`:
     ```text
     [███████████░░░░░░░░░░░░░░░░░░░] 35.0%
     Legenda: [█ = Parte Calculada (70.0) | ░ = Restante (130.0)]
     ```
2. **Gráfico de Rosca com Big Number Central (Donut Chart com KPI):**
   - Elimina a distorção central da pizza e aproveita o miolo vazado para estampar o número em destaque (*Big Ass Number*).
   - Segue o princípio *"Highlight the Hero"*: cor chamativa apenas na fatia calculada e cinza neutro para o restante.
   - Implementado nativamente no desktop via **Tkinter Canvas**.

---

## 📁 Estrutura do Repositório

```text
PyCalc/
├── .github/
│   └── workflows/
│       └── tests.yml          # Automação CI no GitHub Actions (testa Python 3.8 a 3.13)
├── Abrir_Calculadora.bat      # Atalho executável de 2 cliques para abrir a calculadora visual
├── Testar_Resultados.bat      # Atalho executável de 2 cliques para rodar a bateria de testes
├── Publicar_no_GitHub.bat     # Assistente interativo para envio do repositório ao GitHub
├── calculator.py              # Módulo principal com a classe Calculator e regras matemáticas
├── gui.py                     # Interface gráfica desktop nativa em Tkinter com gráficos
├── cli.py                     # Interface de terminal interativa (menu numérico e flags)
├── executar.py                # Script inicializador unificado (GUI, CLI e testes)
├── test_calculator.py         # 16 testes unitários automatizados com unittest
├── requirements.txt           # Dependências opcionais de desenvolvimento (pytest, black, flake8)
├── .gitignore                 # Arquivos e diretórios ignorados pelo Git
├── LICENSE                    # Licença MIT de código aberto
└── README.md                  # Documentação técnica oficial do repositório
```

---

## 🚀 Pré-requisitos

- **Python 3.8** ou superior instalado em sua máquina.
  - Para verificar se o Python está instalado, abra o terminal e digite:
    ```bash
    python --version
    ```
- **Git** instalado (necessário para clonar e publicar no GitHub).

---

## 💻 Como Executar

### 1. No Windows (Execução em 2 Cliques, sem terminal)
Se você utiliza Windows, não precisa abrir telas pretas:
- **Abrir a Calculadora Visual:** Dê 2 cliques no arquivo **`Abrir_Calculadora.bat`**.
- **Rodar os Testes:** Dê 2 cliques no arquivo **`Testar_Resultados.bat`**.
- **Publicar no GitHub:** Dê 2 cliques no arquivo **`Publicar_no_GitHub.bat`**.

---

### 2. Pelo Terminal

#### A. Abrir a Calculadora com Janela Visual (Desktop)
```bash
python gui.py
```
> Clique no botão **`% Gráfico`** para abrir o visualizador com Donut Chart e Barra 100%.

#### B. Abrir o Modo de Terminal Interativo (CLI)
```bash
python cli.py
```

#### C. Executar Cálculos Diretos via Linha de Comando (Flags)
```bash
# Somar 15 + 35
python cli.py --add 15 35

# Multiplicar 8 * 7
python cli.py --mul 8 7

# Calcular 35% de 200 com gráfico de barra ASCII
python cli.py --pct 200 35

# Extrair raiz quadrada de 144
python cli.py --sqrt 144
```

---

## 🐍 Utilizando como Módulo Python

Você pode importar a classe `Calculator` em qualquer outro script do seu projeto:

```python
from calculator import Calculator

calc = Calculator()

# Operações básicas
soma = calc.add(125, 75)              # 200
divisao = calc.divide(100, 4)         # 25.0

# Suíte de porcentagens
valor_pct = calc.percentage(200, 15)  # 30.0
proporcao = calc.percentage_ratio(50, 200) # 25.0 (%)
desconto = calc.percentage_discount(200, 20) # 160.0

# Gráfico em texto para relatórios ou logs
barra = calc.render_ascii_bar(35.0)
print(barra)  # [███████████░░░░░░░░░░░░░░░░░░░] 35.0%

# Histórico
for item in calc.get_history():
    print(f"{item['operation']} = {item['result']}")
```

---

## 🧪 Testes Unitários

O projeto conta com **16 testes unitários** automatizados desenvolvidos com o módulo `unittest` padrão do Python, cobrindo cenários normais e limites de falha:

```bash
python -m unittest test_calculator.py -v
```

Saída esperada:
```text
test_addition (test_calculator.TestCalculator) ... ok
test_division (test_calculator.TestCalculator) ... ok
test_division_by_zero (test_calculator.TestCalculator) ... ok
test_history (test_calculator.TestCalculator) ... ok
test_memory_functions (test_calculator.TestCalculator) ... ok
test_modulo (test_calculator.TestCalculator) ... ok
test_multiplication (test_calculator.TestCalculator) ... ok
test_percentage (test_calculator.TestCalculator) ... ok
test_percentage_discount (test_calculator.TestCalculator) ... ok
test_percentage_increase (test_calculator.TestCalculator) ... ok
test_percentage_ratio (test_calculator.TestCalculator) ... ok
test_power (test_calculator.TestCalculator) ... ok
test_render_ascii_bar (test_calculator.TestCalculator) ... ok
test_square_root (test_calculator.TestCalculator) ... ok
test_square_root_negative (test_calculator.TestCalculator) ... ok
test_subtraction (test_calculator.TestCalculator) ... ok

----------------------------------------------------------------------
Ran 16 tests in 0.001s

OK
```

---

## 📤 Publicação no GitHub (Passo a Passo)

### Método 1: Automático (2 Cliques no Windows)
1. Crie um novo repositório vazio em [github.com/new](https://github.com/new).
2. Copie a URL do repositório (ex: `https://github.com/seu-usuario/calculadora-python.git`).
3. Dê dois cliques em **`Publicar_no_GitHub.bat`**, cole a URL e dê Enter!

---

### Método 2: Pelo Terminal (Git Passo a Passo)

Abra o terminal dentro da pasta do projeto e execute os comandos:

```bash
# 1. Inicializar o repositório Git local
git init

# 2. Adicionar todos os arquivos
git add .

# 3. Criar o primeiro commit
git commit -m "feat: Calculadora simples em Python com 4 operacoes, porcentagem, graficos e testes"

# 4. Definir a branch principal como 'main'
git branch -M main

# 5. Conectar ao seu repositório remoto no GitHub (substitua com a sua URL)
git remote add origin https://github.com/SEU_USUARIO/calculadora-python.git

# 6. Enviar para o GitHub
git push -u origin main
```

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Siga as diretrizes:

1. Faça um Fork do projeto.
2. Crie uma Branch para sua feature (`git checkout -b feature/NovaFuncionalidade`).
3. Faça commit das mudanças (`git commit -m 'feat: Adiciona calculo de media ponderada'`).
4. Envie para o branch (`git push origin feature/NovaFuncionalidade`).
5. Abra um **Pull Request**.

---

## 📄 Licença

Este projeto está sob a licença **MIT**. Consulte o arquivo [`LICENSE`](LICENSE) para mais detalhes.

---

⭐ Se este projeto te ajudou a aprender Python ou compor seu portfólio, considere deixar uma estrela no repositório!
