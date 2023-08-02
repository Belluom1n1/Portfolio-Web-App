# + -------------------------- +
# +       Projects Page        +
# + -------------------------- +
# + ---- import libraries ---- +
import dash
from dash import html
import dash_bootstrap_components as dbc

# + ---- page registration ---- +
dash.register_page(__name__,
                   name= 'Projects',
                   top_nav= True,
                   path= '/Projects',
                   custom_key= 'Projects')


# + ---- layout ---- +
layout = html.Div(
    [
        html.H1('Projects Page')
    ]
)

'''
Use Cards and Tabs to display projects in different areas?  
    -> Data Science // Fantasy Football ?
    -> School Projects RVM, Smart Parking System
    -> Certifications, etc. 
'''