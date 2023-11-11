# singleton.py

from hospital.forms import ContactusForm
from django.core.mail import send_mail
from django.conf import settings
from hospital.forms import PatientAppointmentForm
from hospital.models import Patient, Doctor, User
from django.http import HttpResponseRedirect


class AppointmentSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(AppointmentSingleton, cls).__new__(cls, *args, **kwargs)
            cls._instance.appointment_form = PatientAppointmentForm()  # Add this line to initialize the appointment_form attribute
        return cls._instance

    def handle_appointment_booking(self, request):
        form = self.appointment_form  # Use the appointment_form attribute

        patient = Patient.objects.get(user_id=request.user.id)  # For the patient profile picture in the sidebar
        message = None
        mydict = {'appointmentForm': form, 'patient': patient, 'message': message}

        if request.method == 'POST':
            form = PatientAppointmentForm(request.POST)
            if form.is_valid():
                desc = request.POST.get('description')
                doctor = Doctor.objects.get(user_id=request.POST.get('doctorId'))

                appointment = form.save(commit=False)
                appointment.doctorId = request.POST.get('doctorId')
                appointment.patientId = request.user.id
                appointment.doctorName = User.objects.get(id=request.POST.get('doctorId')).first_name
                appointment.patientName = request.user.first_name
                appointment.status = False
                appointment.save()
                return HttpResponseRedirect('patient-view-appointment')

        return mydict


class ContactUsSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ContactUsSingleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def handle_contact_form(self, request):
        form = ContactusForm()

        if request.method == 'POST':
            form = ContactusForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['Email']
                name = form.cleaned_data['Name']
                message = form.cleaned_data['Message']
                send_mail(str(name) + ' || ' + str(email), message, settings.EMAIL_HOST_USER,
                          settings.EMAIL_RECEIVING_USER, fail_silently=False)
                return True  # Indicate success

        return False  # Indicate failure
