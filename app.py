import streamlit as st
import pickle
import numpy as np

loaded_model = pickle.load(open("trained_model.sav", "rb"))

st.title("🩺 Diabetes Prediction System")

st.write("Enter the patient's medical details below.")

pregnancies = st.number_input("Pregnancies", min_value=0)
glucose = st.number_input("Glucose")
bloodpressure = st.number_input("Blood Pressure")
skinthickness = st.number_input("Skin Thickness")
insulin = st.number_input("Insulin")
bmi = st.number_input("BMI")
dpf = st.number_input("Diabetes Pedigree Function")
age = st.number_input("Age")

if st.button("Predict"):

    input_data = np.asarray([[pregnancies, glucose, bloodpressure,
                              skinthickness, insulin,
                              bmi, dpf, age]])

    prediction = loaded_model.predict(input_data)

    if prediction[0] == 0:
        st.success("The person is NOT diabetic.")
    else:
        st.error("The person IS diabetic.")