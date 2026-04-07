## End to End ML Project - Student Performance Prediction


---

🎯 End-to-End Machine Learning Project

📊 Student Performance Prediction


---

🚀 Overview

This project is a production-ready, end-to-end machine learning pipeline designed to predict student performance based on demographic and academic features.

It goes beyond simple model training — this system is structured like a real-world ML application, with modular components, logging, exception handling, and pipeline automation.


---

🧠 Problem Statement

Educational institutions often struggle to identify students at risk of poor performance early enough.

This project aims to:

Predict student scores using key features

Enable early intervention strategies

Demonstrate a scalable ML system design



---

🏗️ Project Architecture

ML Projects
│
├── artifacts/               # Saved outputs (model, data splits, preprocessor)
├── notebooks/              # EDA & experimentation
├── src/
│   ├── components/         # Core ML pipeline components
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │
│   ├── pipeline/           # Training & prediction pipelines
│   │   ├── train_pipeline.py
│   │   ├── predict_pipeline.py
│   │
│   ├── utils.py            # Utility functions
│   ├── logger.py           # Logging system
│   ├── exception.py        # Custom exception handling
│
├── logs/                   # Execution logs
├── requirements.txt        # Dependencies
├── setup.py                # Package setup
└── README.md               # Project documentation


---

⚙️ Key Features

✅ Modular and scalable codebase
✅ Automated data ingestion and preprocessing
✅ Model training with multiple algorithms
✅ Hyperparameter tuning
✅ Pipeline-based architecture
✅ Custom logging and exception handling
✅ Serialized model and preprocessor (.pkl)


---

🔄 ML Pipeline Workflow

1. Data Ingestion

Reads raw dataset

Splits into train and test sets

Stores artifacts


2. Data Transformation

Handles missing values

Encodes categorical variables

Scales numerical features

Saves preprocessing pipeline


3. Model Training

Trains multiple models:

Linear Regression

Decision Trees / Random Forest

KNN

XGBoost

CatBoost


Performs hyperparameter tuning

Selects best-performing model


4. Prediction Pipeline

Loads trained model + preprocessor

Accepts new input data

Returns predictions



---

🧪 Models Used

Linear Regression

K-Nearest Neighbors

Random Forest

XGBoost

CatBoost

AdaBoost


(Because one model is never enough — real ML is about comparison, not guesswork.)


---

📦 Installation

Clone the repository:

git clone https://github.com/habeeb-ml/student_performance_prediction-.git
cd student_performance_prediction-

Create virtual environment:

python -m venv venv
venv\Scripts\activate   # Windows

Install dependencies:

pip install -r requirements.txt


---

▶️ Usage

Run Training Pipeline

python src/pipeline/train_pipeline.py

Run Prediction Pipeline

python src/pipeline/predict_pipeline.py


---

📊 Dataset

The dataset contains features such as:

Gender

Parental level of education

Lunch type

Test preparation course

Reading & writing scores


Target:

Math score (or overall performance)



---

📁 Artifacts Generated

After running the pipeline:

artifacts/
├── model.pkl
├── preprocessor.pkl
├── train.csv
├── test.csv
└── raw.csv


---

🧾 Logging & Exception Handling

Custom logging implemented via logger.py

Structured logs stored in /logs

Centralized error handling via exception.py


(Because debugging without logs is just guessing with confidence.)


---

🔮 Future Improvements

Deploy as a web app (Flask / FastAPI)

Add model monitoring

Integrate CI/CD pipeline

Use real-world educational datasets

Add feature importance visualization



---

👨‍💻 Author

Habeeb

Aspiring ML Engineer & Medical Student

Interested in AI in Healthcare & Clinical Informatics



---

⭐ Final Note

This project is not just about predicting scores —
it’s about building systems that can scale, adapt, and be deployed in real life.


---
