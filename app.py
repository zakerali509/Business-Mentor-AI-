import streamlit as st
from openai import OpenAI

# Streamlit secrets سے API Key حاصل کرنا
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("Business Mentor AI")

st.write("خوش آمدید! میں آپ کا بزنس مینٹور ہوں۔ آپ مجھ سے بزنس، ڈسپلن اور مالیاتی مسائل پر مشورہ لے سکتے ہیں۔")

# یوزر سے سوال لینا
user_input = st.text_input("اپنا سوال یہاں لکھیں:")

if st.button("پوچھیں"):
    if user_input:
        try:
            # OpenAI کو سوال بھیجنا
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_input}]
            )
            # جواب دکھانا
            st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"کوئی غلطی ہوئی: {e}")
    else:
        st.warning("براہ کرم اپنا سوال درج کریں۔")
        
