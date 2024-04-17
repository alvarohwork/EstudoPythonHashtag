from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
#import dash_auth

#usuarios = {
#    "Alvaro": '123456',
#    "Bernardo": "89012"
#}

app = Dash(__name__)
#auth = dash_auth.BasicAuth(app, usuarios)

df = pd.read_excel("Vendas.xlsx")

lista_marcas = list(df["Marca"].unique())
lista_marcas.append("Todas")

lista_paises = list(df["País"].unique())
lista_paises.append("Todos")

# plotly
#fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
#fig2 = px.scatter(df, x="Quantidade", y="Valor Final", color="Produto", size="Valor Unitário", size_max=60)

app.layout = html.Div(children=[
    html.H1(children='My First Dashboard'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    html.H1(children="Vendas de Produto por loja", id='subtitulo'),
    
    dcc.RadioItems(lista_marcas, value="Todas", id='selecao_marcas', inline=True, style={"color": "#00FF00"}),
    html.Div(children=[
            dcc.Dropdown(lista_paises, value="Todos", id='selecao_pais'),
    ], style={"width": "50%", "margin": "auto"}),
    

    dcc.Graph(id='vendas_por_loja'),
    dcc.Graph(id='distribuicao_vendas'),


], style={"text-align": "center", "color": "#FF0000"})

# callbacks -> dar funcionalidade para dashboard (conecta botões com os gráficos)
@app.callback(
    Output('selecao_pais', 'options'),
    Input('selecao_marcas', 'value'),
)
def opcoes_pais(marca):
    # criar uma lógica que diga qual a lista de paises que ele vai pegar
    if marca == "Todas":
        nova_lista_paises = list(df["País"].unique())
        nova_lista_paises.append("Todos")
    else:
        df_filtrada = df.loc[df['Marca']==marca, :]
        nova_lista_paises = list(df_filtrada["País"].unique())
        nova_lista_paises.append("Todos")
    return nova_lista_paises

@app.callback(
        Output('subtitulo', 'children'), # objeto que eu quero modificar
        Output('vendas_por_loja', 'figure'), 
        Output('distribuicao_vendas', 'figure'), 
        Input('selecao_marcas', 'value'), # de onde vem as informações - Entrada
        Input('selecao_pais', 'value'),
)
def selecionar_marca(marca, pais):
    if marca == "Todas" and pais == 'Todos':
        texto = 'Venda de cada Produto por Loja'
        fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
        fig2 = px.scatter(df, x="Quantidade", y="Valor Final", color="Produto", size="Valor Unitário", size_max=60)
    else:
        #definindo os filtros
        df_filtrada = df
        if marca != "Todas":
            df_filtrada = df_filtrada.loc[df_filtrada["Marca"] == marca, :]
        if pais != 'Todos':
            df_filtrada = df_filtrada.loc[df_filtrada["País"] == pais, :]

        texto = f'Vendas de cada Produto por Loja da Marca {marca} e do País {pais}'
        fig = px.bar(df_filtrada, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
        fig2 = px.scatter(df_filtrada, x="Quantidade", y="Valor Final", color="Produto", size="Valor Unitário", size_max=60)
    return texto, fig, fig2   

if __name__ == '__main__':
    app.run_server(debug=True)
