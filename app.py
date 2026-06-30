import streamlit as st

st.title("Business Mentor AI")
st.write("خوش آمدید! میں آپ کا بزنس مینٹور ہوں۔ آپ مجھ سے بزنس، ڈسپلن اور مالیاتی مسائل پر مشورہ لے سکتے ہیں۔")

user_input = st.text_input("اپنا سوال یہاں لکھیں:")
if st.button("پوچھیں"):
    st.write("آپ کا بزنس مینٹور ابھی کام کر رہا ہے...")
  
