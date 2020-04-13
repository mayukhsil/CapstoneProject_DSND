from flask import Flask
from flask import render_template, request, jsonify
import plotly
import pandas as pd
import re
import os
from sqlalchemy import create_engine

url_regex = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"

app = Flask(__name__)




@app.route('/')
#this route will show the menu with three options
@app.route('/index')
def index():
    pass
    
#this route will direct to selection of stocks 
@app.route('/selection')
def selection():
    pass

#this route will select the model
@app.route('/model')
def model():
    pass

#this route will provide the final prediction
@app.route('/prediction')
def prediction():
    pass


def main():
    app.run(host='0.0.0.0', debug=True, port=8000)


if __name__ == '__main__':
    main()