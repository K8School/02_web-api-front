from flask import Flask
from flask import render_template
import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()  # take environment variables from .env.

# Code of your application, which uses environment variables (e.g. from `os.environ` or
# `os.getenv`) as if they came from the actual environment.


app = Flask(__name__)

@app.route('/')
def hello():
    #return 'Hello, World! This is v4!'
    return render_template('index.html', msg='Hello World!', title="Hello from a Docker Container!")

@app.route('/hello/<name>')
def hello_you(name):
    #return 'Hello, World! This is v4!'
    return render_template('index.html', msg=f"Hello {name}!", title="Hello from a Docker Container!")

@app.route('/microservices')
def microservice():
    quote_url = os.environ.get("API_QUOTES")
    r = requests.get(quote_url + "/quote_sentiment").text  
    quote = json.loads(r)["phrase"]
    sentiment = json.loads(r)["sentiment"]
    return render_template('frame.html', quote=quote, sentiment=sentiment, time="now")


@app.route('/universe')
def universe():
    return "42"

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    sum = num1 + num2
    message = f"{num1} + {num2} = {sum}"
    return render_template('index.html', msg=message, title="Hello from a Docker Container!")


@app.route('/txtadd/<int:num1>/<int:num2>')
def txtadd(num1, num2):
    sum = num1 + num2
    return f"{sum}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
