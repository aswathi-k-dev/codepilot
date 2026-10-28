from rest_framework import serializers

from exams.models import Assessment

from django.db.models import Sum

from datetime import date

from problem.models import Question
from problem.serializers import QuestionSerializer


class AssessmentSerializer(serializers.ModelSerializer):

    greetings = serializers.SerializerMethodField(read_only = True)

    question_count = serializers.SerializerMethodField(read_only = True)

    total_marks = serializers.SerializerMethodField(read_only = True)

    questions = serializers.SerializerMethodField(read_only = True)


    class Meta:
        model = Assessment
        fields = "__all__"
        read_only_fields = ["id","end_time","created_by"]

    def validate_exam_date(self,value):

        if value < date.today():
            raise serializers.ValidationError("previous date is not allowed")
        return value

    def get_greetings(self,obj):

        return "good morning"

    def get_question_count(self,obj):

        return Question.objects.filter(assessment = obj).count()

    def get_total_marks(self,obj):

        return Question.objects.filter(assessment = obj).values("score").aggregate(total = Sum("score")).get("total")

    def get_questions(self,obj):

        question_object = Question.objects.filter(assessment = obj)

        serializer_instance = QuestionSerializer(question_object,many = True)

        return serializer_instance.data



