import streamlit as st
import numpy as np

if st.button("Refresh"):
          st.rerun()

st.title("this is a pop quiz for 7 and over.")

n1 =np.random.randint(low = 0,high = 9)
n2=np.random.randint(low=0,high=9)
s=n1+n2
st.write("first number is ",n1)
st.write("second number is",n2)
#st.write("the sum is", s)
a=st.number_input("enter your answer",step=1)

if st.button(" chek your anwser"):
if a==s:
          st.write(" yay all thogh you are not smart you have got it corect")
else:
          st.write ("you are dumb")
          

st.divider()
st.title("reyaans first app")
          
st.write("this is my first app i will make a calculator")
st.write("1*1=")
st.write(1*1)
number1=st.number_input("please insert number 1", step=1)
number2=st.number_input("please insert number 2", step=1)

st.write("the sum is")
st.write(number1+number2)
st.write("the product is")
st.write(number1*number2)
st.write("the difference is")
st.write(number1-number2)
























         
