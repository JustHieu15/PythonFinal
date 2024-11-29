from Patient import Patients
from Doctor import Doctors
from Appointment import Appointments

# Import Patients
# patient1 = Patients(full_name="NguyenHieu", date_of_birth="2001-07-15 01:00:00", gender="Male",
#                     address="HaNoi", phone_number="098765432", email="hieu@gmail.com")
# patient1_id = patient1.save()
# patient2 = Patients(full_name="NguyenKhang", date_of_birth="2002-07-15 01:00:00", gender="Male",
#                     address="HaNoi", phone_number="998765432", email="khang@gmail.com")
# patient2_id = patient2.save()
# patient3 = Patients(full_name="NguyenMinh", date_of_birth="2003-07-15 01:00:00", gender="Male",
#                     address="HaNoi", phone_number="898765432", email="minh@gmail.com")
# patient3_id = patient3.save()

# Import Doctors
# doctor1 = Doctors(full_name="XuanHung", specialization="NhaKhoa", phone_number="", email="xuanhung@gmail.com",
#                   year_of_experience=5)
# doctor1_id = doctor1.save()
#
# doctor2 = Doctors(full_name="XuanHung2", specialization="TimMach", phone_number="", email="xuanhung2@gmail.com",
#                   year_of_experience=6)
# doctor2_id = doctor2.save()
#
# doctor3 = Doctors(full_name="XuanHung3", specialization="KhoaNoi", phone_number="", email="xuanhung3@gmail.com",
#                   year_of_experience=3)
# doctor3_id = doctor3.save()
#
# doctor4 = Doctors(full_name="XuanHung4", specialization="TaiMuiHong", phone_number="", email="xuanhung4@gmail.com",
#                   year_of_experience=7)
# doctor4_id = doctor4.save()
#
# doctor5 = Doctors(full_name="XuanHung5", specialization="KhoaNhi", phone_number="", email="xuanhung5@gmail.com",
#                   year_of_experience=5)
# doctor5_id = doctor5.save()

# Import Appointments
appointment1 = Appointments(patient_id=1, doctor_id=2, appointment_date="2024-07-15 01:00:00", reason="Sick", status="")
appointment1_id = appointment1.save()

appointment2 = Appointments(patient_id=2, doctor_id=3, appointment_date="2024-08-15 01:00:00", reason="Sick", status="finished")
appointment2_id = appointment1.save()

appointment3 = Appointments(patient_id=3, doctor_id=4, appointment_date="2024-10-15 01:00:00", reason="Sick", status="")
appointment3_id = appointment1.save()


patients = Patients.findAll()
for patient in patients:
    print(patient)

doctors = Doctors.findAll()
for doctor in doctors:
    print(doctor)

appointments = Appointments.findAll()
for appointment in appointments:
    print(appointment)
