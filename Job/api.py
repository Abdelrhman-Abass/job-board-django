from pyexpat import model
from .models import job
from .serializers import jobSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics 

@api_view(['GET'])
def jobapi(request):
    all_jobs = job.objects.all()
    data = jobSerializer(all_jobs, many=True).data
    return Response({'data': data})



@api_view(['GET'])
def api_detail_api(request,id):
    job_detail = job.objects.get(id=id)
    data = jobSerializer(job_detail).data
    return Response({'data': data})


class joblistapi(generics.ListCreateAPIView):
    model = job
    queryset = job.objects.all()
    serializer_class = jobSerializer


class jobdetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = jobSerializer
    queryset = job.objects.all()
    lookup_field = 'id'