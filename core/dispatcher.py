# core/dispatcher.py
from iob_modules import iob_1_offhours, iob_2_privilege, iob_4_massaccess

def dispatch_event(event):
    iob_1_offhours.detect(event)
    iob_2_privilege.detect(event)
    iob_4_massaccess.detect(event)
