import dash
import dash_core_components as dcc 
import dash_html_components as html 
import plotly.graph_objs as go
import pandas as pd 
import numpy as np 


#creating layout colors
colors ={
    'text':'red',
    'plot_color':'white',
    'paper_color':'gray'
}

# create raandome variable 
np.random.seed(50)
x_rand=np.random.randint(1,61,60)
y_rand=np.random.randint(1,61,60)

# calling app

app=dash.Dash()
server=app.server 

'''

    html.H1(children= 'Hello Dash !',
            style={
                'textAllign':'center',
                'color':colors['text']
            }
            ),
    html.Div(children= 'Dash Data product development',
            style={
                'textAllign':'center',
                'color':colors['text']

            }
            ),

'''
app.layout = html.Div ([ 
    dcc.Graph(
        id='scatter_chart',
        figure = {
            'data': [
                go.Scatter(
                    x=x_rand,
                    y=y_rand,
                    mode='markers',
                    marker=dict(
                        size=20,
                        line=dict(
                            color='MediumPurple',
                            width=2
                    ))
                    
                )

            ],
            'layout':go.Layout(
                title = 'Scatterr randome plot',
                xaxis={'title':'Random X value'},
                yaxis={'title':'Random Y value'}
                )
        
        }
    )
])


if __name__ == '__main__':
    app.run_server(port=4050)