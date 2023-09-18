# Importar las bibliotecas
import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Crear una aplicación Dash
app = dash.Dash(__name__)

# Cargar los datos de emigración desde el archivo CSV
df = pd.read_csv(r'D:\Germán\Desktop\Python Files\migration.csv')

# Filtrar y procesar los datos para Argentina a España
argentina_spain = df[(df['Country of birth/nationality'] == 'Argentina') & (df['Country'] == 'Spain')]
argentina_spain = argentina_spain.groupby('Year')['Value'].sum().reset_index()

# Obtener la lista de años únicos desde los datos de emigración
available_years = argentina_spain['Year'].unique()

# Diseñar el diseño del dashboard
app.layout = html.Div([
    html.H1("Emigración de Argentina a España"),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': str(year), 'value': year} for year in available_years],
        value=available_years[0]  # Valor predeterminado (primer año en la lista)
    ),
    dcc.Graph(
        id='example-graph'
    )
])

# Definir callbacks
@app.callback(
    Output('example-graph', 'figure'),
    Input('dropdown', 'value')  # Utilizar el ID del Dropdown como entrada
)
def update_graph(selected_year):
    # Filtrar los datos de emigración para el año seleccionado
    filtered_migration = argentina_spain[argentina_spain['Year'] == selected_year]

    # Crear un gráfico de barras basado en los datos filtrados
    fig = px.bar(filtered_migration, x='Year', y='Value', title=f'Emigración de Argentina a España en el año {selected_year}')

    return fig

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)

#Ejecutar el script:
#Ejecuta el script de Python y abre un navegador web para acceder al dashboard en http://localhost:8050.
