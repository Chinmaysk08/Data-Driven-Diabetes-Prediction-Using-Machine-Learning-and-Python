<p align="center">
  <img src="assets/github-banner.png" alt="Diabetes Prediction System Banner" width="100%">
</p>
#  Diabetes Prediction using Machine Learning

A Machine Learning project that predicts whether a person is diabetic or non-diabetic based on medical diagnostic measurements using the **Support Vector Machine (SVM)** algorithm.
## 🚀 Live Demo

🌐 https://diabetes-prediction-chinmay.streamlit.app/

## 📌 Project Overview

Diabetes is one of the most common chronic diseases worldwide. Early prediction can help individuals seek medical attention before serious complications occur.

This project implements a complete Machine Learning pipeline using Python and Scikit-learn to classify patients based on various medical features from the Pima Indians Diabetes Dataset.

---

##  Features

- Data preprocessing
- Exploratory Data Analysis (EDA)
- Feature standardization using StandardScaler
- Train-Test Split
- Support Vector Machine (SVM) Classification
- Model Evaluation
- Prediction System for New Patient Data

---

##  Dataset

Dataset Used:
- **Pima Indians Diabetes Dataset**

### Features

| Feature | Description |
|---------|-------------|
| Pregnancies | Number of pregnancies |
| Glucose | Plasma glucose concentration |
| BloodPressure | Diastolic blood pressure |
| SkinThickness | Triceps skin fold thickness |
| Insulin | 2-Hour serum insulin |
| BMI | Body Mass Index |
| DiabetesPedigreeFunction | Diabetes pedigree function |
| Age | Age of patient |

### Target Variable

| Value | Meaning |
|------|---------|
| 0 | Non-Diabetic |
| 1 | Diabetic |

---

##  Technologies Used

- Python
- Google Colab
- NumPy
- Pandas
- Scikit-learn
- Matplotlib

---

##  Machine Learning Algorithm

**Support Vector Machine (SVM)**

Kernel Used:

- Linear Kernel

Why SVM?

- Performs well on small and medium-sized datasets
- Effective for binary classification problems
- Good generalization capability

---

##  Workflow

```
Load Dataset
        ↓
Data Analysis
        ↓
Split Features & Labels
        ↓
Feature Scaling
        ↓
Train-Test Split
        ↓
Train SVM Model
        ↓
Evaluate Model
        ↓
Predict New Patient
```

---

##  Project Structure

```
Diabetes-Prediction/
│
├── diabetes_prediction.ipynb
├── diabetes.csv
├── README.md
├── requirements.txt
└── images/
```

---

##  Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Diabetes-Prediction.git
```

Move into the project directory

```bash
cd Diabetes-Prediction
```

Install required libraries

```bash
pip install -r requirements.txt
```

---

##  Running the Project

Open the notebook using:

- Google Colab
- Jupyter Notebook

Run all cells sequentially.

---

##  Sample Prediction

Example Input

```python
(5,166,72,19,175,25.8,0.587,51)
```

Output

```
The person is diabetic.
```

---

##  Model Evaluation

Evaluation Metric:

- Accuracy Score

The model is trained using an 80:20 train-test split and evaluated on unseen test data.

---

## Libraries Used

```python
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
```

---

##  Future Improvements

- Logistic Regression comparison
- Random Forest Classifier
- XGBoost
- Hyperparameter Tuning
- Streamlit Web Application
- Flask API
- Docker Deployment

---

## Screenshots

Add screenshots of:

- Dataset Preview
- Correlation Matrix (Optional)
- Model Prediction Output
- Google Colab Notebook

---

##Contributing

Contributions are welcome.

Fork the repository and create a pull request with your improvements.

---

## Author

Chinmay S Kashikar 

Electronics & Communication Engineering(Student)

Aspiring Data Analyst | Python | SQL | Machine Learning

GitHub: https://github.com/Chinmaysk08

LinkedIn: https://www.linkedin.com/in/chinmay-kashikar-23707539b

---

## Support

If you found this project useful, please consider giving it a ⭐ on GitHub.
