import pandas as pd
import streamlit as st
import os
import plotly.express as px
import plotly.graph_objects as go

### Importando dataframes

# Diretório onde os arquivos CSV estão localizados
diretorio = "Dataframes"

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
	page_title='Trabalho Final - Introdução a Python',  # String or None. Strings get appended with "• Streamlit".
	page_icon=None,  # String, anything supported by st.image, or None.
)

demonstrativo = "demostrativo_acidentes_riosp.xlsx"
d_acidentes = pd.read_excel(demonstrativo)

def main():

    st.title('Trabalho Final\n')
    st.write('Nesse projeto vamos analisar um banco de dados que envolve os acidentes na Rodovia Rio-São Paulo (BR-116). No projeto, \
                foi realizado uma análise da base de dados sobre os acidentes nas rodovias concedidas são \
                transmitidos pelas concessionárias e salvos na rede da Superintendência, sob organização\
                da Agência Nacional de Transportes Terrestres.')
    st.write('A seguinte imagem mostra um mapa destacando a rodovia RioSP:')
    # Exibir a imagem na página
    st.image("https://www.ccrriosp.com.br/resources/files/maps/mapa-CCR-RioSP.png", use_column_width=True)
main()


######### Gráfico 1

fig1 = px.bar(df_6_1, x='Tipo_de_acidente', y='Quantidade_Mortos', title = 'Gráfico de Barras - Acidentes e Mortos')
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
def plot_gravidade(dataframe, tipo_gravidade):
    
    fig = px.line(dataframe[tipo_gravidade], x = meses.values(), y=['QuantidadeAcidentes', 'QuantidadePessoasEnvolvidas'],
                                 title = f'Gráfico - {tipo_gravidade}', )
    return fig

#Criando Select Box
tipo_gravidade = list(df_7_1['Gravidade'].unique())
categoria_grafico = st.sidebar.selectbox('Para o Gráfico de Distribuição de gravidade, seleciona a gravidade desejada:', options = df_7_1['Gravidade'].unique())

# Dividir o DataFrame com base na coluna "Gravidade"
dataframes_gravidade = {}
for gravidade in df_7_1['Gravidade'].unique():
    dataframes_gravidade[gravidade] = df_7_1[df_7_1['Gravidade'] == gravidade].copy()

#Printando Gráfico
figura = plot_gravidade(dataframes_gravidade, categoria_grafico)
st.plotly_chart(figura)


## Boston Housing


path = "BostonData.xlsx"
data = pd.read_excel(path)  # Importar o dataframe a partir do arquivo CSV
print(data)


# Explicação dos Dados

def main_2():

    st.title('Boston Dataset\n')
    st.write('Este conjunto de dados contém informações coletadas pelo Serviço de Censo dos Estados Unidos \
                sobre habitação na área de Boston, Massachusetts. Ele foi obtido do arquivo StatLib \
                (http://lib.stat.cmu.edu/datasets/boston) e tem sido amplamente utilizado na literatura como \
                referência para algoritmos. No entanto, essas comparações foram feitas principalmente fora \
                do Delve e, portanto, são um tanto suspeitas. O conjunto de dados é pequeno, contendo \
                apenas 506 casos.')
    # Exibir a imagem na página
    st.image("https://miro.medium.com/v2/resize:fit:1000/1*FHQOSHMMT07CbXpklk1Ehw.jpeg", use_column_width=True)
main_2()

data_dict = {
    'CRIM': 'per capita crime rate by town',
    'ZN': 'proportion of residential land zoned for lots over 25,000 sq.ft.',
    'INDUS': 'proportion of non-retail business acres per town',
    'CHAS': 'Charles River dummy variable (1 if tract bounds river; 0 otherwise)',
    'NOX': 'nitric oxides concentration (parts per 10 million)',
    'RM': 'average number of rooms per dwelling',
    'AGE': 'proportion of owner-occupied units built prior to 1940',
    'DIS': 'weighted distances to five Boston employment centres',
    'RAD': 'index of accessibility to radial highways',
    'TAX': 'full-value property-tax rate per $10,000',
    'PTRATIO': 'pupil-teacher ratio by town',
    'B': '1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town',
    'LSTAT': 'percentage of lower status of the population',
    'MEDV': 'Median value of owner-occupied homes in $1000\'s'
}



######### Gráfico 1

st.subheader('Distribuição de Dados')

names = (list(data.keys()))
tabs = st.tabs(names)
counter = 0

for name_col in names:
    with tabs[counter]:
        fig = px.box(data_frame=data, y = name_col)
        st.plotly_chart(fig)
    counter = counter + 1

######### Gráfico 2

st.subheader('Distribuição de Preços')


# Plotar histograma com cor vermelha e transparência
fig = px.histogram(data_frame = data, y = 'medv', color_discrete_sequence = ['rgba(255, 0, 0, 0.5)'])
fig.update_layout(
    yaxis_title = "Preço mediano das residências (US$ 1000)",
    xaxis = dict(tickangle=90)
)

# Ajustar transparência do histograma
for trace in fig.data:
    if isinstance(trace, go.Bar):
        trace.marker.opacity = 0.5

# Plotar boxplot
boxplot = px.box(data_frame=data, y='medv')

# Adicionar o boxplot ao gráfico de histograma
fig.add_traces(boxplot.data)

# Exibir o gráfico completo
st.plotly_chart(fig)

st.write('Após uma análise inicial dos dados de MEDV \
        (Valor mediano (preço), em US$ 1000, das residências\
        ocupadas pelo proprietário) foi possível obter algumas \
        inferências iniciais. Por exemplo, a média de valor global \
        da base de dados é de 22.53, conforme indicado pelo sumário. \
        Contudo, esse indicador não explicita totalmente a base de\
        dados proposta, já que há uma dispersão de dados relevante nos\
        valores, o que pode ser percebido pela distância do valor do 3º \
        quartil (25.0) para o valor máximo (50.0), dessa forma é possível\
        afirmar que há, na distribuição, uma cauda grossa para a direita \
        (valores superiores à média global).')


###### Grafico 3

st.subheader('Matriz de Correlação')

df = pd.DataFrame(data)

# Calcular a matriz de correlação
correlation_matrix = df.corr()

# Criar o corrplot usando plotly
fig = px.imshow(correlation_matrix, color_continuous_scale='RdBu')

# Configurar o layout do gráfico
fig.update_layout(
    title='Matriz de Correlação',
    xaxis=dict(tickangle=-45),
    yaxis=dict(tickangle=0),
)

# Exibir o gráfico no Streamlit
st.plotly_chart(fig)
# Exibir o texto ao lado do gráfico
st.write("Fica evidente que há uma forte correlação positiva \
                de MEDV com rm (nº quartos) e uma forte correlação negativa \
                com lstat (% populacao baixa renda). Ambas as variáveis também\
                possuem correlação negativa relevante entre si, o que faz \
                sentido, pois em localidades em que a porcentagem de \
                população de baixa renda é menor, tendem a existir moradias mais\
                simples, o que acarreta em um nº de quartos menor e, em conjunto,\
                um valor também inferior, quando comparado à média.")
