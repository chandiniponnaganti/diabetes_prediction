# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 17:14:03 2025

@author: chandini
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open(r"C:/Users/phema/OneDrive/Desktop/ml/trained_model.sav", 'rb'))

#creating a function  for prediction
def diabetes_prediction(input_data):
    input_data = (5,166,72,19,175,25.8,0.587,51)

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    # prediction
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if prediction[0] == 0:
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'
    
def main():
    
    st.title('Diabetes_prediction web app')
    

    Pregnancies = st.text_input('number of  pregnancies')
    Glucose = st.text_input('Glucose')
    BloodPressure = st.text_input('bloddpressure')
    SkinThickness = st.text_input('Skinthickness')
    Insulin = st.text_input('insulin levels')
    BMI = st.text_input('BMI values')
    DiabetesPedigreeFunction = st.text_input('Diabetedpredigreefunction value')
    Age = st.text_input('Age of person')

    diagnosis = ''

    if st.button('Daibetes Test result'):
        diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
 
    st.success(diagnosis)
    
if __name__ == '__main__':
    main()
