📧 Email Fraud Detection 🚨

📌 Project Overview

This project is a Machine Learning-based system that detects whether an email/message is Spam (Fraud) or Not Spam (Legitimate) using Natural Language Processing (NLP) techniques.

---

🎯 Objective

To build a model that can automatically classify emails into:

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

---

📂 Dataset

- SMS Spam Collection Dataset
- Contains labeled messages as spam or ham

---

⚙️ How It Works

1. Data Cleaning
   
   - Convert text to lowercase
   - Remove special characters

2. Feature Extraction
   
   - Convert text into numerical form using TF-IDF

3. Model Training
   
   - Train using Multinomial Naive Bayes

4. Prediction
   
   - Classify new emails as Spam or Not Spam

---

📊 Model Performance

- Accuracy: ~95% - 98%

---

▶️ How to Run

1. Install required libraries:

pip install pandas numpy scikit-learn

2. Run the program:

python main.py

---

🧪 Example

Input:

"Congratulations! You won a free lottery"

Output:

Spam

---

📁 Project Structure

Email-Fraud-Detection/
│── spam.csv
│── main.py
│── README.md

---

🚀 Future Improvements

- Build a Streamlit Web App
- Use advanced models (Logistic Regression, Random Forest)
- Add real-time email filtering

---

💼 Resume Highlight

Built an Email Fraud Detection system using NLP and Machine Learning achieving ~97% accuracy.

---

👨‍💻 Author
Krishn Kumar
