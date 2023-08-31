import os
import joblib
import pandas as pd
from flask import Flask, request
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)


# Load the trained pipeline
pipeline_filename = os.path.join('trained_model', 'stroke_prediction_pipeline.pkl')
pipeline = joblib.load(pipeline_filename)

@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict stroke probability for new data
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: PredictInput
          properties:
            age:
              type: number
              description: Age of the person
            hypertension:
              type: number
              description: Hypertension (0 for No, 1 for Yes)
            heart_disease:
              type: number
              description: Heart disease (0 for No, 1 for Yes)
            avg_glucose_level:
              type: number
              description: Average glucose level
            bmi:
              type: number
              description: Body mass index (BMI)
            gender:
              type: string
              description: Gender (Male, Female, Other)
            ever_married:
              type: string
              description: Marital status (Yes, No)
            work_type:
              type: string
              description: Type of work (Private, Self-employed, etc.)
            Residence_type:
              type: string
              description: Residence type (Urban, Rural)
            smoking_status:
              type: string
              description: Smoking status (formerly smoked, never smoked, etc.)
    responses:
      200:
        description: Successfully predicted stroke probability
        schema:
          id: PredictOutput
          properties:
            prediction:
              type: number
              description: Predicted stroke probability (0 for No, 1 for Yes)
    """
    data = request.get_json()

    # Convert data to a DataFrame
    new_data = pd.DataFrame(data, index=[0])

    # Make predictions using the pipeline
    prediction = pipeline.predict(new_data)

    pred_mapping = {
        0: 'No-Stroke',
        1: 'Stroke'
    }

    predicted_class = pred_mapping[prediction[0]]

    return f"Model prediction is {predicted_class}"

if __name__ == '__main__':
    app.run(debug=True)