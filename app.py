
"""
🚗 Road Accidents in India (2014–2017)
Interactive Dashboard using Dash (Dark Theme - Cyborg)
"""

import os
import json
import pandas as pd
import numpy as np
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go



# 🔹 Load Dataset

CSV_PATH = "Road_Accidents_2017-Annuxure_Tables_4.csv"

if not os.path.exists(CSV_PATH):
    raise FileNotFoundError("❌ CSV not found! Place 'Road_Accidents_2017-Annuxure_Tables_4.csv' in same folder as app.py.")

df = pd.read_csv(CSV_PATH)
df.columns = [c.strip() for c in df.columns]
df['States/UTs'] = df['States/UTs'].astype(str).str.strip()

for c in df.columns[1:]:
    df[c] = pd.to_numeric(df[c], errors='coerce')

# Identify column categories
total_cols = [c for c in df.columns if 'Total Number of Persons Injured in Road Accidents during' in c]
share_cols = [c for c in df.columns if 'Share of States/UTs' in c]
per_pop_cols = [c for c in df.columns if 'Per Lakh Population' in c]
per_vehicle_cols = [c for c in df.columns if 'per 10,000 Vehicles' in c]

def extract_year(col):
    for y in ['2014', '2015', '2016', '2017']:
        if y in col:
            return y
    return None

years = sorted(list({extract_year(c) for c in total_cols if extract_year(c)}))
if not years:
    years = ['2014', '2015', '2016', '2017']


def total_col_for_year(y):
    for c in total_cols:
        if y in c:
            return c
    raise ValueError(f"No total column found for year {y}")

def per_pop_col_for_year(y):
    for c in per_pop_cols:
        if y in c:
            return c
    return None

def per_vehicle_col_for_year(y):
    for c in per_vehicle_cols:
        if y in c:
            return c
    return None

def compute_kpis(year):
    result = {
        'total': "N/A",
        'most_affected': "N/A",
        'max_per_lakh_pop_state': "N/A",
        'max_per_vehicle_state': "N/A"
    }
    try:
        col = total_col_for_year(year)
        total = int(df[col].sum(skipna=True))
        most_affected_state = df.loc[df[col].idxmax(), 'States/UTs']

        pcol = per_pop_col_for_year(year)
        vcol = per_vehicle_col_for_year(year)
        if pcol and pcol in df.columns:
            result['max_per_lakh_pop_state'] = df.loc[df[pcol].idxmax(), 'States/UTs']
        if vcol and vcol in df.columns:
            result['max_per_vehicle_state'] = df.loc[df[vcol].idxmax(), 'States/UTs']

        result['total'] = f"{total:,}"
        result['most_affected'] = most_affected_state
    except Exception as e:
        print(f"[WARN] compute_kpis error: {e}")
    return result


#  Dash App Setup (Cyborg Theme)

app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])
server = app.server
app.title = "Road Accidents in India Dashboard"


# 🔹 Layout

def kpi_card(title, id_val):
    return dbc.Card(
        dbc.CardBody([
            html.H6(title, className="card-title", style={'color': '#b0bec5'}),
            html.H3(id=id_val, style={'color': '#fff'})
        ]), color="dark", outline=False
    )

header = html.Div([
    html.H2("🚗 Road Accidents in India (2014–2017)", style={'marginBottom': '5px'}),
    html.Hr(),
    html.P("Interactive dashboard for analyzing state-wise injuries, rates, and trends.", style={'color': '#9aa0a6'})
])

controls = dbc.Row([
    dbc.Col([
        html.Label("Select Year:", style={'color': '#cfd8dc'}),
        dcc.Dropdown(
            id='year-dropdown',
            options=[{'label': y, 'value': y} for y in years],
            value='2017',
            clearable=False
        )
    ], md=3),
    dbc.Col([
        html.Label("Compare States:", style={'color': '#cfd8dc'}),
        dcc.Dropdown(
            id='states-dropdown',
            options=[{'label': s, 'value': s} for s in df['States/UTs']],
            value=[df['States/UTs'].iloc[0]],
            multi=True
        )
    ], md=6),
    dbc.Col([
        html.Label("Show Choropleth (if available):", style={'color': '#cfd8dc'}),
        dbc.Switch(id='choropleth-switch', value=False, label="")
    ], md=3)
], style={'marginBottom': '10px'})

kpi_row = dbc.Row([
    dbc.Col(kpi_card("Total Persons Injured", "kpi-total"), md=3),
    dbc.Col(kpi_card("Most Affected State", "kpi-most"), md=3),
    dbc.Col(kpi_card("Highest per Lakh Pop.", "kpi-per-pop"), md=3),
    dbc.Col(kpi_card("Highest per 10k Vehicles", "kpi-per-veh"), md=3)
], style={'marginBottom': '15px'})

graph_layout = dbc.Row([
    dbc.Col(dcc.Graph(id='bar-graph'), md=6),
    dbc.Col(dcc.Graph(id='pie-graph'), md=6),
    dbc.Col(dcc.Graph(id='line-graph'), md=7),
    dbc.Col(dcc.Graph(id='corr-graph'), md=5)
])

insights = dbc.Card(dbc.CardBody([
    html.H6("Quick Insights", style={'color': '#cfd8dc'}),
    html.Ul([
        html.Li(id='ins-top5', style={'color': '#eceff1'}),
        html.Li(id='ins-change', style={'color': '#eceff1'})
    ])
]), color="dark")

app.layout = dbc.Container([
    header,
    controls,
    kpi_row,
    graph_layout,
    html.Br(),
    insights
], fluid=True, style={'padding': '20px'})


# 🔹 Callbacks

@app.callback(
    Output('kpi-total', 'children'),
    Output('kpi-most', 'children'),
    Output('kpi-per-pop', 'children'),
    Output('kpi-per-veh', 'children'),
    Input('year-dropdown', 'value')
)
def update_kpis(year):
    k = compute_kpis(year)
    return k['total'], k['most_affected'], k['max_per_lakh_pop_state'], k['max_per_vehicle_state']


@app.callback(
    Output('bar-graph', 'figure'),
    Output('pie-graph', 'figure'),
    Output('line-graph', 'figure'),
    Output('corr-graph', 'figure'),
    Output('ins-top5', 'children'),
    Output('ins-change', 'children'),
    Input('year-dropdown', 'value'),
    Input('states-dropdown', 'value'),
    Input('choropleth-switch', 'value')
)
def update_graphs(year, selected_states, choropleth_on):
    tcol = total_col_for_year(year)
    df_sorted = df.sort_values(by=tcol, ascending=False)

    # Bar Chart
    bar_fig = px.bar(df_sorted, x='States/UTs', y=tcol, title=f"Total Injuries by State - {year}")
    bar_fig.update_layout(template='plotly_dark', xaxis_tickangle=-45, height=450)

    # Pie Chart (Top 8)
    top8 = df.nlargest(8, tcol)
    pie_fig = px.pie(top8, names='States/UTs', values=tcol, title=f"Top 8 States Share - {year}")
    pie_fig.update_layout(template='plotly_dark', height=450)

    # Line Chart (State Comparison)
    cols_years = sorted(total_cols, key=lambda c: extract_year(c) or c)
    line_fig = go.Figure()
    for st in selected_states[:4]:
        row = df[df['States/UTs'] == st]
        if not row.empty:
            vals = [row[c].values[0] for c in cols_years]
            line_fig.add_trace(go.Scatter(
                x=[extract_year(c) for c in cols_years],
                y=vals,
                mode='lines+markers',
                name=st
            ))
    line_fig.update_layout(title="Year-wise Injury Trends", template='plotly_dark',
                           height=450, xaxis_title="Year", yaxis_title="Total Injuries")

    # Correlation Heatmap
    num_df = df.select_dtypes(include=[np.number]).copy()
    corr = num_df.corr()

    # Shorten & Deduplicate Column Names
    def make_unique(lst):
        seen, result = {}, []
        for x in lst:
            if x not in seen:
                seen[x] = 1
                result.append(x)
            else:
                seen[x] += 1
                result.append(f"{x}_{seen[x]}")
        return result

    short_names = {}
    for i, col in enumerate(corr.columns):
        name = col.replace("State/UT-wise Total Number of Persons Injured in Road Accidents during - ", "Injured-")
        name = name.replace("Total Number of Persons injured in Road Accidents per", "Rate-")
        name = name.replace("Share of States/UTs in Total Number of Persons Injured in Road Accidents - ", "Share-")
        short_names[col] = f"{name[:40]}_{i}"

    corr_short = corr.rename(index=short_names, columns=short_names)
    corr_short.columns = make_unique(list(corr_short.columns))
    corr_short.index = corr_short.columns

    corr_fig = px.imshow(
        corr_short,
        text_auto='.2f',
        title="Correlation Heatmap (numeric)",
        color_continuous_scale='plasma',
        aspect="auto"
    )
    corr_fig.update_layout(template='plotly_dark', height=500, margin=dict(l=120, r=20, t=60, b=120))

    # Insights
    df['total_2014_2017'] = df[total_cols].sum(axis=1, skipna=True)
    top5 = df.nlargest(5, 'total_2014_2017')['States/UTs'].tolist()
    ins_top5 = "Top 5 states (2014–2017 total injuries): " + ", ".join(top5)

    col14 = sorted(total_cols, key=lambda c: extract_year(c) or c)[0]
    col17 = sorted(total_cols, key=lambda c: extract_year(c) or c)[-1]
    df['change_14_17'] = df[col17] - df[col14]
    df_sorted = df.sort_values('change_14_17', ascending=False)
    ins_change = f"Highest increase: {df_sorted.iloc[0]['States/UTs']} | Decrease: {df_sorted.iloc[-1]['States/UTs']}"

    return bar_fig, pie_fig, line_fig, corr_fig, ins_top5, ins_change

#  Run App

if __name__ == "__main__":
    app.run(debug=True, port=8050)
