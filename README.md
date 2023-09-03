# Deploying Machine Learning Models on Google Cloud Platform: From Development to Production with Flask, Docker, and Kubernetes
### A beginner-friendly guide to train and deploy a stroke prediction machine learning model on Google Kubernetes Engine

![](https://github.com/Shahrullo/stroke-prediction-kubernetes/blob/main/images/mediumPage2.png)

## Objective
Develop and deploy a machine learning model for predicting strokes. This model will be trained on relevant medical data to accurately identify individuals who might be at risk of experiencing a stroke. The goal is to create a robust and accurate prediction tool that can assist medical professionals in assessing stroke risk factors and making informed decisions about patient care. The deployed model should be integrated into existing healthcare systems to provide timely insights and support preventive measures, ultimately contributing to improved patient outcomes and healthcare management.

## How to run locally
Follow these steps to set up and run the project on your local machine:
1. First, create a virtual environment using Conda or any other tool of your choice. We recommend Conda for this project:\
`conda create -n stroke_kubernetes python==3.10`
2. Activate the newly created environment and install the required dependencies:\
`conda activate stroke_kubernetes`\
`pip install -r requirements.txt`
3. Make sure you have the necessary data downloaded and place it in the data folder in the project's root directory. [Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)
4. To train the model, execute the following command. This will run a minimalistic decision tree model and save the trained weights in the trained_model folder.\
`python ml_pipeline.py`
5. Start the local web service based on Flask by running the following command\
`python app.py`\
You can then access the API documentation by navigating to `http://127.0.0.1:5000/apidocs` in your browser.
