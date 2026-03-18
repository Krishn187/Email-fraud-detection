import pandas as pd
import numpy as np
import re

# Load dataset
df = pd.read_csv("spam.csv", encoding='latin-1')

# Keep only needed columns
df = df[['v1', 'v2']]
df.columns = ['label', 'message']

# Convert labels to 0 and 1
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Remove duplicates
df.drop_duplicates(inplace=True)

# Text cleaning
def clean_text(text):
    text = text.lower()
    text = re.sub('[^a-zA-Z]', ' ', text)
    return text

df['message'] = df['message'].apply(clean_text)

# Feature extraction
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(max_features=3000)
X = tfidf.fit_transform(df['message']).toarray()
y = df['label']

# Train-test split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Train model
from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()
model.fit(X_train, y_train)

# Accuracy
from sklearn.metrics import accuracy_score

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Test function
def predict_email(text):
    text = clean_text(text)
    vector = tfidf.transform([text]).toarray()
    prediction = model.predict(vector)
    return "Spam" if prediction[0] == 1 else "Not Spam"

# Try examples
# print(predict_email("You won a lottery prize! Claim now"))
# print(predict_email("Hey, are we meeting today?"))
import pickle

pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(tfidf, open("vectorizer.pkl", "wb"))