from FlaskApp import app
from flask import render_template
import os, json

import pandas as pd
import plotly
import plotly.express as px

@app.route('/')
@app.route('/home')
def homePage():
    return render_template("home.html", name = "Daniel")


@app.route('/dataVisualization')
def dataVisualization():
    df = px.data.gapminder().query("year == 2007")
    fig = px.treemap(df, path=[px.Constant('world'), 'continent', 'country'], values='pop',
                    color='lifeExp', hover_data=['iso_alpha'],
                    color_continuous_scale='RdBu')
    # df.to_json("data.json")
    return render_template("treeVis.html",  name = "Username", graph = getGraph(fig))              



@app.route("/test")
def dataPage():
    items = [
    {'id': 1, 'name': 'José', 'age': '25', 'height': 1.78},
    {'id': 2, 'name': 'Luis', 'age': '26', 'height': 1.87},
    {'id': 3, 'name': 'Ángel', 'age': '25', 'height': 1.74}]
    return render_template("test.html",  name = "Username", items = items)

@app.route("/plot")
def plot():
    df = px.data.iris()
    fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                    size='petal_length', hover_data=['petal_width'])
    return render_template("plot.html",  name = "Username", graph = getGraph(fig))

# *********************************************************************************************

def getGraph(fig):
    fig.update_layout(paper_bgcolor="rgb(0,0,0,0)",
                      legend = dict(bgcolor = "rgb(252, 252, 252)"),
                      plot_bgcolor = 'white',
                      font_size=18)
    div = fig.to_html(full_html = False, default_width = '100%')

    return div
