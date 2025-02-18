import pandas as pd
import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.pipeline import Pipeline
import pickle

# Load dataset
df_fake = pd.read_csv("dataset/Fake.csv")
df_real = pd.read_csv("dataset/True.csv")

df_fake["label"] = 0  # Fake News
df_real["label"] = 1  # Real News

# Combine both datasets
df = pd.concat([df_fake, df_real])
df = df.sample(frac=1).reset_index(drop=True)  # Shuffle data

# Preprocessing function
def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

df["text"] = df["text"].apply(clean_text)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(df["text"], df["label"], test_size=0.2, random_state=42)

# Create text classification pipeline
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(stop_words="english", max_df=0.7)),
    ("classifier", PassiveAggressiveClassifier(max_iter=50))
])

# Train model
pipeline.fit(X_train, y_train)

# Save model
with open("model.pkl", "wb") as model_file:
    pickle.dump(pipeline, model_file)

print("✅ Model training completed and saved!")
