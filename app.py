'''
  -> Brian Belluomini
  -> Portfolio-Web-App

  -> To run application, type python App.py in the terminal &
     visit https://127.0.0.1:8050 in your web browser.
'''
# + --- imports --- +
import dash
from dash import html, dcc, Dash
import dash_bootstrap_components as dbc

# + --- initialization --- +
app = dash.Dash(__name__,
           use_pages= True,
           external_stylesheet= [dbc.themes.FLATLY])


# + --- laypout --- +
''' This is the only page that should contain a 'app.layout' function.
    For other app Pages or Elements, define the layout as a function.
'''
# app.layout =

