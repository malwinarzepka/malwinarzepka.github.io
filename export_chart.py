import dash
from dash import dcc, html
import plotly.graph_objects as go
import pandas as pd

# Load the data
data = pd.read_csv('uploads/clean_viz3.csv')  # Update path if needed
data['Time'] = pd.to_datetime(data['Time'])
data['FormattedTime'] = data['Time'].dt.to_period('Q').astype(str)

# Ensure Start and End dates are formatted
data['Start'] = pd.to_datetime(data['Start']).dt.to_period('Q').astype(str)
data['End'] = pd.to_datetime(data['End']).dt.to_period('Q').astype(str)

# Initialize Dash app
app = dash.Dash(__name__)

# Dropdown options
countries = data['Country'].unique()
metrics = ['Price-to-income', 'Price-to-rent']
papers = data['Paper'].unique()

# Layout
app.layout = html.Div([
    html.H1("Interactive Housing Bubble Chart"),
    
    html.Label("Select Country:"),
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': c, 'value': c} for c in countries],
        value=countries[0]  # Default selection
    ),
    
    html.Label("Select Metric:"),
    dcc.Dropdown(
        id='metric-dropdown',
        options=[{'label': m, 'value': m} for m in metrics],
        value=metrics[0]  # Default selection
    ),
    
    html.Label("Select Papers:"),
    dcc.Dropdown(
        id='paper-dropdown',
        options=[{'label': p, 'value': p} for p in papers],
        value=[papers[0]],  # Default selection
        multi=True  # Allow multiple selections
    ),
    
    dcc.Graph(id='bubble-chart')  # Placeholder for chart
])

# Callback to update the chart dynamically
@app.callback(
    dash.dependencies.Output('bubble-chart', 'figure'),
    [
        dash.dependencies.Input('country-dropdown', 'value'),
        dash.dependencies.Input('metric-dropdown', 'value'),
        dash.dependencies.Input('paper-dropdown', 'value')
    ]
)
def update_figure(selected_country, selected_metric, selected_papers):
    # Filter data based on selection
    filtered_data = data[data['Country'] == selected_country].copy()
    metric_column = 'Price-to-income' if selected_metric == 'Price-to-income' else 'Price-to-rent'
    filtered_data['Value'] = filtered_data[metric_column]

    # Create figure
    fig = go.Figure()

    # Add line trace
   
