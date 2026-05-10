🚀 Loan Prediction using Random Forest (Bagging Ensemble)


📌 Project Overview

This project is a Loan Approval Prediction System built using Machine Learning (Random Forest - Bagging technique).
It predicts whether a loan application will be approved or rejected based on applicant details like income, education, employment, property area, etc.

The model is trained using real-world structured data and improved using hyperparameter tuning (GridSearchCV).

🧠 What I Learned / Implemented
Data cleaning and preprocessing
Handling missing values
Label Encoding & One-Hot Encoding
Train-test splitting
Decision Tree vs Random Forest comparison
Bagging concept using Random Forest
Hyperparameter tuning using GridSearchCV
Model evaluation (F1-score, Accuracy, Precision, Recall)
Model saving using joblib
📊 Models Used
🌳 Decision Tree Classifier (baseline)
🌲 Random Forest Classifier (Bagging)
🔧 Tuned Random Forest (final model)
🏆 Final Model Performance

After tuning, Random Forest performed best:

Accuracy: ~80%
F1 Score: ~0.86

👉 Final model selected: Random Forest (Tuned)

⚙️ Tech Stack
Python 🐍
Pandas & NumPy
Scikit-learn
Matplotlib
Joblib
Streamlit (for UI)
🧹 Data Preprocessing Steps
Removed unnecessary columns (Loan_ID, Gender)
Handled missing values
Converted categorical values:
Label Encoding → Married, Education, Self_Employed
One-Hot Encoding → Property_Area
Converted 3+ dependents → numeric 3
Split dataset into training and testing sets
🧪 Model Training Workflow
Load dataset
Clean and preprocess data
Encode categorical variables
Train Decision Tree (baseline)
Train Random Forest
Tune hyperparameters using GridSearchCV
Select best model
Train final model on full dataset
Save model using joblib
💾 Model Saving
import joblib
joblib.dump(final_model, "loan_model.pkl")

🌐 Streamlit Web App

A simple web interface is built using Streamlit where users can input:

Income
Education
Marital status
Property area
Loan amount, etc.

👉 The model predicts:

✅ Loan Approved
❌ Loan Rejected
▶️ How to Run Locally
1. Clone repo
git clone https://github.com/your-username/loan-prediction-rf.git
cd loan-prediction-rf

2. Install dependencies
pip install -r requirements.txt

3. Run Streamlit app
streamlit run app.py

📦 Requirements
pandas
numpy
scikit-learn
matplotlib
streamlit
joblib

☁️ Deploy on GitHub / Streamlit Cloud

Yes, you can deploy it on GitHub + Streamlit Cloud:

Steps:
Push code to GitHub
Go to https://streamlit.io/cloud
Connect GitHub repo
Select app.py
Click Deploy 🚀
📌 Future Improvements
Add XGBoost / LightGBM comparison
Improve accuracy with feature engineering
Add SHAP explainability
Deploy as full ML web app with database
Add real-time input validation


👨‍💻 Author

Bhuwan

dataset source: https://www.kaggle.com/datasets/altruistdelhite04/loan-prediction-problem-dataset