from flask import Flask, render_template, request, redirect
from ytapi import com
from classifier import data

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/tone')
def contact():
    return render_template('tone.html')


@app.route('/getcom')
def getcom():
    return render_template('getcom.html', com)


@app.route('/classify')
def classify():
    return render_template('classify.html', data)




if __name__ == "__main__":
    app.run(debug=True, port=4356)
