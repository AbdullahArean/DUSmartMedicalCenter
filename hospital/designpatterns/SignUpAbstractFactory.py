# from abc import ABC, abstractmethod
# from django.contrib.auth.models import Group
# from django.http import HttpResponseRedirect
# from hospital import forms
# from django.shortcuts import render
#
#
# class SignupFactory(ABC):
#     @abstractmethod
#     def create_user_form(self, data):
#         pass
#
#     @abstractmethod
#     def create_profile_form(self, data, files=None):
#         pass
#
#     @abstractmethod
#     def create_group_name(self):
#         pass
#
#     @abstractmethod
#     def create_redirect_url(self):
#         pass
#
#     @abstractmethod
#     def get_template_name(self):
#         pass
#
#     def signup_view(self, request):
#         if isinstance(factory, DoctorSignupFactory):
#             user_form = forms.DoctorUserForm(request.POST)
#             profile_form = forms.DoctorForm(request.POST, request.FILES)
#         elif isinstance(factory, PatientSignupFactory):
#             user_form = forms.PatientUserForm(request.POST)
#             profile_form = forms.PatientForm(request.POST, request.FILES)
#         else:
#             # Handle other cases or raise an exception as needed
#             raise NotImplementedError("Unsupported SignupFactory type")
#         if user_form.is_valid() and profile_form.is_valid():
#                 user = user_form.save()
#                 user.set_password(user.password)
#                 user.save()
#
#                 profile = profile_form.save(commit=False)
#                 profile.user = user
#
#                 if hasattr(profile, 'assigned_doctor_id'):
#                     profile.assigned_doctor_id = request.POST.get('assigned_doctor_id')
#
#                 profile.save()
#
#                 group_name = self.create_group_name()
#                 my_group = Group.objects.get_or_create(name=group_name)
#                 my_group[0].user_set.add(user)
#
#                 return HttpResponseRedirect(self.create_redirect_url())
#
#         user_form = self.create_user_form(None)
#         profile_form = self.create_profile_form(None)
#         my_dict = {'userForm': user_form, 'profileForm': profile_form}
#         return render(request, self.get_template_name(), context=my_dict)
#
#
# class DoctorSignupFactory(SignupFactory):
#     def create_user_form(self, data):
#         return forms.DoctorUserForm(data)
#
#     def create_profile_form(self, data, files=None):
#         return forms.DoctorForm(data, files)
#
#     def create_group_name(self):
#         return 'DOCTOR'
#
#     def create_redirect_url(self):
#         return 'doctorlogin'
#
#     def get_template_name(self):
#         return 'hospital/doctorsignup.html'
#
#
# class PatientSignupFactory(SignupFactory):
#     def create_user_form(self, data):
#         return forms.PatientUserForm(data)
#
#     def create_profile_form(self, data, files=None):
#         return forms.PatientForm(data, files)
#
#     def create_group_name(self):
#         return 'PATIENT'
#
#     def create_redirect_url(self):
#         return 'patientlogin'
#
#     def get_template_name(self):
#         return 'hospital/patientsignup.html'
#
