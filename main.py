from dash import Dash, html, dcc, Input, Output
import plotly.express as px 
import pandas as pd

# start server
app = Dash(__name__)
# read data_frame from xlsx file
df = pd.read_excel('Pesquisa_Kami_Dados_Tratados.xlsx')

#fig = px.bar(df, x='Respostas', color='Setor', barmode='group')

app.layout = html.Div([
    html.H1('PESQUISA DE CLIMA ORGANIZACIONAL'),
    html.H2('Gráficos separados por departamentos'),      
    
       
    html.P("Selecione uma pergunta:"),    
    html.Div([
    dcc.Dropdown(df['Perguntas'], 
                value='Perguntas', id='coluna-perguntas', clearable=False,
                style={'width': '80%'}),
            ]),

    dcc.Graph(id='pesquisa-graph',
              style={'border': '0px solid black'}),   
   
])

# Callback para o gráfico
@app.callback(
    Output("pesquisa-graph", "figure"), 
    Input("coluna-perguntas", "value"), 
    
)
def uptdate_setor(coluna_perguntas_nome):
    if coluna_perguntas_nome == 'Perguntas':
        #fig = px.bar(df, x='Respostas', color='Setor', barmode='group')
        fig = px.bar(x=df[df['Respostas'] == coluna_perguntas_nome]['Respostas'],
        hover_name=df[df['Perguntas'] == coluna_perguntas_nome]['Respostas'])
    else:
        filter = df.loc[df['Perguntas'] == coluna_perguntas_nome, :]
        fig = px.bar(filter, x='Respostas', color='Setor', barmode='group')

    return fig

""" @app.callback(
    Output("pesquisa-graph", "figure"), 
    Input("perguntas-setor", "value"), 
    
)
def uptdate_perguntas(coluna_perguntas_nome):
    if coluna_perguntas_nome == 'Perguntas':
        #fig = px.bar(df, x='Respostas', color='Setor', barmode='group')
        fig = px.bar(x=df[df['Respostas'] == coluna_perguntas_nome]['Respostas'],
        hover_name=df[df['Setor'] == coluna_perguntas_nome]['Respostas'])
    else:
        filter = df.loc[df['Setor'] == coluna_perguntas_nome, :]
        fig = px.bar(filter, x='Respostas', color='Setor', barmode='group')

    return fig
 """

if __name__ == '__main__':
    app.run_server(debug=True)

