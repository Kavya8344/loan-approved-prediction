from flask import Flask, request, render_template
import joblib
import pandas as pd
import json

app = Flask(__name__)

# Load trained model
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


@app.route('/project', methods=['GET', 'POST'])
def predict():

    if request.method == 'POST':

        try:
            income = float(request.form['income'])
            credit_score = float(request.form['credit_score'])
            loan_amount = float(request.form['loan_amount'])
            years_employed = float(request.form['years_employed'])

            # Input Validation
            if income <= 0:
                return render_template(
                    "project.html",
                    prediction="Invalid Income"
                )

            if loan_amount <= 0:
                return render_template(
                    "project.html",
                    prediction="Invalid Loan Amount"
                )

            if credit_score < 300 or credit_score > 850:
                return render_template(
                    "project.html",
                    prediction="Credit Score must be between 300 and 850"
                )

            if years_employed < 0 or years_employed > 40:
                return render_template(
                    "project.html",
                    prediction="Years Employed must be between 0 and 40"
                )

            # Prevent unrealistic values
            if loan_amount > income * 2:
                return render_template(
                    "project.html",
                    prediction="Loan Amount Too High"
                )

            # Create DataFrame for prediction
            data = pd.DataFrame({
                "income": [income],
                "credit_score": [credit_score],
                "loan_amount": [loan_amount],
                "years_employed": [years_employed]
            })

            prediction = model.predict(data)[0]

            result = "Approved" if prediction else "Rejected"

            # Load prediction history
            with open("history.json", "r") as f:
                history = json.load(f)

            # Add new record
            history.append({
                "income": income,
                "credit_score": credit_score,
                "loan_amount": loan_amount,
                "years_employed": years_employed,
                "result": result
            })

            # Save history
            with open("history.json", "w") as f:
                json.dump(history, f, indent=4)

            return render_template(
                "project.html",
                prediction=result
            )

        except ValueError:
            return render_template(
                "project.html",
                prediction="Please enter valid numeric values"
            )

    return render_template("project.html")


if __name__ == "__main__":
    app.run(debug=True)