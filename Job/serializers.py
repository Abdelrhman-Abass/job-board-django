
from rest_framework import  serializers
from .models import job


# Serializers define the API representation.
class jobSerializer(serializers.ModelSerializer):
    class Meta:
        model = job
        fields = '__all__'
