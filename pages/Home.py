# + -------------------------- +
# +          Home Page         +
# + -------------------------- +
# + ---- import libraries ---- +

import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import dash_extensions as de

# + ---- page registration ---- +
''' - Register page with dash.register_page(__name__)
    - define layout as a function, call from app.py '''
dash.register_page(__name__,
                   name= 'Home',
                   top_nav= True,
                   path= '/')

# + ---- fonts // custom css ---- +
''' See Typography.css for Font and other styling  '''


# + ---- lottie ---- +
''' Import Lottie animation files and build them into a container. '''
url1= "https://lottie.host/64e00cda-12a8-4cb9-b6dc-d7209c57b203/kWelZVLc6e.json"    # Mechanical_Idea
url2= "https://lottie.host/c1abd37f-e19a-4be5-85cc-f881a6f6f34c/6TiB1y3gl7.json"    # fiveAxis
url3= "https://lottie.host/17045d7c-e3b2-47b6-a76f-fc71a4ab63c4/jtk56PCzrd.json"    # Electro_Mag
options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))

# Lottie annimation 1
mechIdea= dbc.Container(
    [
        html.Div(de.Lottie(options= options, speed= 0.5, width= '40%', height= '40%', url= url1))
    ],
    fluid= True,
    class_name= 'justify-content-start pm-0',
)

# Lottie annimation 2
fiveAxis= dbc.Container(
    [
        html.Div(de.Lottie(options= options, width= '40%', height= '40%', url= url2))
    ],
    fluid= True,
    class_name= 'justify-content-center pm-0',
)

# Lottie annimation 3
electMag= dbc.Container(
    [
        html.Div(de.Lottie(options= options, width= '35%', height= '35%', url= url3))
    ],
    fluid= True,
    class_name= 'justify-content-center pm-0',
)

# + ---- layout ---- +
layout = dmc.Container(
    [
        html.Br(),
        dbc.Row([], className= 'bg-light'),
        dbc.Row(
            [
                dbc.Col(html.Div(), class_name= 'bg-light'),                                      # gutter column
                dbc.Col(html.Div(), class_name= 'bg-light'),                                      # gutter column
                dbc.Col(html.Div(
                    [
                        dmc.Paper(children= [
                                dbc.Row(
                                    [
                                        html.H3('Welcome', className= 'mb-0'),
                                        html.H6('Thank You for visiting my Web-App', className= 'mb-0 fst-italic', style= {'font-weight': 200}),
                                        html.Br(),
                                    ],
                                ),
                                html.Br(),
                                dmc.Divider(size= 'xs'),
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            [
                                                html.Br(),
                                                html.Div(
                                                    [mechIdea],                # Annimation
                                                    className= 'p-0',
                                                ),
                                                html.Br(),
                                            ],
                                            width= 2,
                                        ),
                                        dbc.Col(
                                            [
                                                html.Br(),
                                                html.Div(
                                                    [
                                                        html.P('This is the 1st Content Div')
                                                    ],
                                                    style= {'text-align': 'start'},
                                                ),
                                            ], width= 8,
                                        ),
                                        dbc.Col(
                                            [
                                                html.Br(),                                         # gutter in row 1
                                            ], width= 1,
                                        )
                                    ],
                                ),
                                dmc.Divider(size= 'md'),
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            [
                                                html.Br(),                                          # gutter in row 2
                                            ],
                                            width= 1,
                                        ),
                                        dbc.Col(
                                            [
                                                html.Br(),
                                                html.Div(
                                                    [
                                                        html.P('This is the 2nd Content Div')  # --> PUT CONTENT HERE for 2nd Div
                                                    ],
                                                    style= {'text-align': 'start'},
                                                ),
                                            ],
                                            width= 8,
                                        ),
                                        dbc.Col(
                                            [
                                                html.Br(),
                                                html.Div(
                                                    [fiveAxis],                                       # --> Put Annimation or icon here for 2nd Div
                                                    className= 'p-0',
                                                ),
                                                html.Br(),
                                            ],
                                            width= 2,
                                        )
                                    ],
                                ),
                                dmc.Divider(size= 'xl'),
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            [
                                                html.Br(),
                                                html.Div(
                                                    [electMag],                                     # --> Put Annimation or icon for 3rd Div
                                                    className= 'pb-1',
                                                ),
                                                html.Br(),
                                            ],
                                            width= 2,
                                        ),
                                        dbc.Col(
                                            [
                                                html.Br(),
                                                html.Div(
                                                    [
                                                        html.P('This is the 3rd Content Div')
                                                    ],
                                                    style= {'text-align': 'start'},
                                                ),
                                            ],
                                            width= 8,
                                        ),
                                        dbc.Col(
                                            [
                                                html.Br(),                                        # gutter in row 3
                                            ],
                                            width= 1,
                                        )
                                    ],
                                )
                            ],
                            shadow= 'lg',
                            p= 'lg',
                            radius= 'md',
                            ta= 'center',
                        ),
                    ]
                ),
                width= 9),
                dbc.Col(html.Div(), class_name= 'bg-light'),                                      # gutter column
                dbc.Col(html.Div(), class_name= 'bg-light'),                                      # gutter column
            ],
            className= 'bg-light',
        ),
        dbc.Row([], className= 'bg-light'),
    ],
    fluid= True,
    className= 'bg-light'
)
