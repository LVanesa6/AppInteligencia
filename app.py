import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import pandas as pd2


# Establecer configuración de página
st.set_page_config(page_title="Asistente de salud",
                   layout="wide",
                   page_icon="🩺")

    
# obtener el directorio de trabajo de main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# cargar modelos guardados

diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))

hipertension_model = pickle.load(open(f'{working_dir}/saved_models/hipertension_model.sav', 'rb'))

# sidebar for navigation

with st.sidebar:
    selected = option_menu('Diagnóstico de enfermedades',

                           ['Diagnóstico de diabetes',
                            'Diagnóstico de hipertensión'
                            ],
                           menu_icon='clipboard-check',
                           icons=['activity', 'heart'],
                           default_index=0)



if selected == 'Diagnóstico de diabetes':


    st.title('Diagnóstico de diabetes usando algoritmo de machine learning')

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Número de embarazos')

    with col2:
        Glucose = st.text_input('Nivel de glucosa')

    with col3:
        BloodPressure = st.text_input('Valor de presión arterial')

    with col1:
        SkinThickness = st.text_input('Valor de espesor de piel')

    with col2:
        Insulin = st.text_input('Nivel de insulina')

    with col3:
        BMI = st.text_input('valor de Indice de masa corporal (IMC)')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Valor de la función pedigrí de la diabetes')

    with col2:
        Age = st.text_input('Edad de la persona')


 
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Resultado del test'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        input_df = pd.DataFrame([user_input], columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'])

        diab_prediction = diabetes_model.predict(input_df)

        if diab_prediction[0] == 1:
            diab_diagnosis = 'La persona es diabetica'
        else:
            diab_diagnosis = 'La persona no es diabetica'

    st.success(diab_diagnosis)


if selected == 'Diagnóstico de hipertensión':

 
    st.title('Diagnóstico de hipertensión usando algoritmo de machine learning')

    col1, col2, col3 = st.columns(3)

    with col1:
        sex = st.text_input('Maculino = 0, Femenino = 1')

    with col2:
        edad = st.text_input('Edad')

    with col3:
        ps = st.text_input('Presión arterial sistólica')

    with col1:
        pd = st.text_input('Presión arterial diastólica')

    with col2:
        peso = st.text_input('Peso en KG')

    with col3:
        altura = st.text_input('Altura en (cm)')

    with col1:
        fuma = st.text_input(' 0 = no fuma, 1 = si fuma')

    with col2:
        afisica = st.text_input('0 = no realiza actividad fisica, 1 = si realiza')

   

    # code for Prediction
    hipertension_diagnosis = ''

    # creating a button for Prediction

    if st.button('Resultado del test'):

        user_input = [sex, edad, ps, pd, peso, altura, fuma, afisica]

        user_input = [float(x) for x in user_input]

        input_df = pd2.DataFrame([user_input], columns=['sex', 'age_years', 'systolic_bp', 'diastolic_bp', 'weight_kg', 'height_cm', 'smoking', 'physical_activity'])

        hipertension_prediction = hipertension_model.predict(input_df)

        if hipertension_prediction[0] == 1:
             hipertension_diagnosis = 'La persona tiene hipertension'
        else:
             hipertension_diagnosis = 'La persona no tiene hiperstension'

    st.success(hipertension_diagnosis)

