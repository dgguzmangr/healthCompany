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
                  'position',
                  'area']
        read_only_fields = ['employee_id']


class AssistantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistant
        fields = ['assistant_id',
                  'employee_id',
                  'user']
        read_only_fields = ['assistant_id', 'employee_id', 'user']

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
                    'position': employee.position,
                    'area': employee.area
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