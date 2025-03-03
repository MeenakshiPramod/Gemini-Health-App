# import streamlit as st
# import os
# from dotenv import load_dotenv
# load_dotenv()
# import google.generativeai as genai
# from PIL import Image

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # Updated model name
# #MODEL_NAME = "gemini-pro-vision"  # Or "gemini-1.5-flash" or other appropriate model name
# MODEL_NAME = "gemini-1.5-flash"

# def get_gemini_response(input, image_parts, prompt):  # Corrected function name
#     model = genai.GenerativeModel(MODEL_NAME) # Use the updated model name
#     response = model.generate_content([input, image_parts[0], prompt]) # Corrected argument order
#     return response.text

# def input_image_setup(uploaded_file):
#     if uploaded_file is not None:
#         bytes_data = uploaded_file.getvalue()
#         image_parts = [
#             {
#                 "mime_type": uploaded_file.type,
#                 "data": bytes_data
#             }
#         ]
#         return image_parts
#     else:
#         return None  # Return None if no file uploaded, handle it later


# st.set_page_config(page_title="Gemini Health App")
# st.header("Gemini Health App")

# uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
# image = None # Initialize image to None
# image_parts = None # Initialize image_parts to None

# if uploaded_file is not None:
#     image = Image.open(uploaded_file)
#     st.image(image, caption="Uploaded Image.", use_column_width=True)
#     image_parts = input_image_setup(uploaded_file) # Assign image_parts here

# input_prompt = """
# You are an expert nutritionist. Analyze the food items in the image and calculate the total calories. Provide details of each food item with its calorie count in the following format:

# 1. Item 1 - Calories: [Number]
# 2. Item 2 - Calories: [Number]
# ...

# Also, analyze the overall healthiness of the meal and provide a percentage breakdown of carbohydrates, proteins, fats, fiber, sugar, and other important dietary components.
# """

# submit = st.button("Tell me the total calories")

# if submit:
#     if image_parts is None: #check if image is uploaded
#         st.error("Please upload an image.")
#     else:
#         try:
#             response = get_gemini_response(input_prompt, image_parts, "") # Pass the prompt, not the user input
#             st.subheader("The Response is")
#             st.write(response)
#         except Exception as e:
#             st.error(f"An error occurred: {e}")  # Handle potential errors gracefully


### Health Management APP
from dotenv import load_dotenv

load_dotenv() ## load all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Google Gemini Pro Vision API And get response

def get_gemini_repsonse(input,image,prompt):
    model=genai.GenerativeModel('gemini-1.5-flash')
    response=model.generate_content([input,image[0],prompt])
    return response.text

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    
##initialize our streamlit app

st.set_page_config(page_title="Gemini Health App")

st.header("Gemini Health App")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_container_width=True)


submit=st.button("Tell me the total calories")

input_prompt="""
You are an expert in nutritionist where you need to see the food items from the image
               and calculate the total calories, also provide the details of every food items with calories intake
               is below format

               1. Item 1 - no of calories
               2. Item 2 - no of calories
               ----
               ----


"""

## If submit button is clicked

if submit:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_repsonse(input_prompt,image_data,input)
    st.subheader("The Response is")
    st.write(response)

