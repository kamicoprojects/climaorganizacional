from dash import Dash, html, dcc, Input, Output
import plotly.express as px 
import pandas as pd


df = pd.read_excel('Pesquisa_Kami_Dados_Tratados.xlsx')
app = Dash(__name__)

fig = px.bar(df, x='Respostas', color='Setor', barmode='group')

app.layout = html.Div(children=[
    html.H1('PESQUISA DE CLIMA ORGANIZACIONAL'),
    html.H2('Gráficos separados por departamentos'),      
    
    html.P("Selecione um Departamento:"),    
    dcc.Dropdown(df['Setor'].unique(), 
                value='Todos Departamentos', id='setor-values', clearable=False ),
    
    html.P("Selecione uma Pergunta:"),
    dcc.Dropdown(df['Perguntas'].unique(), 
                value='Todas perguntas',
                id='perguntas-values', clearable=False ),   
    

    dcc.Graph(id='pesquisa-graph', figure=fig),   
   
])

# Callback para o gráfico
@app.callback(
    Output("pesquisa-graph", "figure"), 
    Input("setor-values", "value"), 
    
    )

def generate_chart(value):
    if value == 'Todos Departamentos':
        fig = px.bar(df, x='Respostas', color='Setor', barmode='group')
    else:
        filter = df.loc[df['Setor'] == value, :]
        fig = px.bar(filter, x='Respostas', color='Setor', barmode='group')
        
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)

