from Base import base_model


class Appointments(base_model):
    def __init__(self, patient_id, doctor_id, appointment_date, reason, status, appointment_id=None):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_date = appointment_date
        self.reason = reason
        self.status = status
