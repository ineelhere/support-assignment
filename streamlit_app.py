import streamlit as st
import wget
import os

st.title("My Streamlit App!")

with st.form("app_form"):
  status_code = st.radio("Pick a status code", ('101','102','405','406','407','416','417','500','502','521'))
  
  submitted = st.form_submit_button("Submit")
  if submitted:
      st.write("You pressed submit!") # confirm that the user pressed submit
      st.image(wget.download('https://http.cat/' + status_code), width=500) #download and show the image
      if os.path.exists(status_code): # check if the file exists on memory
          os.remove(status_code) # if the file exists, delete the same to save memory
