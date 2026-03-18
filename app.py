import streamlit as st
import pickle
import re

# Load saved model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
tfidf = pickle.load(open("vectorizer.pkl", "rb"))

# Text cleaning function
def clean_text(text):
    text = text.lower()
    text = re.sub('[^a-zA-Z]', ' ', text)
    return text

# Prediction function
def predict_email(text):
    text = clean_text(text)
    vector = tfidf.transform([text]).toarray()
    prediction = model.predict(vector)
    return "🚨 Spam" if prediction[0] == 1 else "✅ Not Spam"

# Streamlit UI
st.title("📧 Email Fraud Detection")

st.write("Enter an email/message to check if it's spam or not.")

user_input = st.text_area("Enter your message here")

if st.button("Check"):
    if user_input.strip() != "":
        result = predict_email(user_input)
        st.subheader("Result:")
        st.write(result)
    else:
        st.warning("Please enter a message!")