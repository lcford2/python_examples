import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)
server = app.server

if __name__ == "__main__":
	app.run_server(debug=True)
