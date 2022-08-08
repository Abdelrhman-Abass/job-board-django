from django.urls import path , include 
from . import views

app_name = 'Job'

urlpatterns = [
    path('signup' ,views.signup , name='signup'),
    path('Profile' ,views.Profile , name='Profile'),
    path('profile/edit' ,views.profile_edit , name='Profile_edit'),
]
