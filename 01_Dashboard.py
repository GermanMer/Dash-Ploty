# Importar las bibliotecas
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

# Crear una aplicación Dash
app = dash.Dash(__name__)

# Diseñar el diseño del dashboard
# Definir el diseño del dashboard utilizando componentes HTML y gráficos de Plotly
app.layout = html.Div([
    html.H1("Dashboard Interactivo con Plotly y Dash"),
    dcc.Dropdown(  # Agregar un componente Dropdown
        id='dropdown',  # Asignar un ID
        options=[
            {'label': 'Opción 1', 'value': 'opcion1'},
            {'label': 'Opción 2', 'value': 'opcion2'},
        ],
        value='opcion1'  # Valor predeterminado
    ),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3, 4, 5], 'y': [6, 7, 2, 4, 8], 'type': 'bar', 'name': 'Grupo A'},
                {'x': [1, 2, 3, 4, 5], 'y': [8, 4, 7, 1, 6], 'type': 'bar', 'name': 'Grupo B'},
            ],
            'layout': {
                'title': 'Gráfico de Barras'
            }
        }
    )
])

# Definir callbacks
# Los callbacks permiten que los elementos del dashboard reaccionen a eventos.
@app.callback(
    Output('example-graph', 'figure'),
    Input('dropdown', 'value')  # Utilizar el ID del Dropdown como entrada
)
def update_graph(selected_value):
    # Aquí debes definir la lógica para actualizar el gráfico en función de 'selected_value'.
    # Este es un marcador de posición, reemplázalo con la lógica adecuada.
    if selected_value == 'opcion1':
        updated_figure = {
            'data': [{'x': [1, 2, 3], 'y': [4, 5, 6], 'type': 'bar', 'name': 'Opción 1'}],
            'layout': {'title': 'Gráfico para Opción 1'}
        }
    else:
        updated_figure = {
            'data': [{'x': [1, 2, 3], 'y': [6, 5, 4], 'type': 'bar', 'name': 'Opción 2'}],
            'layout': {'title': 'Gráfico para Opción 2'}
        }

    return updated_figure

print('Abre un navegador web para acceder al dashboard en http://localhost:8050')
# Ejecutar la aplicación (ejecuta la aplicación Dash en el servidor local)
if __name__ == '__main__':
    app.run_server(debug=True)

#Ejecutar el script:
#Ejecuta el script de Python y abre un navegador web para acceder al dashboard en http://localhost:8050.
