import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(
            "PM Release Automation",
            style={"textAlign": "center", "marginTop": "40vh", "color": "#333"},
        ),
        html.P(
            "Welcome",
            style={"textAlign": "center", "color": "#666", "fontSize": "18px"},
        ),
    ],
    style={
        "backgroundColor": "white",
        "minHeight": "100vh",
        "margin": "0",
        "padding": "0",
        "fontFamily": "Segoe UI, sans-serif",
    },
)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8050)
