from .models import Person
from rest_framework import serializers

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'name', 'account_number', 'bank_name', 'email', 'address', 'telephone', 'paid', 'photo', 'joined', 'updated']