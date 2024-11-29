from Base import base_model

class Patients(base_model):
    def __init__(self, full_name, date_of_birth, gender, address, phone_number, email, patient_id=None):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.address = address
        self.phone_number = phone_number
        self.email = email
