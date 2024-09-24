from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the serialized model using a relative path
model = joblib.load('../notebooks/rossmann_model_2024-09-24_14-35-22.pkl')

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Sales Prediction API! Use the /predict endpoint to make predictions."

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    
    # Define all required features
    required_features = [
        'CompetitionDistance', 'Promo', 'DayOfWeek', 'Year', 'Month', 'StoreType', 
        'Assortment', 'Store', 'CompetitionOpenSinceMonth', 'CompetitionOpenSinceYear',
        'Promo2', 'Promo2SinceWeek', 'Promo2SinceYear', 'PromoInterval', 'HolidayFlag',
        'SchoolHoliday', 'StateHoliday', 'IsWeekend', 'Day', 'WeekOfYear', 'Customers',
        'StoreOpen', 'IsHoliday', 'Sales'
    ]
    
    # Check if all features are present
    for feature in required_features:
        if feature not in data:
            return jsonify({"error": f"Missing required feature: {feature}"}), 400
    
    # Extract features from the request in the right order
    features = np.array([data[feature] for feature in required_features])
    
    # Reshape input for the model
    features = features.reshape(1, -1)
    
    # Make prediction
    prediction = model.predict(features)
    return jsonify({'predicted_sales': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)

