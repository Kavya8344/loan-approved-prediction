from flask import Flask, request, render_template, flash, redirect, url_for
import joblib
import json

app = Flask(__name__)

model=joblib.load("model/lr.lb")

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/project',methods=['GET','POST'])
def predict():
    if request.method=="POST":
        data=request.get_json()
    
    return render_template('project.html')

if __name__ == "__main__":
    app.run()