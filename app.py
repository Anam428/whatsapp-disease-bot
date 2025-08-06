from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
import joblib
import difflib
from sklearn.preprocessing import MultiLabelBinarizer

# Load model and symptom list
model = joblib.load("model/disease_model.pkl")
symptom_list = joblib.load("model/symptom_list.pkl")

# Binarizer setup
mlb = MultiLabelBinarizer(classes=symptom_list)
mlb.fit([])

app = FastAPI()

@app.post("/whatsapp")
async def whatsapp_bot(request: Request):
    form = await request.form()
    incoming_msg = form.get("Body", "").strip().lower()

    # Split message into words (spaces & commas)
    raw_tokens = [token.strip() for token in incoming_msg.replace(",", " ").split()]

    # Fuzzy match tokens to known symptoms
    matched = []
    for token in raw_tokens:
        close = difflib.get_close_matches(token, symptom_list, n=1, cutoff=0.7)
        if close:
            matched.append(close[0])

    if not matched:
        return PlainTextResponse("No matching symptoms found. Please rephrase and try again.")

    # Vectorize and predict
    X_input = mlb.transform([matched])
    prediction = model.predict(X_input)[0]

    return PlainTextResponse(f"The predicted disease is: {prediction}")
