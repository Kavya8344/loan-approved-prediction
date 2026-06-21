# Loan Approval Prediction - Data Preprocessing & EDA

## Project Overview

This project focuses on data cleaning, preprocessing, and exploratory data analysis (EDA) for a loan approval dataset.

The objective is to prepare the dataset for machine learning models that can predict whether a loan application will be approved based on applicant information such as income, credit score, employment history, and loan amount.

---

## Dataset Features

* Income
* Credit Score
* Loan Amount
* Years Employed
* Points
* Loan Approved (Target Variable)

### Removed Features

The following columns were removed during preprocessing:

* Name
* City

These columns were treated as non-informative identifiers and were not expected to contribute significantly to loan approval prediction.

---

## Data Preprocessing

The following preprocessing steps were performed:

* Data inspection using Pandas
* Missing value analysis
* Duplicate record detection
* Feature selection
* Target variable preparation
* Data quality checks

---

## Exploratory Data Analysis (EDA)

Visualizations included:

* Histograms
* Boxplots
* Scatterplots
* Loan approval distribution analysis
* Correlation analysis

The visualizations help identify:

* Feature distributions
* Potential outliers
* Relationships between variables
* Factors associated with loan approval

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook

---

## Project Structure

```text
loan-approval-prediction/
│
├── loan.ipynb
├── loan_approval.csv
├── README.md
```

---

## Feature and Target Separation

```python
X = df.drop('loan_approved', axis=1)
y = df['loan_approved']
```

---

## Future Improvements

* Feature scaling
* Train-test split
* Logistic Regression


---

## Author

Kavya Sharma
