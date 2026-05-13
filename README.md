# 📩 SMS & Email Spam Classifier

A machine learning powered web application that detects whether an SMS or email message is **spam or not spam (ham)** — built with Flask and a clean cyberpunk-themed UI.

---

## 🚀 Demo

> Paste any message → Click **Analyse** → Instantly see **SPAM** 🚨 or **NOT SPAM** ✅ with a confidence score.

---

## 📁 Project Structure

```
SMS-SPAM-PREDICTION/
├── app.py                   # Flask backend & prediction API
├── model.pkl                # Trained ML classification model
├── vectorizer.pkl           # Fitted TF-IDF / CountVectorizer
├── requirements.txt         # Python dependencies
├── spam.csv                 # Original dataset used for training
├── sms-spam-detection.ipynb # Model training notebook
└── templates/
    └── index.html           # Frontend UI
```

---

## 🧠 How It Works

1. User inputs a message on the web interface
2. The message is sent to the Flask `/predict` endpoint via a POST request
3. The `vectorizer.pkl` transforms the text into numerical features
4. The `model.pkl` classifies it as **spam (1)** or **ham (0)**
5. Result + confidence score is returned and displayed on screen

---

## 🛠️ Tech Stack

| Layer      | Technology                        |
|------------|-----------------------------------|
| Frontend   | HTML, CSS, Vanilla JavaScript     |
| Backend    | Python, Flask                     |
| ML Model   | Scikit-learn                      |
| Vectorizer | TF-IDF / CountVectorizer          |
| Dataset    | SMS Spam Collection Dataset       |

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/SMS-SPAM-PREDICTION.git
cd SMS-SPAM-PREDICTION
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Flask app

```bash
python app.py
```

### 4. Open in browser

```
http://127.0.0.1:5000
```

---

## 📦 Requirements

```
flask>=2.3.0
scikit-learn>=1.3.0
numpy>=1.24.0
```

> Install all at once: `pip install -r requirements.txt`

---

## 🤖 Model Details

- **Algorithm:** Naive Bayes / Logistic Regression / Random Forest *(update as per your model)*
- **Vectorization:** TF-IDF Vectorizer
- **Training Data:** SMS Spam Collection Dataset (`spam.csv`)
- **Classes:**
  - `0` → Ham (Not Spam)
  - `1` → Spam

---

## 📊 Dataset

The model was trained on the **SMS Spam Collection Dataset**, which contains 5,574 SMS messages labelled as `ham` or `spam`.

| Label | Count |
|-------|-------|
| Ham   | 4,827 |
| Spam  | 747   |

---

## 🌐 API Reference

### `POST /predict`

**Request Body (JSON):**
```json
{
  "message": "Congratulations! You've won a free iPhone. Click here to claim."
}
```

**Response (JSON):**
```json
{
  "label": "spam",
  "confidence": 98.7,
  "message": "Congratulations! You've won a free iPhone. Click here to claim."
}
```

| Field        | Type    | Description                          |
|--------------|---------|--------------------------------------|
| `label`      | string  | `"spam"` or `"ham"`                  |
| `confidence` | float   | Confidence percentage (if available) |
| `message`    | string  | The original input message           |

---

## ✨ Features

- ⚡ Real-time spam detection
- 📊 Confidence score with animated progress bar
- 🎨 Cyberpunk dark-theme UI
- ⌨️ Supports `Ctrl + Enter` to submit
- 📱 Responsive design for mobile & desktop
- 🔄 Clear & reset functionality

---

## 🖼️ Screenshots

> <img width="1311" height="579" alt="image" src="https://github.com/user-attachments/assets/c78522be-ff2b-4b93-832f-0e86b3a8b682" />


---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

**Akhilesh**
- GitHub: [@your-username](https://github.com/your-username)
- LinkedIn: [your-linkedin](https://linkedin.com/in/your-profile)

---

> ⭐ If you found this project helpful, give it a star on GitHub!
