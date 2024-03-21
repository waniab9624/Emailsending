from rest_framework import serializers
from .models import Emailmodel
class Emailmodelserializer(serializers.ModelSerializer):
    class Meta:
        model=Emailmodel
        fields='__all__'