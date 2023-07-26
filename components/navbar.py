# + ------------------------------ +
# + Simple Navbar:                 +
# +   - styled with Bootstrap      +
# + ------------------------------ +

# + ---- imports ---- +
import dash
from dash import html
import dash_bootstrap_components as dbc
import dash_bootstrap_components.icons
import dash_extensions as de

BRAND = '/assets/compassMech.ico'
myBrand = html.Div(
    [
        html.Img(src= '/assets/compassMech.ico', width= '50', height= '50', alt= '', className= 'img-fluid m-0 p-0 inline-block'),
        ' ',
    ],
    className= 'ms-2'
)

# + ---- navbar ---- +
def navbar():
    navbar = dbc.NavbarSimple(
        children= [
            dbc.NavItem(
                dbc.NavLink(
                    [
                        html.I(className= 'p-2 fa-brands fa-github fa-xl'),
                        ' ',
                    ],
                    href= 'https://github.com/Belluom1n1',
                    external_link= True,
                    target= '_blank',
                )
            ),
            dbc.NavItem(
                dbc.NavLink(
                    [
                        html.I(className= 'p-2 fa-brands fa-linkedin fa-xl'),
                        ' ',
                    ],
                    href= 'https://linkedin/in/bbelluom1n1',
                    external_link= True,
                    target= '_blank',
                )
            ),
            dbc.DropdownMenu(
                [
                    dbc.DropdownMenuItem("Naigation", header= True),
                    dbc.DropdownMenuItem(divider= True),
                    dbc.DropdownMenuItem("Home", href= '/'),
                    dbc.DropdownMenuItem("Projects", href= '/Projects'),
                    dbc.DropdownMenuItem("Contact", href= '/Contact'),
                ],
                nav= True,
                in_navbar= True,
                label= 'Menu',
                align_end= True,
                class_name= 'me-2'
            )
        ],
        brand= myBrand,
        brand_href= '/',
        color= 'primary',
        dark= True,
        fluid= True,
        className= 'mb-0',
    )
    return navbar
