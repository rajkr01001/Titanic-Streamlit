import streamlit as st
import pickle

st.set_page_config(page_title='Titanic Survival Prediction', layout='wide')

st.title('Titanic Survival Prediction')
st.sidebar.markdown('Enter Passengers details to predict survival chance')

with open('a.pkl', 'rb') as file:
    model = pickle.load(file)

pclass = st.sidebar.selectbox('Passenger Class',[1,2,3])
age = st.sidebar.slider('Age in Years',0,60,30)
sex = st.sidebar.selectbox('Select Gender 0 = Female, 1 = Male', [0,1])
fare = st.sidebar.number_input('Fare in USD',0.0,255.0)

if st.sidebar.button('Predict'):
    inputs = [[pclass,sex,age,fare]]
    prediction = model.predict(inputs)

    if prediction == 1:
        st.success('You are likely to Survive')
    else:
        st.error('Survival chances are very low')



hide_menu = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)


            
