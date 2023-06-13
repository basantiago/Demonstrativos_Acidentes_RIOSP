import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import sqlite3
import io
import os
import plotly.express as px
import plotly.graph_objects as go

### Importando dataframes

# Diretório onde os arquivos CSV estão localizados
diretorio = "C://Users//barba//OneDrive//Dataframes"

# Dicionário para armazenar os dataframes
dataframes = {}

# Listar os arquivos CSV no diretório
arquivos_csv = [arquivo for arquivo in os.listdir(diretorio) if arquivo.endswith(".csv")]

# Importar os dataframes
for arquivo in arquivos_csv:
    nome_dataframe = arquivo.split(".")[0]  # Obter o nome do dataframe
    caminho_arquivo = os.path.join(diretorio, arquivo)  # Obter o caminho completo do arquivo
    df = pd.read_csv(caminho_arquivo)  # Importar o dataframe a partir do arquivo CSV
    dataframes[nome_dataframe] = df  # Armazenar o dataframe no dicionário

# Criar variáveis específicas para cada dataframe
df_1_1 = dataframes.get("df_1_1")
df_2_1 = dataframes.get("df_2_1")
df_3_1 = dataframes.get("df_3_1")
df_4_1 = dataframes.get("df_4_1")
df_5_1 = dataframes.get("df_5_1")
df_6_1 = dataframes.get("df_6_1")
df_7_1 = dataframes.get("df_7_1")
df_8_1 = dataframes.get("df_8_1")
df_9_1 = dataframes.get("df_9_1")
df_10_1 = dataframes.get("df_10_1")


### Streamlit

st.set_page_config(
	layout="wide",  # Can be "centered" or "wide". In the future also "dashboard", etc.
	initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
	page_title='TP2 - IBD',  # String or None. Strings get appended with "• Streamlit".
	page_icon=None,  # String, anything supported by st.image, or None.
)

d_acidentes = pd.read_excel(r'C:\Users\barba\OneDrive\demostrativo_acidentes_riosp.xlsx')

def main():

    st.title('IBD TP2\n')
    st.write('Nesse projeto vamos analisar o banco de dados do TP2. No projeto, \
                foi realizado uma análise da base de dados sobre os acidentes nas rodovias concedidas são \
                transmitidos pelas concessionárias e salvos na rede da Superintendência, sob organização\
                da Agência Nacional de Transportes Terrestres.')
    st.write('A seguinte imagem mostra um mapa destacando a rodovia RioSP:')
    # Exibir a imagem na página
    st.image("https://www.ccrriosp.com.br/resources/files/maps/mapa-CCR-RioSP.png", use_column_width=True)
main()


######### Gráfico 1

fig1 = px.bar(df_6_1, x='Tipo_de_acidente', y='Quantidade_Mortos', title='Gráfico de Barras - Acidentes e Mortos')
st.subheader('\n\nRetornar o tipo de acidente e a quantidade de mortos correspondente a cada tipo')
# Exibir gráfico no Streamlit
st.plotly_chart(fig1)


######### Gráfico 2 e 3

df_sp = df_3_1[df_3_1['Trecho'] == 'BR-116/SP']
df_rj = df_3_1[df_3_1['Trecho'] == 'BR-116/RJ']

st.subheader('Distribuição de Acidentes por km - Trechos SP e RJ')

# Plotar o primeiro gráfico - Trecho BR-116/SP
fig_sp = go.Figure(data=go.Scatter(x=df_sp['km'], y=df_sp['Total_Acidentes'], mode='markers', name='BR-116/SP'))
fig_sp.update_layout(title='Distribuição de Acidentes por km - BR-116/SP', xaxis_title='km', yaxis_title='Total de Acidentes')
# Criar o segundo gráfico - Trecho BR-116/RJ
fig_rj = go.Figure(data=go.Scatter(x=df_rj['km'], y=df_rj['Total_Acidentes'], mode='markers', name='BR-116/RJ'))
fig_rj.update_layout(title='Distribuição de Acidentes por km - BR-116/RJ', xaxis_title='km', yaxis_title='Total de Acidentes')

# Exibir os gráficos no Streamlit
st.plotly_chart(fig_sp)
st.plotly_chart(fig_rj)


######### Gráfico 4

st.subheader('Distribuição de gravidade e quantidade de acidentes por mês')

meses = {
    1: 'Janeiro',
    2: 'Fevereiro',
    3: 'Março',
    4: 'Abril',
    5: 'Maio',
    6: 'Junho',
    7: 'Julho',
    8: 'Agosto',
    9: 'Setembro',
    10: 'Outubro',
    11: 'Novembro',
    12: 'Dezembro'
}

# Filtrar os dados para cada valor de 'Gravidade' e criar os gráficos
df_gravemente_feridos = df_7_1[df_7_1['Gravidade'] == 'gravemente_feridos']
df_mortos = df_7_1[df_7_1['Gravidade'] == 'mortos']
df_ilesos = df_7_1[df_7_1['Gravidade'] == 'ilesos']

df_gravemente_feridos['Mes'] = df_gravemente_feridos['Mes'].map(meses)
df_mortos['Mes'] = df_mortos['Mes'].map(meses)
df_ilesos['Mes'] = df_ilesos['Mes'].map(meses)

fig_gravemente_feridos = px.line(df_gravemente_feridos, x='Mes', y=['QuantidadeAcidentes', 'QuantidadePessoasEnvolvidas'],
                                 title='Gráfico - Gravemente Feridos')
fig_mortos = px.line(df_mortos, x='Mes', y=['QuantidadeAcidentes', 'QuantidadePessoasEnvolvidas'], title='Gráfico - Mortos')
fig_ilesos = px.line(df_ilesos, x='Mes', y=['QuantidadeAcidentes', 'QuantidadePessoasEnvolvidas'], title='Gráfico - Ilesos')

st.plotly_chart(fig_gravemente_feridos)
st.plotly_chart(fig_mortos)
st.plotly_chart(fig_ilesos)