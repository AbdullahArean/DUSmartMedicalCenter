from django.db import models
from django.contrib.auth.models import User

from hospital.designpatterns.DepartmentSingletonStrategy import DepartmentStrategy
from hospital.designpatterns.DocumentBaseFactory import DocumentBaseFactory


class PersonStrategyFactory:
    @staticmethod
    def create_person(user_type, *args, **kwargs):
        if user_type == 'Doctor':
            return Doctor(*args, **kwargs)
        elif user_type == 'Patient':
            return Patient(*args, **kwargs)


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/', null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=True)
    status = models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    # an abstract base class and is not meant to be instantiated or used on its own to create database tables
    class Meta:
        abstract = True


class Doctor(Person):
    department = models.CharField(max_length=50, choices=DepartmentStrategy.get_choices(), default='Cardiologist')

    def __str__(self):
        return "{} ({})".format(self.get_name, self.department)


class Patient(Person):
    symptoms = models.CharField(max_length=100, null=False)
    assignedDoctorId = models.PositiveIntegerField(null=True)
    admitDate = models.DateField(auto_now=True)

    def __str__(self):
        return "{} ({})".format(self.get_name, self.symptoms)


class Appointment(DocumentBaseFactory):
    common_variable = "Appointment"

    patientId = models.PositiveIntegerField(null=True)
    doctorId = models.PositiveIntegerField(null=True)
    patientName = models.CharField(max_length=40, null=True)
    doctorName = models.CharField(max_length=40, null=True)
    appointmentDate = models.DateField(auto_now=True)
    description = models.TextField(max_length=500)
    status = models.BooleanField(default=False)


class PatientDischargeDetails(DocumentBaseFactory):
    common_variable = "PatientDischargeDetails"

    patientId = models.PositiveIntegerField(null=True)
    patientName = models.CharField(max_length=40)
    assignedDoctorName = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=True)
    symptoms = models.CharField(max_length=100, null=True)

    admitDate = models.DateField(null=False)
    releaseDate = models.DateField(null=False)
    daySpent = models.PositiveIntegerField(null=False)

    roomCharge = models.PositiveIntegerField(null=False)
    medicineCost = models.PositiveIntegerField(null=False)
    doctorFee = models.PositiveIntegerField(null=False)
    OtherCharge = models.PositiveIntegerField(null=False)
    total = models.PositiveIntegerField(null=False)
