from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager


# User model
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email debe ser ingresado.')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    )

    document = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birth_date = models.DateField()
    email = models.EmailField(unique=True)
    cellphone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    discharge_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    nickname = models.CharField(max_length=50, unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['document', 'name', 'lastname', 'gender', 'birth_date', 'cellphone', 'address',
                       'nickname']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_superuser


# Employee model
class Employee(models.Model):
    POSITION = (
        ('PA', 'Personal administrativo'),
        ('PS', 'Personal de salud'),
    )

    employee_id = models.AutoField(primary_key=True)
    position = models.CharField(max_length=2, choices=POSITION)


# Assistant model
class Assistant(models.Model):
    assistant_id = models.AutoField(primary_key=True)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='assistant')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='assistant')


# Doctor model
class Doctor(models.Model):
    SPECIALITY = (
        ('ANE', 'Anestesiología'),
        ('CAR', 'Cardiología'),
        ('DER', 'Dermatología'),
        ('END', 'Endocrinología'),
        ('GAS', 'Gastroenterología'),
        ('GER', 'Geriatría'),
        ('GIN', 'Ginecología y Obstetricia'),
        ('HEM', 'Hematología'),
        ('INF', 'Infectología'),
        ('EME', 'Medicina de Emergencia'),
        ('FAM', 'Medicina Familiar y Comunitaria'),
        ('INT', 'Medicina Interna'),
        ('NEF', 'Nefrología'),
        ('NEU', 'Neumología'),
        ('NER', 'Neurología'),
        ('ONC', 'Oncología'),
        ('OFT', 'Oftalmología'),
        ('ORT', 'Ortopedia y Traumatología'),
        ('OTO', 'Otorrinolaringología'),
        ('PED', 'Pediatría'),
        ('PSQ', 'Psiquiatría'),
        ('RAD', 'Radiología'),
        ('REU', 'Reumatología'),
        ('URO', 'Urología')
    )

    doctor_id = models.AutoField(primary_key=True)
    speciality = models.CharField(max_length=3, choices=SPECIALITY)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='doctor')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_user')

    def create_user(self, email, password=None, **extra_fields):
        user = User.objects.create_user(email=email, password=password, **extra_fields)
        self.user = user
        self.save()


# Nurse model
class Nurse(models.Model):
    RANGE = (
        ('AE', 'Auxiliar de enfermería'),
        ('ER', 'Enfermería registrada'),
        ('EE', 'Enfermería especializada'),
        ('EJ', 'Enfermera jefa'),
        ('ED', 'Enfermera directora')
    )

    AREA = (
        ('EQ', 'Enfermería médico quirúrgica'),
        ('EP', 'Enfermería pediátrica'),
        ('EO', 'Enfermería obstétrica y ginecológica'),
        ('EI', 'Enfermería de cuidados intensivos'),
        ('ES', 'Enfermería de salud mental y psiquiátrica'),
        ('EC', 'Enfermería comunitaria')
    )

    nurse_id = models.AutoField(primary_key=True)
    range = models.CharField(max_length=2, choices=RANGE)
    area = models.CharField(max_length=2, choices=AREA)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='nurse')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='nurse_user')

    def create_user(self, email, password=None, **extra_fields):
        user = User.objects.create_user(email=email, password=password, **extra_fields)
        self.user = user
        self.save()


# Patient model
class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='patient')
    nurse_id = models.ForeignKey(Nurse, on_delete=models.CASCADE, related_name='patient')
    assistant_id = models.OneToOneField(Assistant, on_delete=models.CASCADE, related_name='patient')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_user')

    def create_user(self, email, password=None, **extra_fields):
        user = User.objects.create_user(email=email, password=password, **extra_fields)
        self.user = user
        self.save()


# Relative model
class Relative(models.Model):
    relative_id = models.AutoField(primary_key=True)
    patient_id = models.OneToOneField(Patient, on_delete=models.CASCADE, related_name='relative')
    assistant_id = models.OneToOneField(Assistant, on_delete=models.CASCADE, related_name='relative')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='relative_user')

    def create_user(self, email, password=None, **extra_fields):
        user = User.objects.create_user(email=email, password=password, **extra_fields)
        self.user = user
        self.save()


# Clinic history model

class ClinicHistory(models.Model):
    clinic_history_id = models.AutoField(primary_key=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    patient_id = models.OneToOneField(Patient, on_delete=models.CASCADE, related_name='clinic_history')


# Diagnostic model

class Diagnostic(models.Model):
    TREATMENT_EFFECTIVENESS = (
        ('A', 'Alta'),
        ('M', 'Media'),
        ('B', 'Baja'),
    )

    diagnostic_id = models.AutoField(primary_key=True)
    datetime = models.DateTimeField(auto_now_add=True)
    observations = models.CharField(max_length=4000)
    treatment_effectiveness = models.CharField(max_length=1, choices=TREATMENT_EFFECTIVENESS)
    next_visit = models.DateTimeField
    clinic_history_id = models.ForeignKey(ClinicHistory, on_delete=models.CASCADE, related_name='diagnostic')
    patient_id = models.OneToOneField(Patient, on_delete=models.CASCADE, related_name='diagnostic')
    doctor_id = models.OneToOneField(Doctor, on_delete=models.CASCADE, related_name='diagnostic')


# Vital signs

class VitalSigns(models.Model):
    vital_signs_id = models.AutoField(primary_key=True)
    oximetry = models.DecimalField(max_digits=3, decimal_places=2)
    respiratory_rate = models.PositiveIntegerField()
    heart_rate = models.PositiveIntegerField()
    temperature = models.DecimalField(max_digits=2, decimal_places=1)
    systolic_blood_pressure = models.DecimalField(max_digits=3, decimal_places=1)
    diastolic_blood_pressure = models.DecimalField(max_digits=2, decimal_places=1)
    blood_glucose = models.DecimalField(max_digits=3, decimal_places=2)
    datetime = models.DateTimeField(auto_now_add=True)
    clinic_history_id = models.ForeignKey(ClinicHistory, on_delete=models.CASCADE, related_name='vital_signs')
    patient_id = models.OneToOneField(Patient, on_delete=models.CASCADE, related_name='vital_signs')
    doctor_id = models.OneToOneField(Doctor, on_delete=models.CASCADE, related_name='vital_signs')


# Care_tips model

class CareTips(models.Model):
    care_tips_id = models.AutoField(primary_key=True)
    datetime = models.DateTimeField(auto_now_add=True)
    suggestion = models.CharField(max_length=4000)
    diagnostic_id = models.ForeignKey(Diagnostic, on_delete=models.CASCADE, related_name='care_tips')
    doctor_id = models.OneToOneField(Doctor, on_delete=models.CASCADE, related_name='care_tips')
    relative_id = models.OneToOneField(Relative, on_delete=models.CASCADE, related_name='care_tips')

# diagnostic = Diagnostic.objects.get(diagnostic_id=1)
# care_tips = diagnostic.care_tips.all()