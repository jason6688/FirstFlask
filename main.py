#-*-  coding:utf-8 -*-
from flask import Flask
from flask import render_template

from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)

@app.route('/')
def hello():
    return '<h1>Hello Jason~</h1>';

@app.route('/home')
def home():
    return render_template('home.html')



if __name__ == '__main__':
    app.run()