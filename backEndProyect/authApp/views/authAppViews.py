from rest_framework.decorators import api_view
from rest_framework.response import Response

from authApp.models.models import User
from authApp.serializers.serializers import *
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist


# user methods
@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


def show_user(request):
    if request.method == 'GET':
        users = User.objects.all()
        return JsonResponse([UserSerializer(user).data for user in users], status=200, safe=False)


@api_view(['PUT'])
def update_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=404)

    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def delete_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=404)

    user.delete()
    return Response(status=204)


# employee methods
@api_view(['POST'])
def create_employee(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


def show_employee(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        return JsonResponse([EmployeeSerializer(employee).data for employee in employees], status=200, safe=False)


@api_view(['PUT'])
def update_employee(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response(status=404)

    serializer = EmployeeSerializer(employee, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def delete_employee(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=404)

    employee.delete()
    return Response(status=204)


# Assistant methods:
@api_view(['POST'])
def create_assistant(request):
    serializer = AssistantSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


def show_assistant(request):
    if request.method == 'GET':
        assistants = Assistant.objects.all()
        return JsonResponse([AssistantSerializer(assistant).data for assistant in assistants], status=200, safe=False)


@api_view(['PUT'])
def update_assistant(request, pk):
    try:
        assistant = Assistant.objects.get(pk=pk)
    except Assistant.DoesNotExist:
        return Response(status=404)

    serializer = AssistantSerializer(assistant, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def delete_assistant(request, pk):
    try:
        assistant = Assistant.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=404)

    assistant.delete()
    return Response(status=204)


# Doctor methods
@api_view(['POST'])
def create_doctor(request):
    serializer = DoctorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


def show_doctor(request):
    if request.method == 'GET':
        doctors = Doctor.objects.all()
        return JsonResponse([DoctorSerializer(doctor).data for doctor in doctors], status=200, safe=False)


@api_view(['PUT'])
def update_doctor(request, pk):
    try:
        doctor = Doctor.objects.get(pk=pk)
    except Doctor.DoesNotExist:
        return Response(status=404)

    serializer = DoctorSerializer(doctor, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def delete_doctor(request, pk):
    try:
        doctor = Doctor.objects.get(pk=pk)
    except Doctor.DoesNotExist:
        return Response(status=404)

    doctor.delete()
    return Response(status=204)


# Nurse methods
@api_view(['POST'])
def create_nurse(request):
    serializer = NurseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


def show_nurse(request):
    if request.method == 'GET':
        nurses = Nurse.objects.all()
        return JsonResponse([NurseSerializer(nurse).data for nurse in nurses], status=200, safe=False)


@api_view(['PUT'])
def update_nurse(request, pk):
    try:
        nurse = Nurse.objects.get(pk=pk)
    except Nurse.DoesNotExist:
        return Response(status=404)

    serializer = NurseSerializer(nurse, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def delete_nurse(request, pk):
    try:
        nurse = Nurse.objects.get(pk=pk)
    except Nurse.DoesNotExist:
        return Response(status=404)

    nurse.delete()
    return Response(status=204)


# Patient methods
@api_view(['POST'])
def create_patient(request):
    serializer = PatientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


def show_patient(request):
    if request.method == 'GET':
        patients = Patient.objects.all()
        return JsonResponse([PatientSerializer(patient).data for patient in patients], status=200, safe=False)


@api_view(['PUT'])
def update_patient(request, pk):
    try:
        patient = Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return Response(status=404)

    serializer = PatientSerializer(patient, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def delete_patient(request, pk):
    try:
        patient = Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return Response(status=404)

    patient.delete()
    return Response(status=204)


# Relative methods
@api_view(['POST'])
def create_relative(request):
    serializer = RelativeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


def show_relative(request):
    if request.method == 'GET':
        relatives = Relative.objects.all()
        return JsonResponse([RelativeSerializer(relative).data for relative in relatives], status=200, safe=False)


@api_view(['PUT'])
def update_relative(request, pk):
    try:
        relative = Relative.objects.get(pk=pk)
    except Relative.DoesNotExist:
        return Response(status=404)

    serializer = RelativeSerializer(relative, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def delete_relative(request, pk):
    try:
        relative = Relative.objects.get(pk=pk)
    except Relative.DoesNotExist:
        return Response(status=404)

    relative.delete()
    return Response(status=204)


# Clinic history methods
@api_view(['POST'])
def create_clinic_history(request):
    serializer = ClinicHistorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


def show_clinic_history(request):
    if request.method == 'GET':
        clinic_histories = ClinicHistory.objects.all()
        return JsonResponse([ClinicHistorySerializer(clinic_history).data for clinic_history in clinic_histories], status=200, safe=False)


@api_view(['PUT'])
def update_clinic_history(request, pk):
    try:
        clinic_history = ClinicHistory.objects.get(pk=pk)
    except ClinicHistory.DoesNotExist:
        return Response(status=404)

    serializer = ClinicHistorySerializer(clinic_history, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def delete_clinic_history(request, pk):
    try:
        clinic_history = ClinicHistory.objects.get(pk=pk)
    except ClinicHistory.DoesNotExist:
        return Response(status=404)

    clinic_history.delete()
    return Response(status=204)


# Diagnostic methods
@api_view(['POST'])
def create_diagnostic(request):
    serializer = DiagnosticSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


def show_diagnostic(request):
    if request.method == 'GET':
        diagnostics = Diagnostic.objects.all()
        return JsonResponse([DiagnosticSerializer(diagnostic).data for diagnostic in diagnostics], status=200, safe=False)


@api_view(['PUT'])
def update_diagnostic(request, pk):
    try:
        diagnostic = Diagnostic.objects.get(pk=pk)
    except Diagnostic.DoesNotExist:
        return Response(status=404)

    serializer = DiagnosticSerializer(diagnostic, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def delete_diagnostic(request, pk):
    try:
        diagnostic = Diagnostic.objects.get(pk=pk)
    except Diagnostic.DoesNotExist:
        return Response(status=404)

    diagnostic.delete()
    return Response(status=204)


# Vital signs methods
@api_view(['POST'])
def create_vital_signs(request):
    serializer = VitalSignsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


def show_vital_signs(request):
    if request.method == 'GET':
        vital_signs = VitalSigns.objects.all()
        return JsonResponse([VitalSignsSerializer(vital_sign).data for vital_sign in vital_signs], status=200, safe=False)


@api_view(['PUT'])
def update_vital_signs(request, pk):
    try:
        vital_signs = VitalSigns.objects.get(pk=pk)
    except VitalSigns.DoesNotExist:
        return Response(status=404)

    serializer = VitalSignsSerializer(vital_signs, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def delete_vital_signs(request, pk):
    try:
        vital_signs = VitalSigns.objects.get(pk=pk)
    except VitalSigns.DoesNotExist:
        return Response(status=404)

    vital_signs.delete()
    return Response(status=204)


# Care tips methods
@api_view(['POST'])
def create_care_tips(request):
    serializer = CareTipsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


def show_care_tips(request):
    if request.method == 'GET':
        care_tips = CareTips.objects.all()
        return JsonResponse([CareTipsSerializer(care_tip).data for care_tip in care_tips], status=200, safe=False)


@api_view(['PUT'])
def update_care_tips(request, pk):
    try:
        care_tips = CareTips.objects.get(pk=pk)
    except CareTips.DoesNotExist:
        return Response(status=404)

    serializer = CareTipsSerializer(care_tips, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def delete_care_tips(request, pk):
    try:
        care_tips = CareTips.objects.get(pk=pk)
    except CareTips.DoesNotExist:
        return Response(status=404)

    care_tips.delete()
    return Response(status=204)


# Main post methods
@api_view(['POST'])
def create_main_post(request):
    serializer = MainPostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


def show_main_post(request):
    if request.method == 'GET':
        main_posts = MainPost.objects.all()
        return JsonResponse([MainPostSerializer(main_post).data for main_post in main_posts], status=200, safe=False)


@api_view(['PUT'])
def update_main_post(request, pk):
    try:
        main_post = MainPost.objects.get(pk=pk)
    except MainPost.DoesNotExist:
        return Response(status=404)

    serializer = MainPostSerializer(main_post, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def delete_main_post(request, pk):
    try:
        main_post = MainPost.objects.get(pk=pk)
    except MainPost.DoesNotExist:
        return Response(status=404)

    main_post.delete()
    return Response(status=204)