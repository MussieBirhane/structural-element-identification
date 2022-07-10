import streamlit as st

st.title('Registration form')

first, last = st.columns(2)
first.text_input('First name')
last.text_input('Last name')

email, mobile = st.columns([3, 1])
email.text_input('Email')
mobile.text_input('Mobile No.')

user, pass1, pass2 = st.columns(3)
user.text_input('Username')
pass1.text_input('Password', type='password')
pass2.text_input('Confirm your password', type='password')

check, blank, submit = st.columns(3)
check.checkbox('I agree')
submit.button('Submit')


