"""
Assignment
1. In Sec2 (graph)
- Adding the 3rd figure (bar chart). This bar chart is updated based on the selection of the line
chart.
- Fix color bugs.

"""

from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.colors as colors

df = px.data.gapminder()

# Get a list of all unique countries in the dataset
all_countries = df['country'].unique()

# Define the color scale
color_scale = colors.qualitative.Bold  # Choose a predefined color scale

# Generate a dictionary mapping each country to a unique color
country_colors = dict(zip(all_countries, color_scale[:len(all_countries)]))

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Dropdown(id='dpdn2', value=['Germany','Brazil'], multi=True, options=[{'label': x, 'value': x} for x in df.country.unique()]),
    html.Div([
        dcc.Graph(id='pie-graph', figure={}, className='six columns'),
        dcc.Graph(id='my-graph', figure={}, clickData=None, hoverData=None, selectedData= None,
                  config={
                      'staticPlot': False,     # True, False
                      'scrollZoom': True,      # True, False
                      'doubleClick': 'reset',  # 'reset', 'autosize' or 'reset+autosize', False
                      'showTips': True,       # True, False
                      'displayModeBar': True,  # True, False, 'hover'
                      'watermark': True,
                      # 'modeBarButtonsToRemove': ['pan2d','select2d'],
                        },
                  className='six columns'
                  ),
        dcc.Graph(id='bar-graph', figure={}, className='six columns') # Adding the 3rd figure (bar chart)
    ])
])

@app.callback(
    Output(component_id='my-graph', component_property='figure'),
    Input(component_id='dpdn2', component_property='value'),
)
def update_graph(country_chosen):
    dff = df[df.country.isin(country_chosen)]
    fig = px.line(data_frame=dff, x='year', y='gdpPercap', color='country', color_discrete_map=country_colors, hover_data=["lifeExp", "pop", "iso_alpha"])
    fig.update_traces(mode='lines+markers')
    return fig

# Dash version 1.16.0 or higher
@app.callback(
    Output(component_id='pie-graph', component_property='figure'),
    Input(component_id='my-graph', component_property='hoverData'),
    Input(component_id='my-graph', component_property='clickData'),
    Input(component_id='my-graph', component_property='selectedData'),
    Input(component_id='dpdn2', component_property='value') ##hov เอาเมาส์ไปวาง ไม่กด ก็ยังแสดงผล
)
def update_pie_chart(hov_data, clk_data, slct_data, country_chosen):
    if hov_data is None:
        dff2 = df[df.country.isin(country_chosen)]
        dff2 = dff2[dff2.year == 1952]
        fig2 = px.pie(data_frame=dff2, values='pop', names='country', color='country', color_discrete_map=country_colors, title='Population for 1952')
        return fig2
    else:
        print(f'hover data: {hov_data}')
        # print(hov_data['points'][0]['customdata'][0])
        print(f'click data: {clk_data}')
        print(f'selected data: {slct_data}')
        ##เลือก data ได้
        dff2 = df[df.country.isin(country_chosen)]
        hov_year = hov_data['points'][0]['x']
        dff2 = df[df.country.isin(country_chosen) & (df.year == hov_year)]
        fig2 = px.pie(data_frame=dff2, values='pop', names='country', color='country', color_discrete_map=country_colors, title=f'Population for: {hov_year}')
        return fig2

@app.callback(
    Output(component_id='bar-graph', component_property='figure'),
    [Input(component_id='my-graph', component_property='hoverData'),
     Input(component_id='my-graph', component_property='clickData'),
     Input(component_id='my-graph', component_property='selectedData'),
     Input(component_id='dpdn2', component_property='value')]
)

def update_bar_chart(hov_data, clk_data, selectedData, country_chosen):
    if selectedData:
        selected_countries = [point['curveNumber'] for point in selectedData['points']]
        dff = df[df['country'].isin(country_chosen)]
        dff = dff[dff['country'].isin([dff['country'].unique()[i] for i in selected_countries])]
        fig3 = px.bar(data_frame=dff, x='country', y='lifeExp', color='country', color_discrete_map=country_colors, title='Life Expectancy by Country')
        return fig3
    elif hov_data is None:
        dff2 = df[df.country.isin(country_chosen)]
        dff2 = dff2[dff2.year == 1952]
        fig3 = px.bar(data_frame=dff2, x='country', y='lifeExp', color='country', color_discrete_map=country_colors, title='Life Expectancy for 1952')
        return fig3
    else:
        dff2 = df[df.country.isin(country_chosen)]
        hov_year = hov_data['points'][0]['x']
        dff2 = df[df.country.isin(country_chosen) & (df.year == hov_year)]
        fig3 = px.bar(data_frame=dff2, x='country', y='lifeExp', color='country', color_discrete_map=country_colors, title=f'Life Expectancy for: {hov_year}')
        return fig3
    
if __name__ == '__main__':
    app.run_server(debug=True)
