# iob_modules/iob_4_massaccess.py
from utils.loader import load_model
from alerts.reporter import report_alert
import datetime

model = load_model("models/iob_4_massaccess.onnx")

def detect(event):
    prediction = False  # ONNX demo placeholder
    if prediction:
        report_alert(
            iob_id="IOB-4",
            description="Acceso masivo a ficheros detectado",
            user=event.get('user', 'unknown'),
            timestamp=event.get('timestamp', datetime.datetime.utcnow().isoformat())
        )
