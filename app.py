import streamlit as st
import joblib
model = joblib.load('email_class')
st.title('spam ham classifier')
ip = st.text_input('Enter your message')
op = model.predict([ip])
if st.buttom('predict'):
  st.title(op[0])
