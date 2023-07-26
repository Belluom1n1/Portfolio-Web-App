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
app = Dash(__name__,
           use_pages= True, 
           external_stylesheet= [dbc.themes.FLATLY])
