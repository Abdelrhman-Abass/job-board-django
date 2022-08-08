from django.urls import path , include 
from . import views
from . import api
app_name = 'Job'
urlpatterns = [
    path('' ,views.jobs , name='job_list'),
    path('add' ,views.add_job , name='add_job'),
    path('<str:slug>' ,views.job_detail , name='job_detail'),
    
    # api 
    path('api/jobs' ,api.jobapi , name='jobapi'),
    path('api/jobs/<int:id>' ,api.api_detail_api , name='api_detail_api'),

    path('api/v2/jobs' ,api.joblistapi.as_view() , name='joblistapi'),
    path('api/v2/jobs/<int:id>' ,api.jobdetail.as_view() , name='jobdetail'),

]
