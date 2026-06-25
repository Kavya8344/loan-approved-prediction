# Loan Approval Prediction System

A Machine Learning powered web application that predicts whether a loan application is likely to be approved based on applicant financial information.

Built using **Python, Flask, Scikit-Learn, HTML, CSS, and Bootstrap**.

---

## Project Overview

The Loan Approval Prediction System helps evaluate loan eligibility using Machine Learning algorithms trained on applicant financial data.

The system analyzes:

* Income
* Credit Score
* Loan Amount
* Years Employed

and predicts whether the loan application is:

* Approved
* Rejected

The application also maintains a prediction history for previously submitted applications.

---

## Features

* Real-Time Loan Approval Prediction
* Machine Learning Integration
* Prediction History Tracking
* Responsive User Interface
* Flask Web Application
* Mobile-Friendly Design
* Secure Local Processing

---

## Technologies Used

### Backend

* Python
* Flask
* Joblib

### Machine Learning

* Scikit-Learn
* Pandas
* NumPy

### Frontend

* HTML5
* CSS3
* Bootstrap 5

---

## Dataset Information

The dataset contains financial and employment-related information used to predict loan approval status.

### Features Used

| Feature        | Description             |
| -------------- | ----------------------- |
| Income         | Applicant Annual Income |
| Credit Score   | Applicant Credit Rating |
| Loan Amount    | Requested Loan Amount   |
| Years Employed | Employment Experience   |
| Loan Approved  | Target Variable         |

### Dataset Size

* Total Records: **2000**
* Features Used: **4**
* Target Variable: **Loan Approved**

---

## Machine Learning Models Evaluated

### Logistic Regression

| Metric         | Score  |
| -------------- | ------ |
| Test Accuracy  | 88.25% |
| Train Accuracy | 91.25% |

### Support Vector Machine (SVM)

| Metric         | Score  |
| -------------- | ------ |
| Test Accuracy  | 59.75% |
| Train Accuracy | 63.00% |

### Decision Tree Classifier

| Metric         | Score   |
| -------------- | ------- |
| Test Accuracy  | 95.75%  |
| Train Accuracy | 100.00% |

### Tuned Decision Tree Classifier

| Metric         | Score  |
| -------------- | ------ |
| Test Accuracy  | 93.75% |
| Train Accuracy | 97.94% |

### Random Forest Classifier

| Metric         | Score  |
| -------------- | ------ |
| Test Accuracy  | 95.50% |
| Train Accuracy | 98.38% |

---

## Final Model Used

The deployed model is a **Random Forest Classifier** trained using:

* Income
* Credit Score
* Loan Amount
* Years Employed

### Final Model Performance

| Metric         | Score  |
| -------------- | ------ |
| Test Accuracy  | 95.50% |
| Train Accuracy | 98.38% |

This model was selected as the best-performing model after comparing multiple machine learning algorithms.

---

## Project Structure

```text
Loan-Approval-Prediction/
│
├── app.py
├── history.json
├── requirements.txt
│
├── model/
│   └── best_model.lb
│
├── templates/
│   ├── index.html
│   ├── project.html
│   ├── history.html
│   ├── about.html
│   └── contact.html
│
├── static/
│   └── loan.png
│
└── loan_approval.csv
```

---

## Required Packages

Install all dependencies using:

```bash
pip install -r requirements.txt
```

### requirements.txt

```text
Flask
pandas
numpy
scikit-learn
joblib
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Kavya8344/loan-approved-prediction
```

### Navigate to Project Directory

```bash
cd Loan-Approval-Prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

---

## Open in Browser

```text
http://127.0.0.1:5000
```

---

## Developer

### Kavya Sharma

Machine Learning & Flask Developer

---

## License

This project is developed for educational and learning purposes.
