from Base import base_model


class Doctors(base_model):
    def __init__(self, full_name, specialization, phone_number, email, year_of_experience, doctor_id=None):
        self.full_name = full_name
        self.specialization = specialization
        self.phone_number = phone_number
        self.email = email
        self.year_of_experience = year_of_experience
