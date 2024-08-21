from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load the saved model and scaler
model = joblib.load('heart_disease_model.pkl')
scaler = joblib.load('scaler.pkl')

# Load dataset (for column names)
heart_data = pd.read_csv('data.csv')
X = heart_data.drop(columns='target')

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle form submission
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get form data
            form_data = request.form
            age = float(form_data['age'])
            gender = int(form_data['gender'])
            chest_pain = int(form_data['chest_pain'])
            blood_pressure = float(form_data['blood_pressure'])
            cholesterol = float(form_data['cholesterol'])
            blood_sugar = int(form_data['blood_sugar'])
            electrocardiographic = int(form_data['electrocardiographic'])
            heart_rate = float(form_data['heart_rate'])
            exercise_angina = int(form_data['exercise_angina'])
            oldpeak = float(form_data['oldpeak'])
            slope = int(form_data['slope'])
            ca = int(form_data['ca'])
            thal = int(form_data['thal'])
            
            # Convert to DataFrame for prediction
            input_data = pd.DataFrame([[age, gender, chest_pain, blood_pressure, cholesterol, blood_sugar, 
                                        electrocardiographic, heart_rate, exercise_angina, oldpeak, slope, ca, thal]], 
                                        columns=X.columns)

            # Scale input data
            input_data_scaled = scaler.transform(input_data)
            
            # Predict
            prediction = model.predict(input_data_scaled)
            
            # Render result page with prediction
            result = 'The Person Does have a Heart Disease' if prediction[0] == 0 else 'The Person Does not have a Heart Disease'
            return render_template('result.html', prediction=result)

        except ValueError as e:
            return render_template('index.html', error="Invalid input. Please enter valid numbers.")
            
if __name__ == '__main__':
    app.run(debug=True)
