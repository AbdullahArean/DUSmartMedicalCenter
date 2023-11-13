
# Singleton Pattern:
# SingletonMeta Metaclass:
# A metaclass named SingletonMeta is defined to implement the Singleton pattern.
# The metaclass overrides the __call__ method, which is called when an instance of a class is created.
# It maintains a dictionary, _instances, to keep track of instances created for each class.
# DepartmentStrategy Class with Singleton Metaclass:
# The DepartmentStrategy class is declared with the metaclass=SingletonMeta argument.
# This enforces that only one instance of the DepartmentStrategy class can exist.
# Usage of Singleton in Subclasses:
# Subclasses, such as CardiologistDepartment and others, automatically inherit the Singleton behavior from the DepartmentStrategy class.
# The Singleton pattern ensures that creating multiple instances of the subclasses will always return the same instance of the class.
# Singleton Usage in populate_departments Method:
# The populate_departments method, responsible for populating the departments list, is a class method.
# It is called on the class itself (DepartmentStrategy), and the Singleton pattern ensures that it operates on a single shared instance.
# Strategy Pattern:
# DepartmentStrategy as Strategy Base:
# The DepartmentStrategy class serves as the base class for the Strategy pattern.
# It defines the common interface and behavior for all concrete strategy classes.
# Concrete Strategy Classes:
# Subclasses like CardiologistDepartment, DermatologistsDepartment, etc., represent concrete strategies.
# Each concrete strategy provides its own implementation for the __init__ method, initializing the name and description.
# Dynamic Population of Departments:
# The populate_departments method in DepartmentStrategy dynamically populates the departments list with the names and descriptions of the concrete strategy classes.
# This dynamic population allows for the addition of new strategy classes without modifying the base class.
# get_choices Method:
# The get_choices method in DepartmentStrategy is part of the strategy interface.
# It provides a common method for obtaining the available choices, which are the names and descriptions of the concrete strategy classes.
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class DepartmentStrategy(metaclass=SingletonMeta):
    departments = []

    def __init__(self, name, description):
        self.name = name
        self.description = description
        DepartmentStrategy.departments.append((self.name, self.description))

    def __str__(self):
        return self.name

    @classmethod
    def get_choices(cls):
        if not cls.departments:
            cls.populate_departments()
        return cls.departments

    @classmethod
    def populate_departments(cls):
        for subclass in cls.__subclasses__():
            subclass_name = subclass().__str__()
            subclass_description = subclass().__dict__["description"]
            DepartmentStrategy.departments.append((subclass_name, subclass_description))


class CardiologistDepartment(DepartmentStrategy):
    def __init__(self):
        super().__init__('Cardiologist', 'Specializes in heart-related issues')


class DermatologistsDepartment(DepartmentStrategy):
    def __init__(self):
        super().__init__('Dermatologists', 'Specializes in skin-related issues')


class EmergencyMedicineDepartment(DepartmentStrategy):
    def __init__(self):
        super().__init__('Emergency Medicine Specialists', 'Handles emergency medical cases')


class AllergistsImmunologistsDepartment(DepartmentStrategy):
    def __init__(self):
        super().__init__('Allergists/Immunologists', 'Specializes in allergies and immunology')


class AnesthesiologistsDepartment(DepartmentStrategy):
    def __init__(self):
        super().__init__('Anesthesiologists', 'Administers anesthesia during medical procedures')


class ColonRectalSurgeonsDepartment(DepartmentStrategy):
    def __init__(self):
        super().__init__('Colon and Rectal Surgeons', 'Specializes in colorectal surgery')
