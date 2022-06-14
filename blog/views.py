from django.shortcuts import render

# import for plot a graph
from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly.graph_objs as go

# import to properly see in browser
from django.http import HttpResponse

# data analysis
import pandas as pd

# data visualization
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly
import numpy as np
from matplotlib.figure import Figure

# Create your views here.

def index(request):
   
    return render(request, "blog/index.html")

## graphs page
#def graphs(request):
#
#    line_graph_annotation=[
#        dict(
#        #xref='paper',
#        #yref='paper',
#        x=0,
#        y=12.8,
#        showarrow=True,
#        text='pitch yeast', 
#        bgcolor='white',
#        opacity=0.8,
#        arrowwidth=2,
#        arrowhead=1,
#        arrowsize=1,
#        font=dict(size=13, color='black', family="Courier New, monospace")
#        ), 
#        dict(
#        x=0,
#        y=10,
#        text=f'lag phase<br>3 to 15 hours<br>after pitching',
#        bgcolor='red',
#        showarrow=False,
#        opacity=0.8,
#        font=dict(size=13, color='white')
#        ), 
#        dict(
#        x=2.5,
#        y=6,
#        text=f'Exponential Growth Phase<br>One to Four days',
#        bgcolor='blue',
#        showarrow=False,
#        opacity=0.8,
#        font=dict(size=13, color='white')
#        ), 
#        dict(
#        x=6.5,
#        y=11,
#        text=f'Stationary Phase of<br>Yeast Growth:<br>Three to 10 Days',
#        bgcolor='green',
#        showarrow=False,
#        opacity=0.8,
#        font=dict(size=13, color='white')
#        ), 
#       # dict(
#       # #x=1,
#       # yref='paper',
#       # x=0,
#       # y=-1.5,
#       # #xshift=-5,
#       # #text='Difference between ideal and real plato drop rate<br>can be due to temperature, pH, pitch amount, among others',
#       # #bgcolor='green',
#       # showarrow=False,
#       # opacity=0.8,
#       # font=dict(size=13)#, color='white')
#
#       ]
#
#
#    line_graph_shape=[
#           # dict(
#           # type='line',
#           # yref='paper', y0=0, y1=1,
#           # xref='x', x0=0, x1=0,
#           # line=dict(color='red',
#           #     width=3, dash="dot")
#           # ),
#            dict(type='line',
#                yref='paper', y0=0, y1=1,
#                xref='x', x0=1, x1=1,
#                line=dict(color='blue',
#                    width=3, dash='dot')
#            ),
#            dict(type='line',
#                yref='paper', y0=0, y1=1,
#                xref='x', x0=4, x1=4,
#                line=dict(color='green',
#                    width=3, dash='dot')
#
#    )]
#
#    line_graph_margin = dict(
#            l=1, 
#            r=20, 
#            t=25, 
#            b=1)
#    
#
#    line_graph_layout = {
#            'title': 'Plato degree vs Days of fermentation',
#            'xaxis_title': 'Days',
#            'yaxis_title': 'Plato',
#            #'width': 800,
#            #'height': 400,
#            'annotations': line_graph_annotation,
#            'shapes': line_graph_shape,
#            'xaxis_range':[-2,11],
#            'yaxis_range':[2,16],
#            #'margin': line_graph_margin,
#    }
#            
#            #'grid': True,
#            
#
#    x_data = [0,1,2,3,4,5,6,7,8,9,10,11]
#    y2_data = [12.8, 12.6, 12.2,11.7,10.3,9.6,7.1,5.8,4.7,3.7,3.5]
#    y2_ideal = [12.8, 12,11.5,10,9.2,7,5.1,4,3.5,3.5]
#
#    line_graphs = []
#    line_graphs.append(
#
#            go.Scatter(name='Data', x=x_data, y=y2_data, mode='lines+markers')
#    )
#    
#    line_graphs.append(
#        go.Scatter(name='Ideal', x=x_data, y=y2_ideal, mode='lines+markers')
#    )
#
#    #pH scale
#    ph_scale = []
#    ph_scale_valuesy = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
#    ph_scale_valuesx = [1,1,1,1,1,1,1,1,1,1,1,1,1,1]
#    
#    ph_tick_values = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
#
#    ph_scale_layout={
#            'showlegend': False,
#            #'hiddenlabels': True,
#            #'showlegend': True,
#            #'xaxis_range':[1,1],
#            'xaxis_title': 'Critical Control Points (CCP) for<br> Quality Control (QC)',
#            'yaxis_title': 'Acidic-Base similar',
#            'title': 'pH scale for different elements of production',
#            'yaxis_range':[-0.5,15],
#            'yaxis':dict(tickmode='array',
#                        tickvals=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14],
#                        ticktext=['Battery Acid', #0 
#                                  'Stomack acid'    #1
#                                  ,'Vinegar',   #2
#                                  'Lemon juice',    #3
#                                  'Grapefuit juice', #4
#                                  'Black coffee', #5
#                                  'Milk', #6
#                                  'Water', #7
#                                  'blood ',#8 
#                                  'Baking soda',
#                                  'Indigestion tablet',
#                                  'ammonia solution', 
#                                  'soapy water',
#                                  'Bleaches', 
#                                  'Liquid drain cleaner'])
#            #'tickvals': ph_tick_values,#[1,2,3,4,5,6,7,8,9,10,11],
#            #'ticktect': ph_tick_label,#['Baterry Acid', 'Lemon juice', 'Grapefuit juice','Black coffee', 'Milk', 'Blood', 'Sea water', 'Baking soda','ammonia solution', 'Bleaches', 'Liquid drain cleaner'],
#            #'coloraxis': ph_scale_valuesy,
#            #'update_traces':dict(layout_showlegend=False),
#            #'textposition': 'top center',
#    }
#
#    #ph_scale.append(
#
#    #        go.Bar(name='1',x=['Equally important<br>Elements'], y=[0], showlegend=False)
#    #        )
#    #ph_water_ideal = []
#
#
#    #ph_scale.append(
#
#    #        go.Scatter(x=ph_tick_label, y=ph_tick_values, mode='markers', marker=dict(size=8, color=ph_scale_valuesy, showscale=True))
#
#    #)
#    #ph_scale.append(
#    #        go.Scatter(x=ph_tick_label, y=ph_water_ideal, mode='markers')
#    #)
#
#    ph_scale.append(
#
#            go.Scatter(name='pH',x=['brewing<br>water', 'mash', 'sparge', 'wort', 'yeast', 'beer'], 
#                y=[6.1,5.4,5.7,5.4,4.2,4.3], mode='markers', marker=dict(size=8, color=ph_scale_valuesy, showscale=True), showlegend=True,)
#
#            )
#
#
#    ph_scale_div = plot({'data': ph_scale, 'layout': ph_scale_layout},
#            output_type='div')
#            
#
#    #line_graph_div = plot({'data': line_graphs, 'layout': line_graph_layout},
#    #        output_type='div')
#
#
#
#
#    #pH_Line graph
#    ph_table_annotation=[
#            dict(
#                x=0,
#                y=-0.15,
#                text='target values in ppm',
#                showarrow= False,
#    )]
#
#
#            #'showarrow': False,
#    ph_table_layout = {
#            'title': 'Adjust your water supply to replicate historical famous brewing Centers',
#            'width': 800,
#            'height': 400,
#            'annotations': ph_table_annotation,
#    }
#
#
#    ph_table = []
#
#    ph_table.append(
#            go.Table(header=dict(values=['City', 'Calcium', 'Magnesium', 'Bicarbonate', 'Sulfate', 'Chloride', 'Beer Style']),
#                cells=dict(values=[['Pilsen', 'Dormuntd', 'Vienna', 'Munich', 'London', 'Edinburgh', 'Burton'],
#                    [10, 225, 163, 109, 52, 100, 352],[3, 40,68,21,32,18,24],[3,220,243,171,104,160,320],
#                    [4,120,216,79,32,105,802],[4,60,39,36,34,45,16],
#                    ['Pilsner', 'Export Lager', 'Vienna Lager', 'Oktoberfest', 'British Bitter', 'Scottish Ale', 'India Pale Ale']]))
#    )
#
#    
#
#    #ph_graph_div = plot({'data': ph_bar_graph, 'layout': bar_chart_brew_layout}, output_type='div')
#
#
#    ph_bar_graph = []
#
#    target_pH = [6.0, 5.4, 5.7, 5.4, 4.3, 4.3]
#    pH_element = ['Brewing Water','Mash','Sparge', 'Wort','Yeast','Beer']
#
#    ph_text = [
#            dict
#            (
#            #xref='paper',
#            #yref='paper',
#            x='Brewing Water',
#            y=-2.5,
#            showarrow=False,
#            text='text',
#            #textposition='auto',
#            #='auto',
#            #bgcolor='white',
#            #opacity=0.8,
#            #arrowwidth=2,
#            #arrowhead=1,
#            #arrowsize=1,
#            #font=dict(size=13, color='black', family="Courier New, monospace")
#
#    )]
#
#    bar_chart_brew_layout = {
#            'title': 'Target pH for different processes and elements during brewing, all equally important',
#            'width': 800,
#            'height': 400,
#            #'xaxis_title': '',
#            'yaxis_title': 'pH',
#            #'barmode': 'group',
#            #'textposition': 'auto',
#            #'annotations': ph_text,
#    }
#
#    ph_bar_graph.append(
#            
#            go.Bar(name='target', x =pH_element, y =target_pH, text=target_pH)
#    )
#
#    ph_graph_div = plot({'data': ph_bar_graph, 'layout': bar_chart_brew_layout}, output_type='div')
#    ph_table_div = plot({'data': ph_table, 'layout': ph_table_layout}, output_type='div')
#
#
#    # SPAIN BAR GRAPH    
#    data_spain = ['empty houses', 'houses estimated', 'homeless people']
#    #sp_population = 46647425
#
#    # POPULATION BAR GRAPH
#    bar_chart_pop_layout = {
#            'title': 'Empty vs Total amount of households in Spain 2017',
#            'width': 800,
#            'height': 400,
#            'xaxis_title': 'Spain household data',
#            'yaxis_title': 'Population',
#            'barmode': 'group',
#    }
#
#    data = pd.read_csv('blog/static/country-pop.csv')
#
#    current_population = data[data['Year'] == 2020][:20]
#    #plt.rcParams['figure.figsize'] = (25, 7)
#
#    bar_charts = []
#    #bar_charts.append(
#    #    go.Bar(x=current_population['Country'][:20], y=current_population['Population'][:20])
#    #)
#
#    bar_charts.append(
#
#            go.Bar(name='Empty houses', x=data_spain[0:1], y=[3443365]),
#            )
#    
#    bar_charts.append(
#            go.Bar(name='Total households', x=data_spain[1:2], y=[17500000])
#    )
#    #bar_charts.append(
#
#    #        go.Bar(name='Homeless people', x=data_spain[2:3], y=[40000])
#    #        )
#    
#    
#    line_graph_div = plot({'data': line_graphs, 'layout': line_graph_layout},
#            output_type='div')
#    
#    bar_chart_pop_div = plot({'data': bar_charts, 'layout': bar_chart_pop_layout}, 
#            output_type='div')
#
#
#
#    # POPULATION MAP
#    country = px.data.gapminder()
#
#
#    map_fig = px.scatter_geo(country, locations="iso_alpha", 
#            color='continent',
#            hover_name='country', 
#            size='pop', 
#            animation_frame='year',
#            projection="natural earth")
#
#
#
#    map_div = plot(map_fig, output_type='div')
#
#    #pop_data = px.data.gapminder().query("continent == 'Europe' and year == 2007 and pop > 2.e6")
#    pop_data = px.data.gapminder().query("continent == 'Europe' and year == 2007 and pop > 2.e6").head(10)
#    #pop_data.head(10)
#
#    pop_fig = px.bar(pop_data, y='pop', x='country', text='pop')
#
#    population_div = plot(pop_fig, output_type='div')
#    
#    
#
#
#
#
#
#    return render(request, "blog/graphs.html", context={'line_graph_div': line_graph_div,
#                                                        'ph_graph_div': ph_graph_div,
#                                                        'ph_table_div': ph_table_div,
#                                                        'bar_chart_pop_div': bar_chart_pop_div,
#                                                        'map_div': map_div,
#                                                        'ph_scale_div': ph_scale_div,
#                                                        'population_div': population_div})
#
#def guis(request):
#    
#
#    return render(request, 'blog/guis.html')
