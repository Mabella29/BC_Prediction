import numpy as np
import pickle

with open('scaler.pkl', 'rb') as scaler_file:
    loaded_scaler = pickle.load(scaler_file)



new_data = np.array([[15.5, 16.2, 120.5, 1000.0, 0.115, 0.230, 0.250, 0.160, 0.120,
                      0.127, 0.208, 132.0, 1030.0, 0.135, 0.260, 0.320, 0.250, 0.220,
                      0.190, 0.105, 0.460, 0.155, 0.205, 0.320, 0.480, 0.210, 0.210,
                      130.0, 118.0, 141.0]])




with open('scaler.pkl', 'rb') as scaler_file:
    loaded_scaler = pickle.load(scaler_file)


new_data_scaled = loaded_scaler.transform(new_data)


with open('final_logistic_regression_model.pkl', 'rb') as model_file:
    loaded_model = pickle.load(model_file)

def predict(new_data):
    prediction = loaded_model.predict(new_data_scaled)
    print("Prediction:", prediction)


    y_pred = loaded_model.predict_proba(new_data_scaled)[0,1]
    return y_pred




