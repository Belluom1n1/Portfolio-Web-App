# + ------------------------------ +
# + Simple Navbar:                 +
# +   - styled with Bootstrap      +
# + ------------------------------ +

# + ---- imports ---- +
import dash
from dash import html, Input, Output, State
import dash_bootstrap_components as dbc
import dash_bootstrap_components.icons


# + ---- reactive sidebar ---- +
offcanvas = html.Div(
    [
        dbc.Button("Explore", id= 'open-offcanvas', n_clicks= 0),
        dbc.Offcanvas(
            dbc.ListGroup(
                [
                    dbc.ListGroupItem(page['name'], href= page['path'])
                    for page in dash.page_registry.values()
                    if page['module'] != 'pages.not_found_404'
                ]
            ),
            id= 'offcanvas',
            is_open= False,
        ),
    ],
    className= 'my-3'
)

# + ---- callbacks ---- +
@app.callback(
    Output('offcanvas', 'is_open'),
    Input('open-offcanvas', 'n_clicks'),
    [State('offcanvas', 'is_open')],
)
def toggle_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open
