from FlaskApp import app
from flask import request, redirect, url_for
from flask import render_template
import os, json
import requests

import pandas as pd
import plotly
import plotly.express as px

@app.route('/')
@app.route('/home')
def homePage():
    return render_template("home2.html", name = "Daniel")


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

@app.route("/tasks")
def tasks():
    return render_template("tasks.html")

@app.route("/tasks/subnetRequest" , methods = ['POST', 'GET'])
def subnetAPICall():
    ip = request.form['ip']
    getRequest = requests.get(f'http://localhost:5000/getSubnet/{ip}')
    print(getRequest.json())
    return render_template("tasks.html", subnet = getRequest.json()["subnet"])
    
# *********************************************************************************************
def getGraph(fig):
    fig.update_layout(paper_bgcolor="rgb(0,0,0,0)",
                      legend = dict(bgcolor = "rgb(252, 252, 252)"),
                      plot_bgcolor = 'white',
                      font_size=18)
    div = fig.to_html(full_html = False, default_width = '100%')

    return div
