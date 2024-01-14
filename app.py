from selenium import webdriver
from selenium.webdriver.common.by import By
from flask import Flask, render_template, redirect, request
import csv
import os
from scrap import selenium_function

app = Flask(__name__)
PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))



# Set up the WebDriver (in this example, using Chrome)




# @app.route("/")
# def apart_link():
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_selenium', methods=['POST', 'GET'])
def run_selenium():
    apart_id = request.args['sortId']
    print(apart_id, 'see what is apart')
    selenium_function(apart_id)
    return redirect('/')

def create_event(apart_link):
    
    

        
        
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)