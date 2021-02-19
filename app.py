import streamlit as st
from PIL import Image
import pickle

pickle_in = open('classifier.pkl', 'rb') 
model = pickle.load(pickle_in)

image = Image.open('heart.png')
st.image(image, caption='Heart DIsease Prediction')

st.markdown("# Heart Disease Prediction using Machine Learning")

inputs = []

age = st.sidebar.number_input('Enter Age')
inputs.append(age)

gender = st.sidebar.selectbox('Enter Gender', (0,1))
st.sidebar.text('0: Female')
st.sidebar.text('1: Male')
inputs.append(gender)

cp = st.sidebar.selectbox(
    'Type of Chest Pain:',
    (0,1,2,3)
)

st.sidebar.text('0: Typical angina')
st.sidebar.text('1: Atypical angina')
st.sidebar.text('2: Non-anginal pain')
st.sidebar.text('3: Asymptomatic')
inputs.append(cp)


trestbps = st.sidebar.number_input('Enter trestbps')
inputs.append(trestbps)

chol = st.sidebar.number_input('Enter chol')
inputs.append(chol)

fbs = st.sidebar.selectbox(
    'Fasting Blood sugar?',
    (0,1)
)
inputs.append(fbs)


restecg = st.sidebar.selectbox(
    'Enter restecg:',
    (0,1, 2)
)

st.sidebar.text('0: Nothing to note')
st.sidebar.text('1: ST-T Wave abnormality')
st.sidebar.text('2: left-ventricular hypertrophy')
inputs.append(restecg)


thalch = st.sidebar.number_input('Enter Max Heart rate achieved(thalch)')

inputs.append(thalch)

exang = st.sidebar.selectbox(
    'Exercise induced angina:',
    (0,1)
)

st.sidebar.text('1: Yes')
st.sidebar.text('0: No')

inputs.append(exang)


st.write('Old Peak-')
st.write('ST depression induced by exercise relative to rest looks at stress of heart during excercise unhealthy heart will stress more')
oldpeak = st.number_input('Enter oldpeak')
inputs.append(oldpeak)


st.write('slope - the slope of the peak exercise ST segment')
st.write('0: Upsloping: better heart rate with excercise (uncommon)')
st.write('1: Flatsloping: minimal change (typical healthy heart)')
st.write('2: Downslopins: signs of unhealthy heart')
slope = st.selectbox('Enter slope', (0,1,2))
inputs.append(slope)


st.write('ca - number of major vessels (0-3) colored by flourosopy')
st.write('colored vessel means the doctor can see the blood passing through')
st.write('the more blood movement the better (no clots)')
ca = st.selectbox('Enter ca', (0,1,2,3,4))
inputs.append(ca)


st.write('thal - thalium stress result')
st.write('1,3: normal')
st.write('6: fixed defect: used to be defect but ok now')
st.write('7: reversable defect: no proper blood movement when excercising')
thal = st.selectbox('Enter thal', (0,1,2,3,4,5,6,7))
inputs.append(thal)

# st.button('Predict')

if st.button('Predict'):
    result = model.predict([inputs])[0]
    st.markdown('## Result: ')


    if result == 0:
        st.write('Safe')
    else:
        st.write('Not Safe')