import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

# streamlitでgemini apiを使って簡単なchatbotを作成するサンプルコード

# Gemini api key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Gemini modelの初期化
model = genai.GenerativeModel("gemini-1.5-flash-8b")

# タイトル
st.title("Gemini chatbot")

# ユーザーの入力
user_input = st.text_input("ユーザーの入力")
if user_input:
    response = model.generate_content(user_input)
    st.write(response.text)
