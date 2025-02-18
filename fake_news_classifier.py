import pickle

# Load trained model
with open("model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

def predict_news(news_text):
    prediction = model.predict([news_text])[0]
    return "Real News ✅" if prediction == 1 else "Fake News ❌"

# Example usage
if __name__ == "__main__":
    text = input("Enter news text: ")
    print("Prediction:", predict_news(text))
