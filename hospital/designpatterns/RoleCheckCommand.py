# The provided code utilizes the Command Pattern
# to encapsulate role-checking operations.
# The RoleCheckCommand abstract class defines
# a common interface with an execute method
# for checking if a user has a specific role.
# Concrete commands like IsAdminCommand,
# IsDoctorCommand, and IsPatientCommand
# extend this class, representing distinct
# role-checking tasks. This pattern decouples
# the client code, allowing for flexibility
# and easy extension. Clients can create
# instances of specific commands to check if a user is an admin, doctor, or patient, enabling parameterization of commands. The Command Pattern's modular design facilitates future enhancements and maintains a concise and adaptable structure.
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
