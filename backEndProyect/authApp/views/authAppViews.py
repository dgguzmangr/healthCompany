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

