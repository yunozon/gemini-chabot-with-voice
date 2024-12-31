import streamlit as st
import google.generativeai as genai
import os
from PIL import Image
from dotenv import load_dotenv
load_dotenv()

# streamlitでgemini apiを使って簡単なchatbotを作成するサンプルコード。画像の入力も受け付ける

# Gemini api key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Gemini modelの初期化
model = genai.GenerativeModel("gemini-1.5-flash-8b")
img = Image.open("sample.jpg")

response = model.generate_content(["こんにちは、画像のキャラクターになりきって、自己紹介してほしいです", img])
print(response.text)

