# Learn Dash and SQL with Sakila!

This is a veyr basic dash app to display a web application showing a single non-interactive bar chart, based on a [Pandas](https://pandas.pydata.org/pandas-docs/stable/) dataframe, built from a query to the [Sakila samples DB](https://dev.mysql.com/doc/sakila/en/).

The purpose of this repository is entirely educational. Edit the query, change the layout, add callbacks, edit to your heart's content, and learn Python 🐍 and Dash!

## Quickstart

The code in this repository needs:

* A Sakila database **somewhere**, where it is is not important, but you _will_ need to tell the app where it is.
* The app to run: the app is a [Python](https://docs.python.org/3/) script which runs a [Dash](https://dash.plot.ly/) application, to serve a website showing a chart.

### How do I get that to work?

**Ensure Your DB is Running**

Here we use a DB run by docker, change around line 15 of `assignment/index.py` to point it to your DB.

You should have a recent version of Python 3 running, ideally Python 3.7 or higher. Ideally, create a [virtual environment](https://docs.python.org/3/tutorial/venv.html), otherwise you will be using your _system python_.

Install your dependencies into your virtual environment or your _system python_ using the command below.

    pip install requirements.txt

You will need to specify the location of the database in `assignment/index.py` around line 15 to 22.

Save it, then run your code using:

    python assignment/index.py
