from rest_framework import serializers
from app.models import *

class EmployeMS(serializers.ModelSerializer):
    class Meta:
        model=employe
        fields='__all__'
        