# Previsão Inicial de Custo para Franquia

Aplicação desenvolvida em **Python** utilizando **Streamlit** e **Scikit-Learn** para realizar a previsão do **Custo Inicial de uma Franquia** com base no **Valor Anual da Franquia**, por meio de um modelo de **Regressão Linear Simples**.

## Objetivo

O projeto tem como objetivo demonstrar a aplicação de técnicas de Machine Learning para estimar o custo inicial de uma franquia a partir do valor anual da franquia informado pelo usuário.

## Funcionalidades

- Leitura dos dados a partir de um arquivo CSV.
- Exibição dos dados utilizados no treinamento.
- Treinamento de um modelo de Regressão Linear Simples.
- Visualização dos dados em gráfico de dispersão.
- Exibição da reta de regressão ajustada.
- Entrada de novos valores para previsão.
- Estimativa automática do custo inicial da franquia.

## Tecnologias Utilizadas

- Python 3
- Streamlit
- Pandas
- Scikit-Learn
- Matplotlib
- Seaborn

## Estrutura do Projeto

```text
.
├── app.py
├── slr12.csv
└── README.md
```

## Base de Dados

O arquivo `slr12.csv` deve conter as seguintes colunas:

| Coluna | Descrição |
|---------|-------------|
| FrqAnual | Valor anual da franquia |
| CusInic | Custo inicial da franquia |

Exemplo:

```csv
FrqAnual;CusInic
1000;25000
1500;32000
2000;41000
2500;50000
```

## Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/previsao-franquia.git
cd previsao-franquia
```

### 2. Crie um ambiente virtual (opcional)

```bash
python -m venv venv
```

### 3. Ative o ambiente virtual

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install streamlit pandas scikit-learn matplotlib seaborn
```

Ou utilizando um arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Execução

Para iniciar a aplicação, execute:

```bash
streamlit run app.py
```

Após a execução, o Streamlit abrirá automaticamente uma página no navegador.

## Como Utilizar

1. Execute a aplicação.
2. Visualize os dados carregados da base.
3. Analise o gráfico de dispersão e a linha de regressão.
4. Informe um novo valor para a franquia anual.
5. Clique em **Processar**.
6. Consulte a previsão do custo inicial gerada pelo modelo.

## Modelo de Machine Learning

O projeto utiliza o algoritmo de **Regressão Linear Simples** da biblioteca Scikit-Learn.

## Interface da Aplicação

A aplicação apresenta:

- Tabela com os dados da base.
- Gráfico de dispersão dos dados.
- Linha de regressão ajustada pelo modelo.
- Campo para inserção de novos valores.
- Resultado da previsão em tempo real.

