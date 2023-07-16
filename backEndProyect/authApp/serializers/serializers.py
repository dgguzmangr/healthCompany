from rest_framework import serializers
from authApp.models.models import *

# User serializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id',
                  'document',
                  'name',
                  'lastname',
                  'gender',
                  'birth_date',
                  'email',
                  'cellphone',
                  'address',
                  'discharge_date',
                  'is_active',
                  'nickname']
        read_only_fields = ['id', 'discharge_data']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['employee_id',
                  'position']
        read_only_fields = ['employee_id']


class AssistantSerializer(serializers.ModelSerializer):
    employee_id = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Assistant
        fields = ['assistant_id',
                  'employee_id',
                  'user']
        read_only_fields = ['assistant_id']

    def create(self, validated_data):
        employee_id = validated_data.pop('employee_id')
        user = validated_data.pop('user')
        assistant = Assistant.objects.create(employee_id=employee_id,
                                             user_id=user.id,
                                             **validated_data)
        return assistant


class DoctorSerializer(serializers.ModelSerializer):
    employee_id = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Doctor
        fields = ['doctor_id',
                  'speciality',
                  'employee_id',
                  'user']
        read_only_fields = ['doctor_id']

    def create(self, validated_data):
        employee_id = validated_data.pop('employee_id')
        user = validated_data.pop('user')
        doctor = Doctor.objects.create(employee_id=employee_id,
                                       user_id=user.id,
                                       **validated_data)
        return doctor


class NurseSerializer(serializers.ModelSerializer):
    employee_id = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Nurse
        fields = ['nurse_id',
                  'range',
                  'area',
                  'employee_id',
                  'user']
        read_only_fields = ['nurse_id']

    def create(self, validated_data):
        employee_id = validated_data.pop('employee_id')
        user = validated_data.pop('user')
        nurse = Nurse.objects.create(employee_id=employee_id,
                                     user_id=user.id,
                                     **validated_data)
        return nurse


class PatientSerializer(serializers.ModelSerializer):
    doctor_id = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())
    nurse_id = serializers.PrimaryKeyRelatedField(queryset=Nurse.objects.all())
    assistant_id = serializers.PrimaryKeyRelatedField(queryset=Assistant.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Patient
        fields = ['patient_id',
                  'doctor_id',
                  'nurse_id',
                  'assistant_id',
                  'user']
        read_only_fields = ['patient_id']

    def create(self, validated_data):
        doctor_id = validated_data.pop('doctor_id')
        nurse_id = validated_data.pop('nurse_id')
        assistant_id = validated_data.pop('assistant_id')
        user = validated_data.pop('user')
        patient = Patient.objects.create(doctor_id=doctor_id,
                                         nurse_id=nurse_id,
                                         assistant_id=assistant_id,
                                         user_id=user.id,
                                         **validated_data)
        return patient


class RelativeSerializer(serializers.ModelSerializer):
    patient_id = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())
    assistant_id = serializers.PrimaryKeyRelatedField(queryset=Assistant.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Relative
        fields = ['relative_id',
                  'patient_id',
                  'assistant_id',
                  'user']
        read_only_fields = ['relative_id']

    def create(self, validated_data):
        patient_id = validated_data.pop('patient_id')
        assistant_id = validated_data.pop('assistant_id')
        user = validated_data.pop('user')
        relative = Relative.objects.create(patient_id=patient_id,
                                           assistant_id=assistant_id,
                                           user_id=user.id,
                                           **validated_data)
        return relative


class ClinicHistorySerializer(serializers.ModelSerializer):
    patient_id = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())

    class Meta:
        model = ClinicHistory
        fields = ['clinic_history_id',
                  'creation_date',
                  'patient_id']
        read_only_fields = ['clinic_history_id']

    def create(self, validated_data):
        patient_id = validated_data.pop('patient_id')
        clinic_history = ClinicHistory.objects.create(patient_id=patient_id,
                                                      **validated_data)
        return clinic_history


class DiagnosticSerializer(serializers.ModelSerializer):
    clinic_history_id = serializers.PrimaryKeyRelatedField(queryset=ClinicHistory.objects.all())
    patient_id = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())
    doctor_id = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())

    class Meta:
        model = Diagnostic
        fields = ['diagnostic_id',
                  'datetime',
                  'observations',
                  'treatment_effectiveness',
                  'next_visit',
                  'clinic_history_id',
                  'patient_id',
                  'doctor_id']
        read_only_fields = ['diagnostic_id']

    def create(self, validated_data):
        clinic_history_id = validated_data.pop('clinic_history_id')
        patient_id = validated_data.pop('patient_id')
        doctor_id = validated_data.pop('doctor_id')
        diagnostic = Diagnostic.objects.create(clinic_history_id=clinic_history_id,
                                               patient_id=patient_id,
                                               doctor_id=doctor_id,
                                               **validated_data)
        return diagnostic


class VitalSignsSerializer(serializers.ModelSerializer):
    clinic_history_id = serializers.PrimaryKeyRelatedField(queryset=ClinicHistory.objects.all())
    patient_id = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())
    doctor_id = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())

    class Meta:
        model = VitalSigns
        fields = ['vital_signs_id',
                  'oximetry',
                  'respiratory_rate',
                  'heart_rate',
                  'temperature',
                  'systolic_blood_pressure',
                  'diastolic_blood_pressure',
                  'blood_glucose',
                  'datetime',
                  'clinic_history_id',
                  'patient_id',
                  'doctor_id']
        read_only_fields = ['vital_signs_id']

    def create(self, validated_data):
        clinic_history_id = validated_data.pop('clinic_history_id')
        patient_id = validated_data.pop('patient_id')
        doctor_id = validated_data.pop('doctor_id')
        vital_signs = VitalSigns.objects.create(clinic_history_id=clinic_history_id,
                                                patient_id=patient_id,
                                                doctor_id=doctor_id,
                                                **validated_data)
        return vital_signs


class CareTipsSerializer(serializers.ModelSerializer):
    diagnostic_id = serializers.PrimaryKeyRelatedField(queryset=Diagnostic.objects.all())
    doctor_id = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())
    relative_id = serializers.PrimaryKeyRelatedField(queryset=Relative.objects.all())

    class Meta:
        model = CareTips
        fields = ['care_tips_id',
                  'datetime',
                  'suggestion',
                  'diagnostic_id',
                  'doctor_id',
                  'relative_id']
        read_only_fields = ['care_tips_id']

    def create(self, validated_data):
        diagnostic_id = validated_data.pop('diagnostic_id')
        doctor_id = validated_data.pop('doctor_id')
        relative_id = validated_data.pop('relative_id')
        care_tips = CareTips.objects.create(diagnostic_id=diagnostic_id,
                                            doctor_id=doctor_id,
                                            relative_id=relative_id,
                                            **validated_data)
        return care_tips
