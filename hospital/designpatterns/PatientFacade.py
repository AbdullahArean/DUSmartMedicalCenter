from django.shortcuts import render

from hospital import models


class PatientDetails:
    def __init__(self, user_id):
        self.patient = models.Patient.objects.get(user_id=user_id)

    def get_patient_dict(self):
        return {
            'patient': self.patient,
            'patientId': self.patient.id,
            'patientName': self.patient.get_name,
            'address': self.patient.address,
            'mobile': self.patient.mobile,
            'symptoms': self.patient.symptoms,
            'admitDate': self.patient.admitDate,
        }


class DischargeDetails:
    def __init__(self, patient_id):
        self.discharge_details = models.PatientDischargeDetails.objects.filter(patientId=patient_id).order_by('-id')[:1]

    def get_discharge_dict(self):
        if self.discharge_details:
            return {
                'is_discharged': True,
                'assignedDoctorName': self.discharge_details[0].assignedDoctorName,
                'releaseDate': self.discharge_details[0].releaseDate,
                'daySpent': self.discharge_details[0].daySpent,
                'medicineCost': self.discharge_details[0].medicineCost,
                'roomCharge': self.discharge_details[0].roomCharge,
                'doctorFee': self.discharge_details[0].doctorFee,
                'OtherCharge': self.discharge_details[0].OtherCharge,
                'total': self.discharge_details[0].total,
            }
        else:
            return {'is_discharged': False}


class PatientFacade:
    def __init__(self, request):
        self.request = request

    def get_patient_discharge_view(self):
        patient_details = PatientDetails(user_id=self.request.user.id)
        discharge_details = DischargeDetails(patient_id=patient_details.patient.id)

        patient_dict = patient_details.get_patient_dict()
        discharge_dict = discharge_details.get_discharge_dict()

        patient_dict.update(discharge_dict)  # Combine the dictionaries

        return render(self.request, 'hospital/patient_discharge.html', context=patient_dict)
