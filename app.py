%%writefile app.py
import streamlit as st
st.title('Sentimental Analysis')
import pandas as pd
df = pd.read_csv('/content/inshort_news.csv')
x = df.iloc[:, -1]
y = df.iloc[:, 1]

num = st.number_input("Enter the integer between 0 to 59")

if(st.button('Submit')):
  if x[num]>= 0.05:
    st.write(y[num])
    st.write("The above statment is positive 😀")
  
  elif (x[num]> -0.05 and df.compound[num]< 0.05):
    st.write(y[num])
    st.write("The above statment is netural 🙂")
  
  elif x[num]<= -0.05:
    st.write(y[num])
    st.write("The above statment is negative ☹️")
