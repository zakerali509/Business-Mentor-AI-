import streamlit as st
from openai import OpenAI

# OpenAI کلائنٹ سیٹ اپ
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("💼 زاکر کا بزنس مینٹور AI")
st.write("ہیلو! میں آپ کا پرسنل بزنس مینٹور ہوں۔ آپ مجھ سے ڈراپ شپنگ، ایمیزون، اور آن لائن بزنس کے بارے میں کچھ بھی پوچھ سکتے ہیں۔")

# سسٹم پرامپٹ (یہ اس کا دماغ ہے)
system_instruction = """
تم ایک ماہر بزنس مینٹور ہو جو بالکل نئے سیکھنے والوں (Beginners) کی مدد کرتے ہو۔ 
تمہارے جوابات کا انداز سادہ، مخلصانہ، اور حوصلہ افزا ہونا چاہیے۔ 
اگر کوئی صارف اپنا 'پیشن' بتائے، تو تم اسے اسی کے مطابق ایک سادہ سا 30 دن کا روڈ میپ بنا کر دو۔ 
مشکل الفاظ سے پرہیز کرو اور انہیں قدم بہ قدم گائیڈ کرو۔ 
تمہارا مقصد انہیں ایمیزون اور آن لائن بزنس میں کامیاب بنانا ہے۔
"""

# چیٹ ہسٹری مینجمنٹ
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": system_instruction}]

# چیٹ ڈسپلے کرنا
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# یوزر کا ان پٹ
if prompt := st.chat_input("اپنا کاروباری سوال پوچھیں..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages
        )
        full_response = response.choices[0].message.content
        st.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    
