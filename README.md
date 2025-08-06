 # 🩺 WhatsApp Disease Predictor

A machine learning-powered WhatsApp chatbot that predicts possible diseases based on user-reported symptoms.  
Built with **FastAPI**, **Twilio**, and **Scikit-learn** for seamless healthcare assistance via WhatsApp.

---

## 📱 Features

- 🤖 Chatbot that interacts over WhatsApp  
- 🚑 Predicts disease from list of symptoms  
- ⚡ FastAPI backend for high-performance API  
- 🔎 Trained on symptom-disease dataset  
- 🛡️ Easy to deploy and extend

---

## 🛠️ Tech Stack

- Python 3.10+
- FastAPI
- Twilio WhatsApp API
- Scikit-learn
- Ngrok (for local testing)

---

## 🚀 How It Works

1. User sends symptoms to WhatsApp bot  
2. FastAPI receives message and predicts disease  
3. Bot replies with the most likely disease  

Example:
User: fever, headache, muscle pain
Bot: The predicted disease is: Dengue

yaml
Copy
Edit

---

## 💻 Getting Started

### Prerequisites

- Python installed
- Twilio account and WhatsApp sandbox setup
- Ngrok for tunneling (optional for local testing)

### Installation

1. Clone the repo
```bash
git clone https://github.com/Anam428/whatsapp-disease-predictor.git
cd whatsapp-disease-predictor
Create virtual environment

bash
Copy
Edit
python -m venv .venv
source .venv/bin/activate      # Mac/Linux
.venv\Scripts\activate         # Windows
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Train your model (optional if already trained)

Run FastAPI app

bash
Copy
Edit
uvicorn app:app --reload
Expose your app with ngrok (for Twilio to connect)

bash
Copy
Edit
ngrok http 8000
Set your Twilio webhook to:

arduino
Copy
Edit
https://<your-ngrok-url>/whatsapp
📄 Project Structure
bash
Copy
Edit
├── app.py                # FastAPI main app
├── model.pkl             # Trained ML model
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── .venv/                # Virtual environment (optional)
📝 Example Code Snippet
python
Copy
Edit
@app.post("/whatsapp")
async def whatsapp_reply(request: Request):
    form = await request.form()
    incoming_msg = form.get('Body')
    symptoms = incoming_msg.lower().split(',')
    symptoms = [symptom.strip() for symptom in symptoms]
    prediction = predict_disease(symptoms)
    return PlainTextResponse(f"The predicted disease is: {prediction}")
🐛 Status Callback URL (Optional)
You can also set Twilio Status Callback URL for delivery reports:

arduino
Copy
Edit
https://<your-ngrok-url>/status
🙋 Author
Anam Mansoor
GitHub

⭐ Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

📃 License
This project is licensed under the MIT License.

yaml
Copy
Edit

---

If you want, I can also **save this file for you as `README.md`** so you can directly upload or push it to your repo.  
Just say **"yes, save and give me the file"**.



