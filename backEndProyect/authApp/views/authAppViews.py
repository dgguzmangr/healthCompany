from authApp.models.models import User
from authApp.serializers.serializers import UserSerializer
from django.http import JsonResponse


def show_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        return JsonResponse([UserSerializer(user).data for user in users], status=200, safe=False)

