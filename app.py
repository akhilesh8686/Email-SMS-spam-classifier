from flask import Flask, render_template, request, jsonify
import pickle
import os

app = Flask(__name__)

# ── Load model & vectorizer ──────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "model.pkl"), "rb") as f:
    model = pickle.load(f)

with open(os.path.join(BASE_DIR, "vectorizer.pkl"), "rb") as f:
    vectorizer = pickle.load(f)

# ── Routes ───────────────────────────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    message = data.get("message", "").strip()

    if not message:
        return jsonify({"error": "Please enter a message."}), 400

    # Transform & predict
    features = vectorizer.transform([message])
    prediction = model.predict(features)[0]

    # Try to get confidence probability (works if model supports predict_proba)
    confidence = None
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(features)[0]
        confidence = round(float(max(proba)) * 100, 1)

    label = "spam" if str(prediction) in ("1", "spam", "SPAM") else "ham"

    return jsonify({
        "label": label,
        "confidence": confidence,
        "message": message
    })


if __name__ == "__main__":
    app.run(debug=True)