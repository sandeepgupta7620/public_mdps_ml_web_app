# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 19:06:04 2022

@author: ASUS
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Multiple Disease Prediction System", page_icon=":tada:", layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")


# loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav','rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('parkinsons_model.sav','rb'))

breast_cancer_model = pickle.load(open('breast_cancer_model.sav','rb'))

# sidebar for navigate

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                           
                           ['User Manual',
                            'Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'Breast Cancer Prediction'],
                           
                           icons = ['person','activity','heart','person','activity'],
                           
                           default_index = 0)
    
    # Sysmptoms page
    
if (selected == 'User Manual'):
    st.title('User Manual')
    st.write("---")
    
    st.subheader("Welcome, to the page :wave: ")
    
    st.write("In this particular webpage, you can predict Diabetes, Heart Disease, Parkinson's Disease and Breast Cancer Disease.")
    
    st.write("---")
    st.subheader("How to use this website ?")
    st.write(
        """
                -  you will be able to find the symptoms that you posses on each module, and thereby you can go for that particular disease prediction.
                
                -  In each modeule, at the bottom of the page, we have provided you with contact form, if incase you have a problem using this website then you can reach out to us.
                
             """
             )
    st.write("---")
    
    st.subheader("Note")
    st.write(
        """
        1) after the prediction is done , and the result is +ve, then you should consult with the doctor about the diseases.
        2) Prediction Accuracy rate is 80 to 85%.
        
        """
        )
    st.write("---")
    

        
# Diabetes Prediction page
if (selected == 'Diabetes Prediction'):
    
    #page title
    st.title('Diabetes Prediction using ML')
    
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("Diabetes Disease")
            st.write("##")
            st.write(
                """
                Diabetes is a chronic (long-lasting) health condition that affects how your body turns food into energy.
                If you have any of the following diabetes symptoms, you can go for Diabetes disease prediction.
                - Urinate (pee) a lot, often at night
                - Are very thirsty, Are very hungry
                - Lose weight without trying
                - Have blurry vision
                - Have numb or tingling hands or feet
                - Feel very tired
                - Have very dry skin
                - Have sores that heal slowly
                - Have more infections than usual
                
                """
            )
            st.write("[For more info >](https://www.cdc.gov/diabetes/basics/diabetes.html)")
            
            st.write("If you have some of the above symptoms, you can predict wheather you have Diabetes or not")
            st.write("##")
 # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)
    
    with st.container():
        st.write("---")
        st.header("Get In Touch With Me!")
        st.write("##")

        # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
        contact_form = """
        <form action="https://formsubmit.co/sandeep.p.gupta@slrtce.in" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()
    
# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("Heart Disease")
            st.write("##")
            st.write(
                """
                The term “heart disease” refers to several types of heart conditions. The most common type of heart disease in the United States is coronary artery disease (CAD), which affects the blood flow to the heart. Decreased blood flow can cause a heart attack.            
                Symptoms of coronary artery disease can include:
                - Chest pain, chest tightness, chest pressure and chest discomfort (angina)
                - Shortness of breath
                - Pain in the neck, jaw, throat, upper belly area or back
                - Pain, numbness, weakness or coldness in the legs or arms if the blood vessels in those body areas are narrowed
                - Pale gray or blue skin or lips (cyanosis)
                - Swelling in the legs, belly area or areas around the eyes
                - In an infant, shortness of breath during feedings, leading to poor weight gain
                - Easily getting short of breath during exercise or activity
                - Dizziness, lightheadedness and fainting
                
                
                """
            )
            st.write("[For more info >](https://www.mayoclinic.org/diseases-conditions/heart-disease/symptoms-causes/syc-20353118)")
            
            st.write("If you have some of the above symptoms, you can predict wheather you have Heart Disease or not")
            st.write("##")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    with st.container():
        st.write("---")
        st.header("Get In Touch With Me!")
        st.write("##")

        # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
        contact_form = """
        <form action="https://formsubmit.co/sandeep.p.gupta@slrtce.in" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("Parkinson's Disease")
            st.write("##")
            st.write(
                """
                Parkinson’s disease is a brain disorder that causes unintended or uncontrollable movements, such as shaking, stiffness, and difficulty with balance and coordination.
                Symptoms usually begin gradually and worsen over time. As the disease progresses, people may have difficulty walking and talking. They may also have mental and behavioral changes, sleep problems, depression, memory difficulties, and fatigue.
               
                Parkinson’s has four main symptoms:
                - Tremor in hands, arms, legs, jaw, or head
                - Muscle stiffness, where muscle remains contracted for a long time
                - Slowness of movement
                - Impaired balance and coordination, sometimes leading to falls
                
                Other symptoms may include:
                - Depression and other emotional changes
                - Difficulty swallowing, chewing, and speaking
                - Urinary problems or constipation
                - Skin problems
                
                """
            )
            st.write("[For more info >](https://www.nia.nih.gov/health/parkinsons-disease)")
            
            st.write("If you have some of the above symptoms, you can predict wheather you have Parkinson's disease or not")
            st.write("##")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz) [Average vocal fundamental frequency]')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz) [Maximum vocal fundamental frequency]')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz) [Minimum vocal fundamental frequency]')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%) [Several measures of variation in fundamental frequency]')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs) [Several measures of variation in fundamental frequency]')
        
    with col1:
        RAP = st.text_input('MDVP:RAP [Several measures of variation in fundamental frequency]')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ [Several measures of variation in fundamental frequency]')
        
    with col3:
        DDP = st.text_input('Jitter:DDP [Several measures of variation in fundamental frequency]')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer [Several measures of variation in amplitude NHR,HNR]')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)
    
    with st.container():
        st.write("---")
        st.header("Get In Touch With Me!")
        st.write("##")

        # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
        contact_form = """
        <form action="https://formsubmit.co/sandeep.p.gupta@slrtce.in" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()
    
# Breast Cancer Prediction page
if (selected == 'Breast Cancer Prediction'):
    
    #page title
    st.title('Breast Cancer Prediction using ML')
    
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("Breast Cancer Disease")
            st.write("##")
            st.write(
                """
                Breast cancer happens when cells in your breast grow and divide in an uncontrolled way, creating a mass of tissue called a tumor. Signs of breast cancer can include feeling a lump in your breast, experiencing a change in the size of your breast and seeing changes to the skin on your breasts.
                
                Breast cancer is most often diagnosed in adults over the age of 50, but it can occur at any age.
                
                Is breast cancer malignant or benign?
                
                What are the symptoms of benign breast disease?
                
                Benign breast disease makes you more prone to getting breast lumps. Finding a lump can be scary, but these breast changes are benign (not cancer). Certain types of breast disease increase your risk of breast cancer. 
                - Breast pain (mastalgia)
                - Nipple discharge.
                - Change in breast size, shape or contour.
                - Inverted, creased or scaly nipple.
                - Dimpled, puckered or scaly breasts.
                
                What are the symptoms of Malignant breast disease?
                
                Breast cancer is a malignant tumor that grows in or around the breast tissue, mainly in the milk ducts and glands. A tumor usually starts as a lump or calcium deposit that develops as a result of abnormal cell growth.
                - Arms and legs feeling painless
                - Fatigue
                - Weight loss
                - Severe pain
                - Skin changes, such as yellowing, darkening or redness of the skin, sores that won't heal, or changes to existing moles.
                
                """
            )
            st.write("[For more info >](https://www.cdc.gov/cancer/breast/basic_info/symptoms.htm)")
            
            st.write("If you have some of the above symptoms, you can predict wheather you have Benign Breast Cancer or Malignant Breast Cancer")
            st.write("##")
    
 # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        mean_radius = st.text_input('Mean Radius')
        
    with col2:
        mean_texture = st.text_input('Mean Texture')
    
    with col3:
        mean_perimeter = st.text_input('Mean perimeter')
    
    with col1:
        mean_area = st.text_input('Mean Area')
    
    with col2:
        mean_smoothness = st.text_input('Mean Smoothness')
    
    with col3:
        mean_compactness = st.text_input('Mean Compactness')
    
    with col1:
        mean_concavity = st.text_input('Mean Concavity')
    
    with col2:
        mean_concave_points = st.text_input('Mean Concave Points')
    
    with col3:
        mean_symmetry = st.text_input('Mean Symmetry')
    
    with col1:
        mean_fractal_dimension = st.text_input('Mean Fractal Dimension')
    
    with col2:
        radius_error = st.text_input('Radius Error')
    
    with col3:
        texture_error = st.text_input('Texture Error')
    
    with col1:
        perimeter_error = st.text_input('Perimeter Error')
    
    with col2:
        area_error = st.text_input('Area Error')
    
    with col3:
        smoothness_error = st.text_input('Smoothness Error')
    
    with col1:
        compactness_error = st.text_input('Compactness Error')
    
    with col2:
        concavity_error = st.text_input('Concavity Error')
    
    with col3:
        concave_points_error = st.text_input('Concave Points Error')
    
    with col1:
        symmetry_error = st.text_input('Symmetry Error')
    
    with col2:
        fractal_dimension_error = st.text_input('Fractal Dimension Error')
    
    with col3:
        worst_radius = st.text_input('Worst Radius')
        
    with col1:
        worst_texture = st.text_input('Worst Texture')
    
    with col2:
        worst_perimeter = st.text_input('Worst Perimeter')
    
    with col3:
        worst_area = st.text_input('Worst Area')
    
    with col1:
        worst_smoothness = st.text_input('Worst Smoothness')
    
    with col2:
        worst_compactness = st.text_input('Worst Compactness')
    
    with col3:
        worst_concavity = st.text_input('Worst Concavity')
    
    with col1:
        worst_concave_points = st.text_input('Worst Concave Points')
    
    with col2:
        worst_symmetry = st.text_input('Worst Symmetry')
    
    with col3:
        worst_fractal_dimension = st.text_input('Worst Fractal Dimension')
  
    # code for Prediction
    breast_cancer_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Breast Cancer Test Result'):
        breast_cancer_prediction = breast_cancer_model.predict([[mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness,mean_compactness,mean_concavity,mean_concave_points,
                                                                 mean_symmetry,mean_fractal_dimension,radius_error,texture_error,perimeter_error,area_error,smoothness_error,
                                                                 compactness_error,concavity_error,concave_points_error,symmetry_error,fractal_dimension_error,
                                                                 worst_radius,worst_texture,worst_perimeter,worst_area,worst_smoothness,worst_compactness,
                                                                 worst_concavity,worst_concave_points,worst_symmetry,worst_fractal_dimension]])
        
        if (breast_cancer_prediction[0] == 1):
          breast_cancer_diagnosis = 'The Breast Cancer is Benign'
        else:
          breast_cancer_diagnosis = 'The Breast cancer is Malignant'
        
    st.success(breast_cancer_diagnosis)
    
    with st.container():
        st.write("---")
        st.header("Get In Touch With Me!")
        st.write("##")

        # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
        contact_form = """
        <form action="https://formsubmit.co/sandeep.p.gupta@slrtce.in" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()
    
    
    
    


    

    
