import streamlit as st
import pandas as pd
# images libraries
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title='Web Application')
st.header('streamlit web application')
st.subheader('Linear Regression')
st.latex('y=mx+c')
st.markdown('_Linear regression is a statistical method used to model the relationship between a dependent variable and one or more independent variables. It provides valuable insights for prediction and data analysis._')
st.text('_this is a text_')
st.caption('this is a caption')

# type the any program
st.code('''numbers=[10,20,30,40,50]
total_sum=0
for num in numbers:
  total_sum +=num
  print(f"sum of numbers:{total_sum}"''',language='python')

# reading the data using pandas

data=pd.read_csv('sample.csv')
st.dataframe(data)
# button
submit=st.button('submit')

# checkbox
submit=st.checkbox('submit')

#radio button

if submit:
    st.dataframe(data)
st.radio('choose one',{'a','b','c','d'})


# table view

st.table(data)

#json value

h={'a':{1,2,3},'b':{8,9,10}}
st.json(h)


# columns --> metric values

col1,col2 = st.columns(2)
with col1:
    st.metric('IBM','$100','-5%')
with col2:
    st.metric('ZOHO','$50','100%')


# select box
cols=list(data.columns)
name=st.selectbox('choose a any attribute:',cols)
st.write(cols)
st.write('The attribute selected by the user',name)


# text box
col1,col2 = st.columns(2)
with col1:
    a=st.number_input('Enter a number1')
with col2:
    b=st.number_input('Enter a number2')
submit=st.button('ADD')
if submit:
    st.write('The sum of a and b is',a+b)

#slider
col1,col2=st.columns(2)
with col1:
    a=st.slider('Enter a number1',0,100,10)
with col2:
    b=st.slider('Enter a number2',0,10,1)
submit=st.checkbox('ADD')
if submit:
    st.write('The sum of a and b is',a+b)

option=st.multiselect('Choose your variable',cols)
st.write('Your selection',option)

#Images adding
submit=st.checkbox('show images')
if submit:
    img =Image.open(r'C:/Users/gamin/Desktop/Python/img.jpg')
    st.image(img)

#charts
target=st.selectbox('choose a target',cols)
col2 = cols.copy()
col2.remove(target)
x_var=st.selectbox('choose a x variable',col2)
y_var =st.selectbox('choose a y variable',col2)

fig=px.scatter(data,x=x_var,y=y_var,color=target)
st.plotly_chart(fig)
    


