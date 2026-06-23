from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

model = joblib.load("model/best_model.lb")

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

    with open("history.json", "r") as f:
        history_data = json.load(f)

    return render_template(
        "history.html",
        historical_data=history_data
    )

import json

@app.route('/project', methods=['GET','POST'])
def predict():

    if request.method == 'POST':

        income = float(request.form['income'])
        credit_score = float(request.form['credit_score'])
        loan_amount = float(request.form['loan_amount'])
        years_employed = float(request.form['years_employed'])

        data = [[
            income,
            credit_score,
            loan_amount,
            years_employed
        ]]

        prediction = model.predict(data)[0]

        result = "Approved" if prediction else "Rejected"

        # Load old history
        with open("history.json", "r") as f:
            history = json.load(f)

        # Add new prediction
        history.append({
            "income": income,
            "credit_score": credit_score,
            "loan_amount": loan_amount,
            "years_employed": years_employed,
            "result": result
        })

        # Save
        with open("history.json", "w") as f:
            json.dump(history, f, indent=4)

        return render_template(
            "project.html",
            prediction=result
        )

    return render_template("project.html")

if __name__ == "__main__":
    app.run(debug=True)