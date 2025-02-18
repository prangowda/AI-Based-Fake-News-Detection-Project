from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load trained model
with open("model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

@app.route("/", methods=["GET"])
def home():
    return "Fake News Detection API is Running 🚀"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data["text"]
    prediction = model.predict([text])[0]
    result = "Real News ✅" if prediction == 1 else "Fake News ❌"
    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)
