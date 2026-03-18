📧 Email Fraud Detection 🚨

📌 Project Overview

This project is a Machine Learning-based web application that detects whether an email/message is Spam (Fraud) or Not Spam (Legitimate) using Natural Language Processing (NLP) techniques.

---

🎯 Objective

To build an intelligent system that can automatically classify emails into:

- ✅ Ham (Not Spam)
- ❌ Spam (Fraud / Phishing)

---

🛠️ Tech Stack

- Python 🐍
- Pandas
- NumPy
- Scikit-learn
- TF-IDF Vectorizer
- Naive Bayes Algorithm
- Streamlit (for web app)

---

⚙️ How It Works

1. Data Preprocessing
   
   - Convert text to lowercase
   - Remove special characters

2. Feature Extraction
   
   - Convert text into numerical form using TF-IDF

3. Model Training
   
   - Train using Multinomial Naive Bayes

4. Deployment
   
   - Model is saved using pickle
   - Integrated into a Streamlit web application

---

📊 Model Performance

- Accuracy: ~97%

---

🌐 Streamlit Web App

The project includes a web interface where users can:

- Enter an email/message
- Click on Check
- Get instant prediction

🧪 Example

Input:

Congratulations! You won a lottery

Output:

🚨 Spam

---

▶️ How to Run the Project

1. Install dependencies

pip install pandas numpy scikit-learn streamlit

---

2. Train the model

python main.py

(This will create "model.pkl" and "vectorizer.pkl")

---

3. Run the web app

streamlit run app.py

---

📁 Project Structure

Email-Fraud-Detection/
│── spam.csv
│── main.py
│── app.py
│── model.pkl
│── vectorizer.pkl
│── README.md

---

🚀 Future Improvements

- Add multiple ML models for comparison
- Improve UI design
- Deploy the app online
- Add real-time email filtering

---

💼 Resume Highlight

Developed an Email Fraud Detection system using NLP and Machine Learning with deployment using Streamlit.

---

👨‍💻 Author

Krishn