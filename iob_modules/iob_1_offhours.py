# iob_modules/iob_1_offhours.py
from utils.loader import load_model
from alerts.reporter import report_alert
import datetime

model = load_model("models/iob_1_offhours.pkl")

def detect(event):
    timestamp = event.get('timestamp', datetime.datetime.utcnow().isoformat())
    user = event.get('user', 'unknown')
    hour = datetime.datetime.fromisoformat(timestamp).hour
    features = [event.get('user_id', 0), hour]
    prediction = model.predict([features])
    if prediction == 1:
        report_alert(
            iob_id="IOB-1",
            description="Acceso fuera de horario habitual",
            user=user,
            timestamp=timestamp
        )
