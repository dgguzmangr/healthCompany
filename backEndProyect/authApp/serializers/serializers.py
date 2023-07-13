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
    employee = EmployeeSerializer()
    user = UserSerializer()

    class Meta:
        model = Assistant
        fields = ['assistant_id',
                  'employee_id',
                  'user']
        read_only_fields = ['assistant_id',
                            'employee_id',
                            'user']

    def create(self, validated_data):
        employee_data = validated_data.pop('employee')
        employee_instance = Employee.objects.create(**employee_data)
        assistant_instance = Assistant.objects.create(employee_id=employee_instance, **validated_data)
        return assistant_instance

    def to_representation(self, obj):
        assistant = Assistant.objects.get(assistant_id=obj.assistant_id)
        employee = Employee.objects.get(employee_id=assistant.employee_id)
        user = User.objects.get(user_id=assistant.user_id)
        return {'assistant_id': assistant.assistant_id,
                'employee': {
                    'employee_id': employee.employee_id,
                    'position': employee.position
                },
                'user': {
                    'user_id': user.user_id,
                    'document': user.document,
                    'name': user.name,
                    'lastname': user.lastname,
                    'gender': user.gender,
                    'birth_date': user.birth_date,
                    'email': user.email,
                    'cellphone': user.cellphone,
                    'address': user.address,
                    'discharge_data': user.discharge_data,
                    'is_active': user.is_active,
                    'nickname': user.nickname
                    }
                }


class DoctorSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()
    user = UserSerializer()

    class Meta:
        model = Doctor
        fields = ['doctor_id',
                  'speciality',
                  'employee_id',
                  'user']

    def create(self, validated_data):
        employee_data = validated_data.pop('employee')
        employee_instance = Employee.objects.create(**employee_data)
        doctor_instance = Doctor.objects.create(employee_id=employee_instance, **validated_data)
        return doctor_instance

    def to_representation(self, obj):
        doctor = Doctor.objects.get(doctor_id=obj.doctor_id)
        employee = Employee.objects.get(employe_id=doctor.employee_id.doctor_id)
        user = User.objects.get(user_id=doctor.user_id)
        return {'doctor_id': doctor.doctor_id,
                'speciality': doctor.speciality,
                'employee': {
                    'employee_id': employee.employee_id,
                    'position': employee.position
                },
                'user': {
                    'user_id': user.user_id,
                    'document': user.document,
                    'name': user.name,
                    'lastname': user.lastname,
                    'gender': user.gender,
                    'birth_date': user.birth_date,
                    'email': user.email,
                    'cellphone': user.cellphone,
                    'address': user.address,
                    'discharge_data': user.discharge_data,
                    'is_active': user.is_active,
                    'nickname': user.nickname
                }
            }


class NurseSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()
    user = UserSerializer()

    class Meta:
        model = Doctor
        fields = ['nurse_id',
                  'range',
                  'area',
                  'employee_id',
                  'user']

    def create(self, validated_data):
        employee_data = validated_data.pop('employee')
        employee_instance = Employee.objects.create(**employee_data)
        nurse_instance = Nurse.objects.create(employee_id=employee_instance, **validated_data)
        return nurse_instance

    def to_representation(self, obj):
        nurse = Nurse.objects.get(nurse_id=obj.nurse_id)
        employee = Employee.objects.get(employe_id=nurse.employee_id.nurse_id)
        user = User.objects.get(user_id=nurse.user_id)
        return {'nurse_id': nurse.nurse_id,
                'range': nurse.range,
                'area': nurse.area,
                'employee': {
                    'employee_id': employee.employee_id,
                    'position': employee.position
                },
                'user': {
                    'user_id': user.user_id,
                    'document': user.document,
                    'name': user.name,
                    'lastname': user.lastname,
                    'gender': user.gender,
                    'birth_date': user.birth_date,
                    'email': user.email,
                    'cellphone': user.cellphone,
                    'address': user.address,
                    'discharge_data': user.discharge_data,
                    'is_active': user.is_active,
                    'nickname': user.nickname
                }
            }


class PatientSerializar(serializers.ModelSerializer):
    doctor = DoctorSerializer()
    nurse = NurseSerializer()
    assistant = AssistantSerializer()
    user = UserSerializer()
    employee = EmployeeSerializer()

    class Meta:
        model = Patient
        fields = ['patient_id',
                  'doctor_id',
                  'nurse_id',
                  'assistant_id'
                  'user']

    def create(self, validated_data):
        doctor_data = validated_data.pop('doctor')
        doctor_instance = Doctor.objects.create(**doctor_data)
        nurse_data = validated_data.pop('nurse')
        nurse_instance = Nurse.objects.create(**nurse_data)
        assistant_data = validated_data.pop('assistant')
        assistant_instance = Assistant.objects.create(**assistant_data)
        patient_instance = Patient.objects.create(doctor_id=doctor_instance,
                                                  nurse_id=nurse_instance,
                                                  assistant_id=assistant_instance,
                                                  **validated_data)
        return patient_instance

    def to_representation(self, obj):
        patient = Patient.objects.get(patient_id=obj.patient_id)
        doctor = Doctor.objects.get(doctor_id=patient.doctor_id)
        nurse = Nurse.objects.get(nurse_id=patient.nurse_id)
        assistant = Assistant.objects.get(assistant_id=patient.assistant_id)
        user = User.objects.get(user_id=patient.user_id)
        employee = Employee.objects.get(employee_id=patient.employee_id)
        return {
            'patient_id': patient.patient_id,
            'doctor': {
                'doctor_id': doctor.doctor_id,
                'speciality': doctor.speciality,
                'employee': {
                    'employee_id': employee.employee_id,
                    'position': employee.position
                },
            },
            'nurse': {
                'nurse_id': nurse.nurse_id,
                'range': nurse.range,
                'area': nurse.area,
                'employee': {
                    'employee_id': employee.employee_id,
                    'position': employee.position
                    }
            },
            'assistant': {
                'assistant_id': assistant.assistant_id,
                'employee': {
                    'employee_id': employee.employee_id,
                    'position': employee.position
                }
            },
            'user': {
                'user_id': user.user_id,
                'document': user.document,
                'name': user.name,
                'lastname': user.lastname,
                'gender': user.gender,
                'birth_date': user.birth_date,
                'email': user.email,
                'cellphone': user.cellphone,
                'address': user.address,
                'discharge_data': user.discharge_data,
                'is_active': user.is_active,
                'nickname': user.nickname
            }
        }


class RelativeSerializer(serializers.ModelSerializer):
    patient = PatientSerializar()
    assistant = AssistantSerializer()
    user = UserSerializer()

    class Meta:
        model = Relative
        fields = ['relative_id',
                  'patient_id',
                  'assistant_id'
                  'user']

    def create(self, validated_data):
        patient_data = validated_data.pop('patient')
        patient_instance = Patient.objects.create(**patient_data)
        assistant_data = validated_data.pop('assistant')
        assistant_instance = Assistant.objects.create(**assistant_data)
        relative_instance = Relative.objects.create(patient_id=patient_instance,
                                                    assistant_id=assistant_instance,
                                                    **validated_data)
        return relative_instance

    def to_representation(self, obj):
        relative = Relative.objects.get(relative_id=obj.relative_id)
        patient = Patient.objects.get(patient_id=relative.patient_id)
        assistant = Assistant.objects.get(assistant_id=relative.assistant_id)
        user = User.objects.get(user_id=relative.user_id)
        employee= Employee.objects.get(employee_id=relative.employee_id)
        return {
            'relative_id': relative.relative_id,
            'patient': {
                'patient_id': patient.patient_id,
            },
            'assistant': {
                'assistant_id': assistant.assistant_id,
                'employee': {
                    'employee_id': employee.employee_id,
                    'position': employee.position
                }
            },
            'user': {
                'user_id': user.user_id,
                'document': user.document,
                'name': user.name,
                'lastname': user.lastname,
                'gender': user.gender,
                'birth_date': user.birth_date,
                'email': user.email,
                'cellphone': user.cellphone,
                'address': user.address,
                'discharge_data': user.discharge_data,
                'is_active': user.is_active,
                'nickname': user.nickname
            }
        }


class ClinicHistorySerializer(serializers.ModelSerializer):
    patient = PatientSerializar()

    class Meta:
        model = ClinicHistory
        fields = ['clinic_history_id',
                  'creation_date',
                  'patient_id']

    def create(self, validated_data):
        patient_data = validated_data.pop('patient')
        patient_instance = Patient.objects.create(**patient_data)
        clinic_history_instance = ClinicHistory.objects.create(patient_id=patient_instance, **validated_data)
        return clinic_history_instance

    def to_representation(self, obj):
        clinic_history = ClinicHistory.objetcs.get(clinic_history_id=obj.clinic_history_id)
        patient = Patient.objects.get(patient_id=clinic_history.patient_id)
        return {
            'clinic_history_id': clinic_history.clinic_history_id,
            'creation_date': clinic_history.creation_date,
            'patient': {
                'patient_id': patient.patient_id,
            }
        }


class DiagnosticSerializer(serializers.ModelSerializer):
    clinic_history = ClinicHistorySerializer()
    patient = PatientSerializar()
    doctor = DoctorSerializer()
    employee = EmployeeSerializer()

    class Meta:
        model = Diagnostic
        fields = ['diagnostic_id',
                  'datetime',
                  'observations',
                  'treatment_effectiveness',
                  'next_visit',
                  'clinic_history-id',
                  'patient_id',
                  'doctor_id'
                  'employee_id']

    def create(self, validated_data):
        clinic_history_data = validated_data.pop('clinic_history')
        clinic_history_instance = ClinicHistory.objects.create(**clinic_history_data)
        patient_data = validated_data.pop('patient')
        patient_instance = Patient.objetcs.create(**patient_data)
        doctor_data = validated_data.pop('doctor')
        doctor_instance = Doctor.objects.create(**doctor_data)
        employee_data = validated_data.pop('employee')
        employee_instance = Employee.objects.create(**employee_data)
        diagnostic_instance = Diagnostic.objects.create(clinic_history_id=clinic_history_instance,
                                                        patient_id=patient_instance,
                                                        doctor_id=doctor_instance,
                                                        employee_id=employee_instance,
                                                        **validated_data)
        return diagnostic_instance

    def to_representation(self, obj):
        diagnostic = Diagnostic.objects.get(diagnostic_id=obj.diagnostic_id)
        clinic_history = ClinicHistory.objects.get(clinic_history_id=diagnostic.clinic_history_id)
        patient = Patient.objects.get(patient_id=diagnostic.patient_id)
        doctor = Doctor.objects.get(doctor_id=diagnostic.doctor_id)
        employee = Employee.objects.get(employee_id=diagnostic.employee_id)
        return {
            'diagnostic_id': diagnostic.diagnostic_id,
            'datetime': diagnostic.datetime,
            'observations': diagnostic.observations,
            'treatment_effectiveness': diagnostic.treatment_effectiveness,
            'next_visit': diagnostic.next_visit,
            'clinic_history': {
                'clinic_history_id': clinic_history.clinic_history_id,
                'creation_date': clinic_history.creation_date,
                'patient': {
                    'patient_id': patient.patient_id,
                }
            },
            'patient': {
                'patient_id': patient.patient_id,
            },
            'doctor': {
                'doctor_id': doctor.doctor_id,
                'speciality': doctor.speciality,
                'employee': {
                    'employee_id': employee.employee_id,
                    'position': employee.position
                }
            }
        }


class VitalSignsSerializer(serializers.ModelSerializer):
    clinic_history = ClinicHistorySerializer()
    patient = PatientSerializar()
    doctor = DoctorSerializer()
    employee = EmployeeSerializer()

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
                  'doctor_id'
                  'employee_id']

    def create(self, validated_data):
        clinic_history_data = validated_data.pop('clinic_history')
        clinic_history_instance = ClinicHistory.objects.create(**clinic_history_data)
        patient_data = validated_data.pop('patient')
        patient_instance = Patient.objects.create(**patient_data)
        doctor_data = validated_data.pop('doctor')
        doctor_instance = Doctor.objects.create(**doctor_data)
        employee_data = validated_data.pop('employee')
        employee_instance = Employee.objects.create(**employee_data)
        vital_signs_instance = VitalSigns.objects.create(clinic_history_id=clinic_history_instance,
                                                         patient_id=patient_instance,
                                                         doctor_id=doctor_instance,
                                                         employee_id=employee_instance,
                                                         **validated_data)
        return vital_signs_instance

    def to_representation(self, obj):
        vital_signs = VitalSigns.objects.get(vital_signs_id=obj.vital_signs_id)
        clinic_history = ClinicHistory.objects.get(clinic_history_id=obj.vital_signs.clinic_history_id)
        patient = Patient.objects.get(patient_id=obj.vital_signs.patient_id)
        doctor = Doctor.objects.get(doctor_id=obj.vital_signs.doctor_id)
        employee = Employee.objects.get(employee_id=obj.vital_signs.employee_id)
        return {
            'vital_signs_id': vital_signs.vital_signs_id,
            'oximetry': vital_signs.oximetry,
            'respiratory_rate': vital_signs.respiratory_rate,
            'heart_rate': vital_signs.heart_rate,
            'temperature': vital_signs.temperature,
            'systolic_blood_pressure': vital_signs.systolic_blood_pressure,
            'diastolic_blood_pressure': vital_signs.diastolic_blood_presurre,
            'blood_glucose': vital_signs.blood_glucose,
            'datetime': vital_signs.datetime,
            'clinic_history': {
                'clinic_history_id': clinic_history.clinic_history_id,
                'creation_date': clinic_history.creation_date,
                'patient': {
                    'patient_id': patient.patient_id,
                }
            },
            'patient': {
                'patient_id': patient.patient_id,
            },
            'doctor': {
                'doctor_id': doctor.doctor_id,
                'speciality': doctor.speciality,
                'employee': {
                    'employee_id': employee.employee_id,
                    'position': employee.position
                }
            }
        }


class CareTipsSerializer(serializers.ModelSerializer):
    diagnostic = DiagnosticSerializer()
    doctor = DoctorSerializer()
    relative = RelativeSerializer()
    employee= EmployeeSerializer()

    class Meta:
        model = CareTips
        fields = ['care_tips_id',
                  'datetime',
                  'suggestion',
                  'diagnostic_id',
                  'doctor_id',
                  'relative_id',
                  'employee_id']

    def create(self, validated_data):
        diagnostic_data = validated_data.pop('diagnostic')
        diagnostic_instance = Diagnostic.objects.create(**diagnostic_data)
        doctor_data = validated_data.pop('doctor')
        doctor_instance = Doctor.objects.create(**doctor_data)
        relative_data = validated_data.pop('relative')
        relative_instance = Relative.objects.create(**relative_data)
        employee_data = validated_data.pop('employee')
        employee_instance = Employee.objects.create(**employee_data)
        care_tips_instance = CareTips.objects.create(diagnostic_id=diagnostic_instance,
                                                     doctor_id=doctor_instance,
                                                     relative_id=relative_instance,
                                                     **validated_data)
        return care_tips_instance

    def to_representation(self, obj):
        care_tips = CareTips.objects.get(care_tips_id=obj.care_tips_id)
        diagnostic = Diagnostic.objects.get(diagnostic_id=obj.diagnostic_id)
        doctor = Doctor.objects.get(doctor_id=obj.doctor_id)
        relative = Relative.objects.get(relative_id=obj.relavite_id)
        employee = Employee.objects.get(employee_id=obj.employee_id)
        return {
            'care_tips_id': care_tips.care_tips_id,
            'datetime': care_tips.datetime,
            'suggestion': care_tips.suggestion,
            'diagnostic': {
                'diagnostic_id': diagnostic.diagnostic_id,
                'datetime': diagnostic.datetime,
                'observations': diagnostic.observations,
                'treatment_effectiveness': diagnostic.treatment_effectiveness,
                'next_visit': diagnostic.next_visit,
            },
            'doctor': {
                'doctor_id': doctor.doctor_id,
                'speciality': doctor.speciality,
                'employee': {
                    'employee_id': employee.employee_id,
                    'position': employee.positions
                }
            },
            'relative': {
                'relative_id': relative.relative_id,
            }
        }
