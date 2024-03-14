from rest_framework import serializers
from .models import student

class Stud_serializer(serializers.ModelSerializer):
    class Meta:
        model=student
        fields=['id','name','city','roll']