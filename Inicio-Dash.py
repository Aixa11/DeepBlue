import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

# Configuración de la aplicación Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout de la landing page
app.layout = html.Div(
    style={
        'display': 'flex',
        'height': '100vh',
        'backgroundColor': '#FFFFFF',
        'fontFamily': 'Arial, sans-serif',
        'overflow': 'hidden',
    },
    children=[
        # Sección de la imagen de fondo a la izquierda
        html.Div(
            style={
                'width': '50%',
                'backgroundImage': 'url("https://via.placeholder.com/500x800")',  # Reemplaza con tu URL o archivo local
                'backgroundSize': 'cover',
                'backgroundPosition': 'center',
            }
        ),
        # Sección derecha con título, subtítulo y botón
        html.Div(
            style={
                'width': '50%',
                'display': 'flex',
                'flexDirection': 'column',
                'justifyContent': 'center',
                'alignItems': 'center',
                'padding': '0 50px',
                'textAlign': 'center',
            },
            children=[
                html.H1(
                    "Deep Blue",
                    style={
                        'fontSize': '60px',
                        'fontWeight': 'bold',
                        'marginBottom': '20px',
                    }
                ),
                html.P(
                    "Explora las regiones protegidas y los efectos del cambio climático en el planeta. Descubre información detallada y visualizaciones dinámicas.",
                    style={'fontSize': '18px', 'color': '#555'},
                ),
                dbc.Button(
                    "Descubrir más",
                    id='discover-btn',
                    color='primary',
                    style={'marginTop': '40px', 'padding': '15px 30px', 'fontSize': '18px'},
                ),
            ]
        ),
    ]
)

# Callback para redirigir al hacer clic en el botón
@app.callback(
    dash.Output('url', 'href'),
    [dash.Input('discover-btn', 'n_clicks')],
    prevent_initial_call=True
)
def redirect_to_dashboard(n_clicks):
    # Redirige al script principal de la plataforma
    return "./dashboard"  # Cambia a la URL correcta de tu aplicación principal

# Ejecuta la aplicación
if __name__ == "__main__":
    app.run_server(debug=True)
