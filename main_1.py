import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from sklearn import preprocessing

le = preprocessing.LabelEncoder()


# loading the saved models

cervical_model = pickle.load(open('cervical_model.sav', 'rb'))

thyroid_model = pickle.load(open('thyroid_model.sav', 'rb'))

mesothelioma_model = pickle.load(open('mesothelioma_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
        selected = option_menu('Home Diagnostic',

                           ['Thyroid Prediction',
                            'Cervical cancer Prediction',
                            'Mesothelioma Prediction'],
                           menu_icon='hospital-fill',
                           default_index=0)
    #Thyroid Prediction Page
if selected == 'Thyroid Prediction':

    # page title
        st.title('Thyroid Prediction');
        
        col1, col2, col3 = st.columns(3)
    
        with col1:
            age = st.text_input('Age of the Person')
    
        with col2:
            sex = st.text_input('Enter your gender')
 
        with col3:
            on_antithyroid_meds = st.text_input('On antithyroid meds')

        with col1:
            pregnant = st.text_input('Pregnant')

        with col2:
            thyroid_surgery = st.text_input('Thyroid surgery')

        with col3:    
            query_hyperthyroid = st.text_input('Query hyperthyroid')

        with col1:
            tumor = st.text_input('Tumor')

        with col2:
            TSH_measured = st.text_input('TSH measured')

        with col3:
            TSH = st.text_input('TSH')

        with col1:
            T3_measured = st.text_input('T3 measured')

        with col2:
            T3 = st.text_input('T3')

        with col3:
            TT4_measured = st.text_input('TT4 measured')   
 
        with col1:
            TT4 = st.text_input('TT4')

        with col2:
            T4U_measured = st.text_input('T4U measured')

        with col3:
            T4U = st.text_input('T4U')

        with col1:
            FTI = st.text_input('FTI')

        with col2:
            TBG = st.text_input('TBG')

        with col3:
            referral_source = st.text_input('Referral source')


    
    # code for Prediction
        thyroid_diagnosis = ''
    
    # creating a button for Prediction
     
    
        if st.button('Thyroid Test Result'):
        #st.success([age,sex, on_antithyroid_meds, pregnant,thyroid_surgery,query_hyperthyroid,tumor, TSH_measured,TSH, T3_measured,T3, TT4_measured, TT4,T4U_measured, T4U,FTI, TBG,referral_source])
            user_input = [age,sex, on_antithyroid_meds, pregnant,thyroid_surgery,query_hyperthyroid,tumor, TSH_measured,TSH, T3_measured,T3, TT4_measured, TT4,T4U_measured, T4U,FTI, TBG,referral_source]
  
            user_input = le.fit_transform(user_input)
#        import numpy as np
# Convert y to a one-dimensional array
#       user_input = user_input.flatten()  

       

#       st.success(user_input)

            thyroid_prediction = thyroid_model.predict([user_input])
            

       # thyroid_prediction = thyroid_model.predict([[age,sex, on_antithyroid_meds, pregnant,thyroid_surgery,query_hyperthyroid,tumor, TSH_measured,TSH, T3_measured,T3, TT4_measured, TT4,T4U_measured, T4U,FTI, TBG,referral_source]])

       # thyroid_prediction = thyroid_model.predict([[le.fit_transform(age),le.fit_transform(sex), le.fit_transform(on_antithyroid_meds),le.fit_transform(pregnant),le.fit_transform(thyroid_surgery),le.fit_transform(query_hyperthyroid),le.fit_transform(tumor), le.fit_transform(TSH_measured),le.fit_transform(TSH), le.fit_transform(T3_measured),le.fit_transform(T3), le.fit_transform(TT4_measured), le.fit_transform(TT4),le.fit_transform(T4U_measured), le.fit_transform(T4U),le.fit_transform(FTI), le.fit_transform(TBG),le.fit_transform(referral_source)]])

            if thyroid_prediction[0] == 1:
                thyroid_diagnosis = 'Thyroid Positive'
            else:
                thyroid_diagnosis = 'Thyroid Negative'

            st.success(thyroid_diagnosis)


    
    
    #Cervical cancer Prediction Page
if selected == 'Cervical cancer Prediction':

    # page title
        st.title('Cervical cancer Prediction')
        col1, col2, col3 = st.columns(3)
        with col1:
            Age = st.text_input('Age of the Person')

        with col2:
            First_sexual_intercourse = st.text_input('First sexual intercourse')

        with col3:
            Num_of_pregnancies = st.text_input('Number of pregnancies')

        with col1:
            Smokes = st.text_input('Smokes')

        with col2:
            Smokes_years = st.text_input('Smokes years')

        with col3:
            Smokes_packs_per_year = st.text_input('Smokes packs per year')

        with col1:
            Hormonal_Contraceptives_years = st.text_input('Hormonal Contraceptives years')

        with col2:
            IUD = st.text_input('IUD')

        with col3:
            STDs_vulvo_perineal_condylomatosis = st.text_input('STDs vulvo perineal condylomatosis')

        with col1:
            STDs_syphilis = st.text_input('STDs syphilis')

        with col2:
            STDs_Number_of_diagnosis = st.text_input('STDs Number of diagnosis')   
    
        with col3:
            STDs_Time_since_first_diagnosis = st.text_input('STDs Time since first diagnosis')

        with col1:
            STDs_Time_since_last_diagnosis = st.text_input('STDs Time since last diagnosis')

        with col2:
            Dx_Cancer = st.text_input('Dx Cancer')

        with col3:
            Dx_HPV = st.text_input('Dx HPV')
            
        with col1:
            Dx = st.text_input('Dx')
            
        with col2:
            Hinselmann = st.text_input('Hinselmann')

        with col3:
            Schiller= st.text_input('Schiller')
        
        with col1:
            Citology = st.text_input('Citology')
            
    # code for Prediction
        cervical_diagnosis = ''
            
            # creating a button for Prediction
             
            
        if st.button('Cervical cancer Test Result'):
                #st.success([age,sex, on_antithyroid_meds, pregnant,thyroid_surgery,query_hyperthyroid,tumor, TSH_measured,TSH, T3_measured,T3, TT4_measured, TT4,T4U_measured, T4U,FTI, TBG,referral_source])
                user_input_c = [Age, First_sexual_intercourse, Num_of_pregnancies, Smokes, Smokes_years, Smokes_packs_per_year, Hormonal_Contraceptives_years, IUD, STDs_vulvo_perineal_condylomatosis, STDs_syphilis, STDs_Number_of_diagnosis, STDs_Time_since_first_diagnosis, STDs_Time_since_last_diagnosis, Dx_Cancer, Dx_HPV, Dx, Hinselmann, Schiller, Citology]
          
                user_input_c = le.fit_transform(user_input_c)
        #        import numpy as np
        # Convert y to a one-dimensional array
         #       user_input = user_input.flatten()  

               

         #       st.success(user_input)

                cervical_prediction = cervical_model.predict([user_input_c])
                

               

                if cervical_prediction[0] == 1:
                    cervical_diagnosis = 'Cervical Positive'
                else:
                    cervical_diagnosis = 'Cervical Negative'

                st.success(cervical_diagnosis)
            
            
            
            
            
    
    
    
if selected == 'Mesothelioma Prediction':

    # page title
    st.title('Mesothelioma Prediction') 
    col1, col2, col3 = st.columns(3)
    
    
    
    
    with col1:
        age = st.text_input('Age of the Person')

    with col2:
        gender = st.text_input('Gender')

    with col3:
        city = st.text_input('City')

    with col1:
        asbestos_exposure = st.text_input('Asbestos Exposure')

    with col2:
        type_of_MM = st.text_input('Type of MM')

    with col3:
        duration_of_asbestos_exposure = st.text_input('Duration of asbestos exposure')

    with col1:
        diagnosis_method = st.text_input('Diagnosis Method')

    with col2:
        keep_side = st.text_input('Keep Side')

    with col3:
        cytology = st.text_input('Cytology')

    with col1:
        duration_of_symptoms = st.text_input('Duration of Symptoms')

    with col2:
        dyspnoea = st.text_input('Dyspnoea')   
    
    with col3:
        ache_on_chest = st.text_input('Ache On Chest')

    with col1:
        weakness = st.text_input('Weakness')

    with col2:
        habit_of_cigarette = st.text_input('Habit of Cigarette')

    with col3:
        performance_status = st.text_input('Performance Status')

    with col1:
        white_blood = st.text_input('White Blood')

    with col2:
        cell_count = st.text_input('Cell Count')
    
    with col3:
        hemoglobin = st.text_input('Hemoglobin')

    with col1:
        platelet_count_PLT = st.text_input('Platelet Count PLT')

    with col2:
        sedimentation = st.text_input('Sedimentation')

    with col3:
        blood_lactic_dehydrogenise = st.text_input('Blood Lactic Dehydrogenise')

    with col1:
        alkaline_phosphatise = st.text_input('Alkaline Phosphatise')

    with col2:
        total_protein = st.text_input('Total Protein')

    with col3:
        albumin = st.text_input('Albumin')

    with col1:
        glucose = st.text_input('Glucose')

    with col2:
        pleural_lactic_dehydrogenise = st.text_input('Pleural Lactic Dehydrogenise')

    with col3:
        pleural_protein	 = st.text_input('Pleural Protein')

    with col1:
        pleural_albumin = st.text_input('Pleural Albumin')   
    
    with col2:
        pleuralglucose = st.text_input('Pleuralglucose')

    with col3:
        dead_or_not = st.text_input('Dead or Not')

    with col1:
        pleural_effusion = st.text_input('Pleural Effusion')

    with col2:
        pleural_thickness_on_tomography = st.text_input('Pleural Thickness on Tomography')

    with col3:
        pleural_level_of_acidity= st.text_input('Pleural Level of Acidity')

    with col1:
        creative_protine = st.text_input('Creative Protine')
        
        
    # code for Prediction
        mesothelioma_diagnosis = ''
            
            # creating a button for Prediction
             
            
    if st.button('Mesothelioma Test Result'):
                #st.success([age,sex, on_antithyroid_meds, pregnant,thyroid_surgery,query_hyperthyroid,tumor, TSH_measured,TSH, T3_measured,T3, TT4_measured, TT4,T4U_measured, T4U,FTI, TBG,referral_source])
        user_input_m = [age,gender,city, asbestos_exposure, type_of_MM, duration_of_asbestos_exposure, diagnosis_method, keep_side, cytology, duration_of_symptoms,dyspnoea, ache_on_chest, weakness, habit_of_cigarette, performance_status,	white_blood, cell_count, hemoglobin, platelet_count_PLT, sedimentation,	blood_lactic_dehydrogenise, alkaline_phosphatise, total_protein,	albumin, glucose, pleural_lactic_dehydrogenise,	pleural_protein, pleural_albumin, pleuralglucose, dead_or_not, pleural_effusion, pleural_thickness_on_tomography, pleural_level_of_acidity, creative_protine]
          
        user_input_m = le.fit_transform(user_input_m)
        #        import numpy as np
        # Convert y to a one-dimensional array
         #       user_input = user_input.flatten()  

               

         #       st.success(user_input)

        mesothelioma_prediction = mesothelioma_model.predict([user_input_m])
        

               

        if mesothelioma_prediction[0] == 1:
            mesothelioma_diagnosis = 'Mesothelioma Positive'
        else:
            mesothelioma_diagnosis = 'Mesothelioma Negative'

        st.success(mesothelioma_diagnosis)
