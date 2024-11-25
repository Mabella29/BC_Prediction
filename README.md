# BC_Prediction

Breast Cancer Prediction Model
This project uses a Logistic Regression model to predict whether a breast cancer tumor is malignant or benign based on a set of features extracted from breast cancer diagnostic data. The model has been trained on a dataset containing various features related to the tumor’s physical characteristics, such as radius, texture, area, perimeter, and others.

# Streamlit cloud link
https://testml-9wuu92gudcune6ef6zjlyx.streamlit.app/

## Model Overview
The model is designed to classify breast cancer tumors into two categories:

1. Malignant: Cancerous tumors
2. Benign: Non-cancerous tumors

# Key Features
Mean Radius: The average distance from the center to the perimeter of the tumor.

Mean Texture: Standard deviation of gray-scale values in the image. It measures the contrast or texture of the tumor.

Mean Perimeter: The average length of the tumor’s perimeter.

Mean Area: The average area covered by the tumor.

Mean Smoothness: Local variation in radius lengths, indicating how smooth the tumor’s contour is.

Compactness: A measure of the tumor's shape, calculated as the perimeter squared divided by the area minus 1.0. Higher compactness suggests a more circular, compact tumor.

Concavity: A measure of the severity of concave portions in the tumor's contour. Tumors with higher concavity are more likely to be malignant.

Concave Points: The number of concave portions in the tumor's contour. More concave points are often associated with malignant tumors.

Symmetry: A measure of how symmetric the tumor is. Malignant tumors tend to be less symmetric compared to benign ones.

Fractal Dimension: A measure of the tumor’s complexity or irregularity. It captures the detail and texture of the tumor boundary and is related to the fractal pattern it forms.

These features are crucial for making predictions about whether a tumor is benign or malignant. Each of these measurements is derived from the image of the tumor, and together they provide important information for the model to classify the tumor accurately.

## How it works
Model Training: A Logistic Regression model is trained using the dataset with labeled examples of malignant and benign tumors.
Data Scaling: The features are scaled to ensure that the model performs optimally, accounting for differences in the range of feature values.
Prediction: Once the model is trained, it can predict the class (malignant or benign) of new tumor data based on the input features. Additionally, it provides a probability of the tumor being malignant.
How to Use the Model
You can interact with this model through a Streamlit web application. Enter the values for the features of the tumor, and the model will predict whether the tumor is malignant or benign. The model also provides the probability that the tumor is malignant.

## Deployment
This model is deployed as a web application using Streamlit, and it can be accessed locally or hosted on platforms such as Streamlit Cloud or Heroku. The application provides a user-friendly interface where users can input feature values and receive predictions.

## Requirements
Python 3.11
streamlit
flask
pickle
numpy
scikit-learn version 1.5.2
pandas

## Run the Application
To run the Streamlit app locally, follow these steps:

1. Clone the repository.

2. Install dependencies:



Run the Streamlit app:


streamlit run streamlitApp.py
The application will be accessible at http://localhost:8501 in your web browser.



