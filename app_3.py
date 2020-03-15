import dash
import dash_core_components as dcc 
import dash_html_components as html 
import plotly.graph_objs as go
import pandas as pd 
import numpy as np 


# investigate dataframe 
orders =pd.read_csv('sales_data_sample.csv',encoding='ISO-8859-1')

#print(orders.info())




# calling app

app=dash.Dash()
server=app.server 




app.layout = html.Div ([ 
    dcc.Graph(
        id='scatter_chart',
        figure = {
            'data': [
                go.Scatter(
                    x=orders.QUANTITYORDERED,
                    y=orders.SALES,
                    mode='markers',
                    marker=dict(
                        size=10,
                        line=dict(
                            color='MediumPurple',
                            width=2
                    ))
                    
                )

            ],
            'layout':go.Layout(
                title = 'Scatterr randome plot',
                xaxis={'title':'Order quantity'},
                yaxis={'title':'Sales'},
                hovermode='closest'
                )
        
        }
    )
])


if __name__ == '__main__':
    app.run_server(port=4050)
