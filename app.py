from flask import Flask, redirect
from flask import render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/game')
def game():
    with open('suggest.csv') as f:
        reader = csv.reader(f)
        keyword = [row for row in reader]
    return render_template('game.html',keyword=keyword[3][0])

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)