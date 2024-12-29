import plotly.graph_objects as go
import pandas as pd

# Load your data
data = pd.read_csv('uploads/clean_viz3.csv')
data['Time'] = pd.to_datetime(data['Time'])
data['FormattedTime'] = data['Time'].dt.to_period('Q').astype(str)

# Ensure Start and End dates are formatted in 'Q1 YYYY'
data['Start'] = pd.to_datetime(data['Start']).dt.to_period('Q').astype(str)
data['End'] = pd.to_datetime(data['End']).dt.to_period('Q').astype(str)

# Filter Example: Default to France and Price-to-Income
selected_country = 'France'
selected_metric = 'Price-to-income'
selected_papers = ['Bago et al. (2021)']

# Prepare data
filtered_data = data[data['Country'] == selected_country].copy()
metric_column = 'Price-to-income' if selected_metric == 'Price-to-income' else 'Price-to-rent'
filtered_data['Value'] = filtered_data[metric_column]

# Create the figure
fig = go.Figure()

# Add line trace
fig.add_trace(go.Scatter(
    x=filtered_data['FormattedTime'], 
    y=filtered_data['Value'], 
    mode='lines',
    line=dict(color='black'),
    name=selected_metric
))

# Highlight bubble periods
colors = ['#FF7F50', '#20B2AA', '#9370DB', '#FF4500']
for idx, paper in enumerate(selected_papers):
    paper_data = filtered_data[(filtered_data['Paper'] == paper) & (filtered_data['Bubble'] == 'Yes')]
    for _, row in paper_data.iterrows():
        fig.add_shape(
            type='rect',
            x0=row['Start'],
            x1=row['End'],
            y0=0,
            y1=max(filtered_data['Value']),
            xref='x',
            yref='y',
            fillcolor=colors[idx % len(colors)],
            opacity=0.25,
            layer='below',
            line_width=0
        )

# Customize layout
fig.update_layout(
    title=f'{selected_metric.title()} - {selected_country}',
    xaxis_title='Quarter',
    yaxis_title=f'{selected_metric.title()} Index',
    hovermode='x unified',
    template='ggplot2',  # Classical gray template
    autosize=True,
    margin=dict(l=40, r=40, t=40, b=40),
    xaxis=dict(
        tickmode='array',
        tickvals=filtered_data['FormattedTime'].unique()[::6],  # Tick every 6 quarters
        tickangle=45,
        showgrid=True,
        gridcolor='lightgrey'
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor='lightgrey'
    )
)

# Export to static HTML
fig.write_html("interactive_chart.html")
