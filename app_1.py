import dash
import dash_core_components as dcc 
import dash_html_components as html 



# calling app

app=dash.Dash()
server=app.server 


app.layout = html.Div ([ 
    html.H1('Hello Dash !'),
    html.Div('Dash Data product development')
])



if __name__ == '__main__':
    app.run_server(port=4050)