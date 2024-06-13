from rest_framework import serializers
from .models import Question,Option 



class QuestionSerializer(serializers.ModelSerializer):
    #choice = ChoiceSerializer(many = True)
    class Meta:
        model = Question
        fields = "__all__"

class ChoiceSerializer(serializers.ModelSerializer):
    question_text = QuestionSerializer()
    class Meta:
        model = Choice
        fields = "__all__"
    