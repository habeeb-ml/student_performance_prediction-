from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler

from src.pipeline import predict_pipeline
from src.pipeline.predict_pipeline import CustomData,PredictPipeline


application = Flask(__name__)
app = application

## Route for a home page
@app.route("/")
def home():
    return render_template('home.html')

@app.route('/predict_datapoint',methods=['GET','POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        data=CustomData(
            gender=request.form.get('gender') or "",
            race_ethnicity=request.form.get('ethnicity') or "",
            parental_level_of_education=request.form.get('parental_level_of_education') or "",
            lunch=request.form.get('lunch') or "",
            test_preparation_course=request.form.get('test_preparation_course') or "",
            reading_score=float(request.form.get('reading_score') or 0.0),
            writing_score=float(request.form.get('writing_score') or 0.0)
        )

        pred_df=data.get_data_as_data_frame()
        print(pred_df)

        predict_pipeline=PredictPipeline()
        results=predict_pipeline.predict(pred_df)
        results=round(results[0])
        return render_template('result.html',results=results)
    

if __name__=='__main__':
    app.run(host='0.0.0.0') # Remember to always remove "debug = True" before deployment
    
        


    