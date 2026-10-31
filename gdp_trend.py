import dash
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Sample dataset (GDP Trend)
data = {
    "Year": [2018, 2019, 2020, 2021, 2022],
    "India": [2.7, 4.2, -7.3, 9.1, 6.7],
    "USA": [2.9, 2.3, -3.4, 5.9, 2.1],
    "China": [6.7, 6.1, 2.3, 8.1, 3.0]
}

df = pd.DataFrame(data)

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Interactive Dashboard Example", style={"textAlign": "center"}),

    dcc.Dropdown(
        id="country-dropdown",
        options=[
            {"label": "India", "value": "India"},
            {"label": "USA", "value": "USA"},
            {"label": "China", "value": "China"}
        ],
        value="India"
    ),

    dcc.Graph(id="gdp-chart")
])

@app.callback(
    Output("gdp-chart", "figure"),
    Input("country-dropdown", "value")
)
def update_graph(selected_country):
    fig = px.line(
        df,
        x="Year",
        y=selected_country,
        title=f"GDP Growth of {selected_country}"
    )
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)