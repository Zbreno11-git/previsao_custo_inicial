import streamlit as st 
import pandas as pd 
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt, seaborn as sns

path = '/Users/luanabreno/Downloads/download/3.Franquia/'

df = pd.read_csv(path + 'slr12.csv', sep=';')

st.set_page_config(page_title='Previsão Franquia', layout='wide')

st.markdown(
    "<h1 style='font-size: 50px; white-space: nowrap;'>Previsão Inicial de Custo para Franquia</h1>", unsafe_allow_html=True)

X = df[['FrqAnual']]
y = df['CusInic'] 

model = LinearRegression().fit(X, y)

col1, col2 = st.columns(2)

with col1:
    st.subheader('Dados')
    st.table(df.head(11))

with col2:
    st.subheader('Gráfico de Dispersão')
    fig, ax = plt.subplots()
    ax.scatter(X, y, color='b')
    ax.plot(X, model.predict(X), color='r')
    st.pyplot(fig)

st.header('Valor Anual da Franquia: ')
novo_valor = st.number_input('Insira novo valor', 
                    min_value=1.0, max_value=99999.0,
                    value=1500.0, step=0.01)
processar = st.button('Processar')

if processar:
    novo_valor_df = pd.DataFrame([[novo_valor]], columns=['FrqAnual'])
    prev = model.predict(novo_valor_df)
    st.header(f'Previsão de Custo Inicial: R${prev[0]:.2f}')
