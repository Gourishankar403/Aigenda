import streamlit as st
import os 
from PIL import Image
import google.generativeai as genai

genai.configure(api_key="AIzaSyBJ5Fn-Bo-IEDTmubX-pRzz2HdOKEz6F_w")

model = genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(input_text, image_data, prompt):
    response = model.generate_content([input_text, image_data[0], prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data=uploaded_file.getvalue()
        image_parts=[
            {
                "mime_type":uploaded_file.type,
                "data":bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError
    


st.set_page_config(page_title='WIE is Invoice Generator')
st.sidebar.header("RoboBill")
st.sidebar.write("Made by Me ")
st.sidebar.write('powered by google gemini ai ')
st.header("Robobill ")
st.subheader("Manager your expenses with Robobill")
input=st.text_input('What do you want me to do ?',key='input')
uploaded_file=st.file_uploader('choose an image ',type=['jpg','jpeg','png'])
image=''
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption='uploaded Image',use_column_width=True)

ssubmit=st.button("Lets Go ")


#back end starts from here 

input_prompt="""
you are an expert in reading invoices . We are going to upload an image of 
an invoice and you will have to answer any type of questions that the user asks you
. 
You have to greet the user first Make sure to keep the fonts uniform and give the items 
list in a point-wise format.

At the end , make sure to repeat the name of out app 'RoboBill ' and as the user to 
use it again in the future. leave a lasting impression on the user by wishing him/her
happy and healthy life forward

"""


if ssubmit:
    image_data=input_image_details(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.subheader('here is what you need to know:')
    st.write(response)




