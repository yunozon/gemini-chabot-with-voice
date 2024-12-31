import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

"""
gemini apiでプロンプトに対して文章を生成するサンプルコード
"""

# Gemini api key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel("gemini-1.5-flash-8b")
response = model.generate_content("こんにちは、自己紹介してほしいです")
print(response.text)