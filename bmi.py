import streamlit as st
weight=st.number_input("Enter weight in kg",min_value=0) #in kg
height=st.number_input("Enter height in cm",min_value=0) #in cm


btn=st.button('BMI')

if btn:
    bmi=weight/(height/100)**2
    st.write(bmi)
    if bmi<18.5:
        st.info("Underweight")
    elif bmi>+18.5 and bmi<=25:
        st.success("Normal")
    elif bmi>25 and bmi<=30:
        st.warning("Overweight")
    else:
        st.error("Obesity")