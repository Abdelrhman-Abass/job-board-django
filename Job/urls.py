from django.urls import path , include 
from . import views
urlpatterns = [
    path('' ,views.jobs),
    path('<int:id>' ,views.job_detail),
    
]
