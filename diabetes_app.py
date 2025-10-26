2# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved model

diabetes_model = pickle.load(open('diabetes_model (2).sav','rb'))

# Page title

st.title('Diabetes Pridection using ML')

Pregnancies = st.text_input('Number of Pregnancies')
Glucose = st.text_input('Glucose level')
BloodPressure = st.text_input('Blood Pressure value')
SkinThickness = st.text_input('Skin Thickness value')
Insulin = st.text_input('Insulin level')
BMI = st.text_input('BMI value')
DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
Age = st.text_input('Age of the person')

#Code for prediction
diab_diagnosis=''

#Creating a button for prediction

if st.button('Diabetes Test Result'):
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    
    if (diab_prediction[0]==1):
        diab_diagnosis = 'The person is diabetic'
        
    else:
        diab_diagnosis = 'The person is Not Diabetic'
    
st.success(diab_diagnosis)  

    
