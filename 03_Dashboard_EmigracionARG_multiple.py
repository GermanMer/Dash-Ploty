# Importar las bibliotecas
import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Crear una aplicación Dash
app = dash.Dash(__name__)

# Cargar los datos de emigración desde el archivo CSV
df = pd.read_csv(r'D:\Germán\Desktop\Python Files\migration.csv')
df = df.dropna(axis=0)
df['Value'] = df['Value'].astype(int)

# Filtrar y procesar los datos para cada uno de los 3 países
arg_esp = df[(df['Country of birth/nationality'] == 'Argentina') & (df['Country'] == 'Spain')]
arg_esp = arg_esp.groupby('Year')['Value'].sum().reset_index()

arg_ita = df[(df['Country of birth/nationality'] == 'Argentina') & (df['Country'] == 'Italy')]
arg_ita = arg_ita.groupby('Year')['Value'].sum().reset_index()

arg_usa = df[(df['Country of birth/nationality'] == 'Argentina') & (df['Country'] == 'United States')]
arg_usa = arg_usa.groupby('Year')['Value'].sum().reset_index()

# Combinar los datos de los tres destinos en un solo DataFrame
combined_data = pd.concat([arg_esp, arg_ita, arg_usa], keys=['España', 'Italia', 'Estados Unidos'])

# Obtener la lista de años únicos desde los datos de emigración
available_years = combined_data['Year'].unique()

# Diseñar el diseño del dashboard
app.layout = html.Div([
    html.H1("Emigración de Argentina a España, Italia y Estados Unidos"),
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
    filtered_migration = combined_data[combined_data['Year'] == selected_year]

    # Crear un gráfico de barras basado en los datos filtrados
    fig = px.bar(filtered_migration, x=filtered_migration.index.get_level_values(0), y='Value',
                 color=filtered_migration.index.get_level_values(0),  # Utiliza 'level_0' como la columna de color
                 title=f'Emigración de Argentina en el año {selected_year}',
                 labels={'x': 'Destino', 'Value': 'Cantidad de Emigrantes'})

    return fig

print('Abre un navegador web para acceder al dashboard en http://localhost:8050')
# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)

#Ejecutar el script:
#Ejecuta el script de Python y abre un navegador web para acceder al dashboard en http://localhost:8050.
