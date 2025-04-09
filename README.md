# BrightPath Academy: *Student Performance Prediction*

This project focuses on identifying and supporting at-risk students at **BrightPath Academy** using machine learning techniques. By analyzing data such as study habits, parental support, extracurricular activities, and more, we aim to predict a student’s academic performance class (GradeClass) and provide actionable insights to improve interventions.


## Problem Statement
BrightPath Academy aims to proactively assist students by predicting their academic performance and identifying those at risk. This model helps classify students into performance categories based on multiple academic and demographic factors


## Technologies Used

- Python (Pandas, NumPy, Seaborn, Matplotlib)
- Scikit-learn
- Dash
- Render


## Data Preprocessing

- Filled missing **numerical values** with **median** (binary columns with **mode**).
- Filled missing **categorical values** with **mode**.
- Removed GPA outliers using IQR method.

