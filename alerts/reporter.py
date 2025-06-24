# alerts/reporter.py
def report_alert(iob_id, description, user, timestamp):
    print(f"[ALERTA] {iob_id} | {description} | Usuario: {user} | Hora: {timestamp}")
