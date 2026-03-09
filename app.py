import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

df = pd.read_csv('StockData.csv')

companies = sorted(df['Company'].unique())
colors = ['#FF8000', '#D1C9C9', '#348A53', '#004AEF', '#E82127']
color_map = {company: color for company, color in zip(companies, colors)}
months = df['Month'].unique().tolist()

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Stock Market Analysis Dashboard",
            style={'textAlign': 'center', 'fontWeight': 'bold', 'fontFamily': 'Times New Roman'}),
    html.Div([
        html.Label("Select Month:", style={'fontWeight': 'bold', 'marginRight': '5px', 'textAlign': 'center'}),
        dcc.Dropdown(
            id='month-dropdown',
            options=[{'label': m, 'value': m} for m in months],
            value=months[0],
            style={'width': '165px', 'display': 'inline-block', 'verticalAlign': 'middle'}
        ),
        html.Label("Select Stock Price Metric:", style={'fontWeight': 'bold', 'marginLeft': '365px', 'marginRight': '5px'}),
        dcc.RadioItems(
            id='metric-radio',
            options=[{'label': m, 'value': m} for m in ['Open', 'Close', 'High', 'Low']],
            value='Open',
            inline=True,
            style={'display': 'inline-block', 'verticalAlign': 'middle'}
        ),
    ], style={'display': 'flex', 'alignItems': 'center', 'padding': '15px 25px',
              }),
    html.Div([
        dcc.Graph(id='bar-chart', style={'width': '50%'}),
        dcc.Graph(id='box-plot', style={'width': '50%'})
    ], style={'display': 'flex'})
], style={'fontFamily': 'Times New Roman', 'maxWidth': '1200px', 'margin': '0 auto'})

@app.callback(
    Output('bar-chart', 'figure'),
    Output('box-plot', 'figure'),
    Input('month-dropdown', 'value'),
    Input('metric-radio', 'value')
)
def charts(month, metric):
    matched = df[df['Month'] == month]

    avg_df = matched.groupby('Company')[metric].mean().reset_index()
    bargraph = px.bar(
        avg_df, x='Company', y=metric,
        color='Company',
        color_discrete_map=color_map,
        title=f'Average {metric} Prices of Each Company',
        labels={metric: f'Average {metric} Price'}
    )
    bargraph.update_layout(showlegend=True)

    boxgraph = px.box(
        matched, x='Company', y=metric,
        color='Company',
        color_discrete_map=color_map,
        title=f'Stock {metric} Price Distributions',
        labels={metric: metric}
    )
    (boxgraph.update_layout(showlegend=True))

    return bargraph, boxgraph

if __name__ == '__main__':
    app.run(debug=True)