def role_check(user, group_name):
    return user.groups.filter(name=group_name).exists()


def is_admin(user):
    return role_check(user, 'ADMIN')


def is_doctor(user):
    return role_check(user, 'DOCTOR')


def is_patient(user):
    return role_check(user, 'PATIENT')