import dash
import dash_core_components as dcc 
import dash_html_components as html 
import plotly.graph_objs as go
import pandas as pd 
import numpy as np
from datetime import datetime as dt 


# investigate dataframe 
orders =pd.read_csv('sales_data_sample.csv',encoding='ISO-8859-1')

#print(orders.info())




# calling app

app=dash.Dash()
server=app.server 



app.layout=html.Div([
    html.Label('Choose a City'),
    dcc.Dropdown(
        id = 'first-dropdown',
        options=[
            {'label':'San fransisco','value':'SF'},
            {'label':'New York City','value':'NYC'},
            {'label':'Miami','value':'MIA','disabled':True}
        ],
        placeholder='Select a City',
        multi=True
    ),
    html.Label("this is a slider"),
    dcc.Slider(
        min=1,
        max=10,
        value=5,
        step=0.5,
        marks={i:i for i in range(10)}

    ),
    html.Label("Range slider"),
    dcc.RangeSlider(
        min=1,
        max=10,
        step=0.5,
        value=[3,7],
        marks={i:i for i in range(10)}
    ),
    html.Label("this is the input box"),
    dcc.Input(
        placeholder="Input your name",
        type="text",
        value=''
    ),
    dcc.Textarea(
        placeholder="Input your feedback",
        value="Placeholder for text",
        style={'width':'100%'}
    ),
    dcc.Checklist(
        options=[
            {'label':'San fransisco','value':'SF'},
            {'label':'New York City','value':'NYC'},
            {'label':'Miami','value':'MIA'}
        ],
        value=['SF','NYC']  
    ),
    html.Button('Submit', id='submit button'),


    html.Br(),
    html.Br(),
    dcc.RadioItems(
        options=[
            {'label':'San fransisco','value':'SF'},
            {'label':'New York City','value':'NYC'},
            {'label':'Miami','value':'MIA'}
        ],
        value='SF'     
    ),
    html.Br(),
    html.Br(),
    dcc.DatePickerSingle(
        id='dt-pick-single',
        date=dt(2020,3,12)
    ), 
    html.Br(),
    html.Br(),
    dcc.DatePickerRange(
        id='dtpickrange',
        start_date=dt(2015,1,1),
        end_date_placeholder_text='specify the date'

    ),

    dcc.Markdown(
        '''
        something very nice and very easy 
        http://www.google.com
        
        '''
    )

])

if __name__ == '__main__':
    app.run_server(port=4050)
