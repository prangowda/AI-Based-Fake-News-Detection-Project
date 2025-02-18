# 📰 AI-Based Fake News Detection  

## 📌 Overview  
This project is an **AI-powered Fake News Detection System** that classifies news articles as **real or fake** using **Natural Language Processing (NLP) and Machine Learning**.  
It is trained on a labeled dataset and can analyze **news headlines or full articles** to detect misinformation.  

---

## 🛠️ Technologies Used  

| **Technology**  | **Purpose**  |
|---------------|--------------|
| **Python**   | Main programming language |
| **Scikit-learn** | Machine learning model training |
| **NLTK** | Natural Language Processing (NLP) |
| **Pandas** | Data manipulation |
| **TfidfVectorizer** | Text feature extraction |
| **Flask** | Web-based API for detection |

---

## 📜 Features  
✅ **Detects fake news using NLP and ML**  
✅ **Pretrained machine learning model**  
✅ **Web-based detection using Flask API**  
✅ **Fast and lightweight classification**  
✅ **Can be extended as a Chrome extension or API**  

---

## 🚀 Installation & Setup  

### **1️⃣ Install Dependencies**  
Run the following command to install required libraries:  
```sh
pip install scikit-learn pandas nltk flask
```

### **2️⃣ Download Dataset**  
You can use the **Fake News Dataset** from Kaggle:  
🔗 [Download Fake News Dataset](https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset)  

Extract and place the dataset inside the `dataset/` directory.

---

## 📂 Project Structure  
```
/Fake_News_Detection
│── dataset/                     # Dataset folder
│── train_fake_news_model.py      # Model training script
│── fake_news_classifier.py       # Fake news detection script
│── app.py                        # Flask web app
│── model.pkl                     # Saved trained model
│── README.md                     # Documentation
```

---

## 🎯 How to Run the Project  

### **1️⃣ Train the Model**  
Run the following command to train the model:  
```sh
python train_fake_news_model.py
```
This will generate a saved model file **model.pkl**.

### **2️⃣ Test News Classification**  
Run the following command and enter a news article to classify it:  
```sh
python fake_news_classifier.py
```

### **3️⃣ Run Flask API**  
Start the Flask API by running:  
```sh
python app.py
```
The API will be available at **http://127.0.0.1:5000/**.

To test the API, send a **POST request** to the `/predict` endpoint with a JSON payload:  
```json
{
  "text": "Breaking News: Scientists find a cure for COVID-19."
}
```
Response:  
```json
{
  "prediction": "Real News ✅"
}
```

---

## 📂 Example Output  

| **News** | **Prediction** |
|-----------|--------------|
| ✅ "The government announces new lockdown measures." | **Real News** |
| ❌ "Aliens have landed in New York and started a McDonald's!" | **Fake News** |

---

## 🚀 Future Enhancements  
- ✅ **Deploy as a Chrome Extension**  
- ✅ **Add a web-based UI for users**  
- ✅ **Enhance dataset with more sources**  
- ✅ **Integrate with fact-checking APIs**  
