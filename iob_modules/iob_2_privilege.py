# iob_modules/iob_2_privilege.py
from utils.loader import load_model
from alerts.reporter import report_alert
import datetime

model = load_model("models/iob_2_privilege.pkl")

def detect(event):
    # Similar structure for privilege escalation
    prediction = model.predict([[]])
    if prediction == 1:
        report_alert(
            iob_id="IOB-2",
            description="Escalada de privilegios detectada",
            user=event.get('user', 'unknown'),
            timestamp=event.get('timestamp', datetime.datetime.utcnow().isoformat())
        )
