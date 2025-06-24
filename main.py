# main.py
from core.monitor import start_monitoring
from core.dispatcher import dispatch_event

def main():
    for event in start_monitoring():  # Stream de eventos
        dispatch_event(event)

if __name__ == "__main__":
    main()
