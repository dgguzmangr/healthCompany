"""
URL configuration for healthCompany project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from authApp.views import authAppViews

urlpatterns = [
    # user urls
    path('admin/', admin.site.urls),
    path('create_user/', authAppViews.create_user),
    path('show_user/', authAppViews.show_user),
    path('update_user/<int:pk>/', authAppViews.update_user),
    path('delete_user/<int:pk>/', authAppViews.delete_user),
    # employee urls
    path('create_employee/', authAppViews.create_employee),
    path('show_employee/', authAppViews.show_employee),
    path('update_employee/<int:pk>/', authAppViews.update_employee),
    path('delete_employee/<int:pk>/', authAppViews.delete_employee),
    # assistant urls
    path('create_assistant/', authAppViews.create_assistant),
    path('show_assistant/', authAppViews.show_assistant),
    path('update_assistant/<int:pk>/', authAppViews.update_assistant),
    path('delete_assistant/<int:pk>/', authAppViews.delete_assistant),
    # doctor urls
    path('create_doctor/', authAppViews.create_doctor),
    path('show_doctor/', authAppViews.show_doctor),
    path('update_doctor/<int:pk>/', authAppViews.update_doctor),
    path('delete_doctor/<int:pk>/', authAppViews.delete_doctor),
    # nurse urls
    path('create_nurse/', authAppViews.create_nurse,),
    path('show_nurse/', authAppViews.show_nurse),
    path('update_nurse/<int:pk>/', authAppViews.update_nurse),
    path('delete_nurse/<int:pk>/', authAppViews.delete_nurse),
    # patient urls
    path('create_patient/', authAppViews.create_patient),
    path('show_patient/', authAppViews.show_patient),
    path('update_patient/<int:pk>/', authAppViews.update_patient),
    path('delete_patient/<int:pk>/', authAppViews.delete_patient),
    # relative urls
    path('create_relative/', authAppViews.create_relative),
    path('show_relative/', authAppViews.show_relative),
    path('update_relative/<int:pk>/', authAppViews.update_relative),
    path('delete_relative/<int:pk>/', authAppViews.delete_relative),
    # clinic history urls
    path('create_clinic_history/', authAppViews.create_clinic_history),
    path('show_clinic_history/', authAppViews.show_clinic_history),
    path('update_clinic_history/<int:pk>/', authAppViews.update_clinic_history),
    path('delete_clinic_history/<int:pk>/', authAppViews.delete_clinic_history),
    # diagnostic urls
    path('create_diagnostic/', authAppViews.create_diagnostic),
    path('show_diagnostic/', authAppViews.show_diagnostic),
    path('update_diagnostic/<int:pk>/', authAppViews.update_diagnostic),
    path('delete_diagnostic/<int:pk>/', authAppViews.delete_diagnostic),
    # vital signs urls
    path('create_vital_signs/', authAppViews.create_vital_signs),
    path('show_vital_signs/', authAppViews.show_vital_signs),
    path('update_vital_signs/<int:pk>/', authAppViews.update_vital_signs),
    path('delete_vital_signs/<int:pk>/', authAppViews.delete_vital_signs),
    # tips care urls
    path('create_care_tips/', authAppViews.create_care_tips),
    path('show_care_tips/', authAppViews.show_care_tips),
    path('update_care_tips/<int:pk>/', authAppViews.update_care_tips),
    path('delete_care_tips/<int:pk>/', authAppViews.delete_care_tips),
    # main post urls
    path('create_main_post/', authAppViews.create_main_post),
    path('show_main_post/', authAppViews.show_main_post),
    path('update_main_post/<int:pk>/', authAppViews.update_main_post),
    path('delete_main_post/<int:pk>/', authAppViews.delete_main_post),
]
