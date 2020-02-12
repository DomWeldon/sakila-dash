"""Example Dash app querying Sakila."""
import dash
import dash_core_components as dcc
import dash_html_components as html
from sqlalchemy import create_engine
import pandas as pd


# 1. Where is the DB?
# You need to point this string at your DB, options:
# a) running python locally with docker on your mahcine for the DB
db_connection_str = "mysql+pymysql://root:sakila@0.0.0.0/sakila"
# b) DB is somewhere else entirely?
# db_connection_str = 'mysql+pymysql://root:sakila@random.internet/sakila'

# 2. Connect to that DB
db_connection = create_engine(db_connection_str)

# 3. Setup Dash
# Here we create the app, don;t worry about this for now
app = dash.Dash(__name__)

# 4. Write a query!
# ecrire ton query ici!!!
sql_query = """
    SELECT first_name, COUNT(*) AS c
    FROM actor
    GROUP BY first_name;"""
# N.B. - I've split my query over several lines here using triple quotes
# to make it more readable. Making code easy to read is good practice!


# 5. Run that query and make a Pandas DataFrame
# Here we are loading your data from our data base using the SQL query above
df = pd.read_sql(sql_query, con=db_connection)

# 6. Create a Dash LAyour
app.layout = html.Div(
    children=[
        # Titre
        html.H1("Mon Data"),
        # Graph
        dcc.Graph(
            id="example-graph",
            figure={
                "data": [
                    {
                        "x": df.first_name,
                        # This is related to your SQL query, but how?
                        "y": df.c,
                        "type": "bar",
                        # Change this to make the graph useful
                        "name": "Nombre des acteurs par leur prénom",
                    }
                ],
                # Find Dash's documentation to make this look even more
                # informative!
                "layout": {"title": ("Nombre des acteurs par leur prénom")},
            },
        ),
    ]
)

# 7, Run the app
if __name__ == "__main__":
    # When python sees the file
    # Running python locally?
    app.run_server(debug=True, host="localhost")
    # Running evrything in docker?
    # docker - if running locally, use "localhost" for host
    # app.run_server(debug=True, host="0.0.0.0")

# See your app at: http://localhost:8050
