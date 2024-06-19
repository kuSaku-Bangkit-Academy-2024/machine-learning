from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd
import pickle
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def predict_expenses(input_data, model_path='model.h5', scaler_path='scaler.pkl'):
    """
    Predicts expenses based on the input income using a pre-trained model.

    Parameters:
    input_data (pd.DataFrame): DataFrame containing the input data with a column named 'Income'.
    model_path (str): Path to the saved model.
    scaler_path (str): Path to the saved scaler (optional).

    Returns:
    pd.DataFrame: DataFrame containing the predicted expenses.
    """

    model = load_model(model_path)

    with open(scaler_path, 'rb') as file:
        scaler = pickle.load(file)
    
    normalized_income = scaler.transform(input_data[['Income']])
    
    predictions = model.predict(normalized_income)
    
    features = ['Food', 'Household', 'Education', 'Health', 'Transportation', 'Apparel', 'Social Life', 'Entertainment', 'Other']
    
    predictions_df = pd.DataFrame(predictions, columns=features)
    
    result_df = input_data.copy()
    result_df[features] = predictions_df
    
    return result_df

if __name__ == '__main__':

    input_data = pd.DataFrame({
        'Income': [1000000, 1700000, 1800000, 2600000, 5500000]
    })

    predicted_expenses = predict_expenses(input_data)
    print(predicted_expenses)