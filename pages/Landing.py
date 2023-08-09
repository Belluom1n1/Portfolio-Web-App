# + ----------------- +
# +   Landing Page    +
# + ----------------- +
# + ---- library imports ---- +
import dash
from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

# + ---- resume modal ---- +

# + ---- page registration ---- +
dash.register_page(__name__,
                   name= 'Contact',
                   top_nav= True,
                   path= '/Contact',
                   custom_key= 'Contact')


# + ---- icons // buttons --- +
'''
Refer to these comments for accordion title styling.

    myRes = html.I(className= 'p-3 fa-regular fa-file-lines fa-xl')
    myGit = html.I(className= 'p-3 fa-brands fa-github fa-xl')
    myLinked = html.I(className= 'p-3 fa-brands fa-linkedin fa-xl')
'''

# + ---- layout ---- +
layout = dbc.Container([
    html.Div(
        dbc.Row([
            dbc.Col([
                html.Br(),
                dmc.Paper(
                    [
                        dmc.Grid(
                            children= [
                                dmc.Col(
                                    html.Div(
                                        [
                                            # Name
                                            # Student of Mech E.
                                        ]
                                    ), span= 8,
                                )
                            ],
                            grow= True,
                            gutter= 'md',
                        ),
                        dmc.Grid(
                            children= [
                                dmc.Col(
                                    html.Div(
                                        [
                                            # Contact Info
                                        ]
                                    ), span= 5,
                                ),
                                dmc.Col(
                                    html.Div(
                                        [
                                            # work timeline
                                        ]
                                    ), span= 3,
                                )
                            ],
                            gutter= 'md',
                        ),
                        html.Br(),
                    ],
                    shadow= 'xl',
                    p= 'lg',
                    radius= 'md',
                ),
                html.Br(),
            ],
            width= {'size': 8, 'padding': 2}),
        ],
        justify= 'center')
    )
],
fluid= True,
style= {'background-color': '#ecf0f1'})
