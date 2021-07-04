from rest_framework import serializers
from .models import StudentAccount
from .models import CareerQuestion

class StudentAccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StudentAccount
        fields = ('__all__')

class CareerQuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CareerQuestion
        fields = ('__all__')