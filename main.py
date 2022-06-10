from dash import Dash, html, dcc, Input, Output
import plotly.express as px 
import pandas as pd
import dash_bootstrap_components as dbc

# start server
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# read data_frame from xlsx file - Depto Administrativo
df_adm = pd.read_excel('Pesquisa_Kami_Dados_Tratados.xlsx', sheet_name='adm')
fig = px.histogram(df_adm, x='Respostas', color='Setor', barmode='group')



# read data_frame from xlsx file - Depto Operacional
df_op = pd.read_excel('Pesquisa_Kami_Dados_Tratados.xlsx', sheet_name='op')
fig = px.histogram(df_op, x='Respostas', color='Setor', barmode='group')

# read data_frame from xlsx file - Depto Vendas
df_vendas = pd.read_excel('Pesquisa_Kami_Dados_Tratados.xlsx', sheet_name='vendas')
fig = px.histogram(df_vendas, x='Respostas', color='Setor', barmode='group')

# read data_frame from xlsx file - Depto Vendas
df_treina = pd.read_excel('Pesquisa_Kami_Dados_Tratados.xlsx', sheet_name='treinamento')
fig = px.histogram(df_treina, x='Respostas', color='Setor', barmode='group')


app.layout = dbc.Container(html.Div([
    html.H1('KAMI CO.',
            style={'width': '100%', 'margin': '30px',
                 'color': 'red','font-size':'50px',
                'margin-bottom':'10px'
    }),
    
    html.H1('PESQUISA DE CLIMA ORGANIZACIONAL',
            style={'width': '100%', 'margin': '30px'
                , 'font-size':'30px', 'margin-top':'1px', 'margin-bottom':'10px'
    }),

    html.H3('Resultados separados por Departamentos',
    style={'width': '100%', 'margin': '30px', 'margin-top': '30px'
    }),      
    
    html.H3("ADMINISTRATIVO", 
    style={'width': '100%', 'margin': '30px'
    }),   
    
    html.H5("Selecione uma pergunta:", 
    style={'width': '100%', 'margin': '30px'
    }),   

       
    html.Div([
    dcc.Dropdown(df_adm['Perguntas'], 
                value='Perguntas', id='coluna-perguntas-adm', clearable=False,
                style={'width': '80%', 'margin-left': '15px  '}),
            ]),

    dcc.Graph(id='pesquisa-graph-adm',
              style={'border': '0px solid black', 
                    }),     
      
    ##########################GRÁFICO OPERACIONAL##############################
    
    html.Br(),
    html.Br(),
    html.Div([   
        html.H3("OPERACIONAL", 
        style={'width': '100%', 'margin': '30px'}),   

        html.H5("Selecione uma pergunta:", 
        style={'width': '100%', 'margin': '30px'}),   
        
        html.Div([
        dcc.Dropdown(df_op['Perguntas'], 
                    value='Perguntas', id='coluna-perguntas-op', clearable=False,
                    style={'width': '80%', 'margin-left': '15px  '}),
                ]),

        dcc.Graph(id='pesquisa-graph-op',
                style={'border': '0px solid black', 
                        "background-color": "#242424"}),          


    #######################GRÁFICO DE VENDAS###############################
    
    html.Br(),
    html.Br(),
    html.Div([   
        html.H3("VENDAS", 
        style={'width': '100%', 'margin': '30px'}),   

        html.H5("Selecione uma pergunta:", 
        style={'width': '100%', 'margin': '30px'}),   
        
        html.Div([
        dcc.Dropdown(df_vendas['Perguntas'], 
                    value='Perguntas', id='coluna-perguntas-vendas', clearable=False,
                    style={'width': '80%', 'margin-left': '15px  '}),
                ]),

        dcc.Graph(id='pesquisa-graph-vendas',
                style={'border': '0px solid black', 
                        "background-color": "#242424"}), 

    #######################GRÁFICO DE TREINAMENTO###############################
    
    html.Br(),
    html.Br(),
    html.Div([   
        html.H3("VENDAS", 
        style={'width': '100%', 'margin': '30px'}),   

        html.H5("Selecione uma pergunta:", 
        style={'width': '100%', 'margin': '30px'}),   
        
        html.Div([
        dcc.Dropdown(df_vendas['Perguntas'], 
                    value='Perguntas', id='coluna-perguntas-treina', clearable=False,
                    style={'width': '80%', 'margin-left': '15px  '}),
                ]),

        dcc.Graph(id='pesquisa-graph-treina',
                style={'border': '0px solid black', 
                        "background-color": "#242424"}),

                    ])
                ])
            ])
    ])
)

#######################CALLBACK ADMINISTRATIVO#####################
@app.callback(
    Output("pesquisa-graph-adm", "figure"), 
    Input("coluna-perguntas-adm", "value"), 
    
)
def uptdate_graph(coluna_perguntas_adm):
    if coluna_perguntas_adm == 'Perguntas':
        #fig = px.bar(df, x='Respostas', color='Setor', barmode='group')
        fig = px.histogram(x=df_adm[df_adm['Respostas'] == coluna_perguntas_adm]['Respostas'],
        hover_name=df_adm[df_adm['Perguntas'] == coluna_perguntas_adm]['Respostas'])
        
    else:
        filter = df_adm.loc[df_adm['Perguntas'] == coluna_perguntas_adm, :]
        fig = px.histogram(filter, x='Respostas', color='Setor', barmode='group')
        fig.update_layout(
        paper_bgcolor='#FFFFFF',
        )

    return fig


############################CALLBACK OPERACIONAL##############################

@app.callback(
    Output("pesquisa-graph-op", "figure"), 
    Input("coluna-perguntas-op", "value"), 
    
)
def uptdate_graph(coluna_perguntas_nome):
    if coluna_perguntas_nome == 'Perguntas':
        #fig = px.bar(df, x='Respostas', color='Setor', barmode='group')
        fig = px.histogram(x=df_op[df_op['Respostas'] == coluna_perguntas_nome]['Respostas'],
        hover_name=df_op[df_op['Perguntas'] == coluna_perguntas_nome]['Respostas'])
    else:
        filter = df_op.loc[df_op['Perguntas'] == coluna_perguntas_nome, :]
        fig = px.histogram(filter, x='Respostas', color='Setor', barmode='group')

    return fig


############################CALLBACK VENDAS##############################
@app.callback(
    Output("pesquisa-graph-vendas", "figure"), 
    Input("coluna-perguntas-vendas", "value"), 
    
)
def uptdate_graph(coluna_perguntas_vendas):
    if coluna_perguntas_vendas == 'Perguntas':
        #fig = px.bar(df, x='Respostas', color='Setor', barmode='group')
        fig = px.histogram(x=df_vendas[df_vendas['Respostas'] == coluna_perguntas_vendas]['Respostas'],
        hover_name=df_vendas[df_vendas['Perguntas'] == coluna_perguntas_vendas]['Respostas'])
    else:
        filter = df_vendas.loc[df_vendas['Perguntas'] == coluna_perguntas_vendas, :]
        fig = px.histogram(filter, x='Respostas', color='Setor', barmode='group')

    return fig


############################CALLBACK TREINAMENTOS##############################
@app.callback(
    Output("pesquisa-graph-treina", "figure"), 
    Input("coluna-perguntas-treina", "value"), 
    
)
def uptdate_graph(coluna_perguntas_treina):
    if coluna_perguntas_treina == 'Perguntas':
        #fig = px.bar(df, x='Respostas', color='Setor', barmode='group')
        fig = px.histogram(x=df_treina[df_treina['Respostas'] == coluna_perguntas_treina]['Respostas'],
        hover_name=df_treina[df_treina['Perguntas'] == coluna_perguntas_treina]['Respostas'])
    else:
        filter = df_vendas.loc[df_vendas['Perguntas'] == coluna_perguntas_treina, :]
        fig = px.histogram(filter, x='Respostas', color='Setor', barmode='group')

    return fig



if __name__ == '__main__':
    app.run_server(debug=True)

