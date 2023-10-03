import streamlit as st
import requests

# GUI layout
st.title('Heart Disease Prediction')

if "token" not in st.session_state:
    st.session_state.token = None

# User login
st.sidebar.subheader("User Login")
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")
if st.sidebar.button('Login'):
    response = requests.post('http://localhost:8000/auth/token', json={'username': username, 'password': password})
    if response.status_code != 200:
        st.sidebar.write('Login failed')
    else:
        st.session_state.token = response.json()['access_token']
        st.sidebar.write('Logged in successfully')

# GUI inputs
age = st.number_input('Age', value=25)
sex = st.selectbox('Sex', [0, 1])
cp = st.selectbox('Chest Pain Type', [0, 1, 2, 3])
trestbps = st.number_input('Resting Blood Pressure', value=120)
chol = st.number_input('Serum Cholestoral in mg/dl', value=200)
fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', [0, 1])
restecg = st.selectbox('Resting Electrocardiographic Results', [0, 1, 2])
thalach = st.number_input('Maximum Heart Rate Achieved', value=150)
exang = st.selectbox('Exercise Induced Angina', [0, 1])
oldpeak = st.number_input('ST Depression Induced by Exercise Relative to Rest', value=0.0)
slope = st.selectbox('Slope of the Peak Exercise ST Segment', [0, 1, 2])
ca = st.selectbox('Number of Major Vessels Colored by Flourosopy', [0, 1, 2, 3])
thal = st.selectbox('Thal', [0, 1, 2, 3])

# When 'Predict' is clicked, make a request to the API and display the output
if st.button('Predict'):
    if st.session_state.token is None:
        st.write('Please login first')
    else:
        response = requests.post('http://localhost:8000/predict', headers={'Authorization': f'Bearer {st.session_state.token}'}, json={
        'age': age,
        'sex': sex,
        'cp': cp,
        'trestbps': trestbps,
        'chol': chol,
        'fbs': fbs,
        'restecg': restecg,
        'thalach': thalach,
        'exang': exang,
        'oldpeak': oldpeak,
        'slope': slope,
        'ca': ca,
        'thal': thal
        })

        if response.status_code == 200:
            prediction = response.json()['prediction']
            st.write(f'Prediction: {prediction}')
        else:
            st.write('Failed to get prediction')