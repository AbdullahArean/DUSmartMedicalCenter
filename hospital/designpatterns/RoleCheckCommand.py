class RoleCheckCommand:
    def __init__(self, user, group_name):
        self.user = user
        self.group_name = group_name

    def execute(self):
        return self.user.groups.filter(name=self.group_name).exists()


class IsAdminCommand(RoleCheckCommand):
    def __init__(self, user):
        super().__init__(user, 'ADMIN')


class IsDoctorCommand(RoleCheckCommand):
    def __init__(self, user):
        super().__init__(user, 'DOCTOR')


class IsPatientCommand(RoleCheckCommand):
    def __init__(self, user):
        super().__init__(user, 'PATIENT')

# Example usage:
# user = # your user object
# is_admin = IsAdminCommand().execute
# is_doctor = IsDoctorCommand().execute
# is_patient = IsPatientCommand().execute
