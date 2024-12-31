import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Gemini api key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Gemini modelの初期化
model = genai.GeminiModel("gemini-1.5-flash-8b")