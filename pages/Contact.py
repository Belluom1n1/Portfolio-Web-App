# + ----------------- +
# +   Contact Page    +
# + ----------------- +
# + ---- library imports ---- +
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

# + ---- page registration ---- +
dash.register_page(__name__,
                   name= 'Contact',
                   top_nav= True,
                   path= '/Contact',
                   custom_key= 'Contact')

# + ---- icons // buttons --- +
#Refer to these comments for accordion title styling.

#   -> myRes = html.I(className= 'p-3 fa-regular fa-file-lines fa-xl')
#   -> myGit = html.I(className= 'p-3 fa-brands fa-github fa-xl')
#   -> myLinked = html.I(className= 'p-3 fa-brands fa-linkedin fa-xl')

# + ---- layout ---- +
layout = dbc.Container([
    html.Div(
        dbc.Row([
            dbc.Col([
                html.Br(),
                dmc.Paper(
                    [
                        html.H2('Brian Belluomini', id= 'h2', className= 'mb-1'),
                        dcc.Markdown('#### _Student of Mechanical Engineering_', id= 'h4-sub', style= {'font-weight': 200}),
                        html.Hr(className= 'mt-2 mb-3'),
                        html.Br(),
                        html.H4('Phone:', style= {'font-weight': 300}, id= 'h4'),
                        html.Hr(style= {'width': '50%'}),
                        dcc.Markdown('_916-955-6175_'),
                        html.Br(),
                        html.H4('Location:', style= {'font-weight': 300}, id= 'h4'),
                        html.Hr(style= {'width': '50%'}),
                        dcc.Markdown('_Sacramento, CA. 95608_'),
                        html.Br(),
                        html.H4('Email:', style= {'font-weight': 300}, id= 'h4'),
                        html.Hr(style= {'width': '50%'}),
                        html.Br(),
                        dcc.Markdown('''
                             * _email_1_

                             * _email_2_
                             '''),
                        html.Br(),
                        dcc.Markdown('#### Education:'),
                        html.Hr(style= {'width': '50%'}),
                        dcc.Markdown('''
                            - **California State University, Sacramento** | Sacramento, CA. \n
                                _Bachelor's of Science in Mechanical Engineering (BSME)_ \n
                                _Graduated in Fall 2023_

                            - **California State University, Sacramento** | Sacramento, CA. \n
                                _Master's of Science in Mechanical Engineering (MSME)_ \n
                                _Expected Graduation in Spring 2025_
                             '''),
                        html.Br(),
                        html.H4('Links:'),
                        html.Hr(style= {'width': '50%'}),
                        html.Div(
                            dbc.Accordion(
                                [
                                    dbc.AccordionItem(      # Resume Item
                                        [
                                            html.I(className= 'p-2 ms-1 fa-regular fa-file-lines fa-xl', style= {'color': '#bf3fd6'}),
                                            '  Click on the icon to right to view my Resume.',
                                        ],
                                        title= 'Resume',
                                        class_name= 'dbc',
                                    ),
                                    dbc.AccordionItem(     # Github Item
                                        [
                                            html.A(html.I(className= 'p-2 ms-1 fa-brands fa-github fa-xl', style= {'color': '#9d34b0'}), href= 'https://github.com/Belluom1n1', target= '_blank'),
                                            "     You can visit my public Github page through the link embedded in the icon,",
                                            html.P("or by clicking the icon on the header.", className= 'mx-5'),
                                            html.P('Note:  Repositories may not be regularly maintained.', className= 'text-warning fst-italic mx-5'),
                                        ],
                                        title= 'Github',
                                        class_name= 'dbc',
                                    ),
                                    dbc.AccordionItem(                                  # LinkedIn Item
                                        [
                                            html.A(html.I(class_name= 'p-2 ms-1 fa-brands fa-linkedin fa-xl', style= {'color': '#6184f4'}), href= "https://linkedin.com/in/_user", target= '_blank'),
                                            "  You can view my LinkedIn profile by using the link embedded in this icon,",
                                            html.P("or by clicking the icon in the header.", class_name= 'mx-5'),
                                        ],
                                        title= 'LinkedIn',
                                        class_name= 'dbc',
                                    )
                                ],
                                start_collapsed= True,
                                style= {'width': '50%'}
                            )
                        ),
                        html.Br(),
                    ],
                    shadow= 'xl',
                    p= 'lg',
                    radius= 'md',
                ),
                html.Br(),
            ],
            width= {'size': 7, 'padding': 2})
        ],
        justify= 'center')
    )
], fluid= True, style= {'background-color': '#ecf0f1'})
