from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView
from rest_framework import authentication,permissions
from rest_framework.response import Response
from rest_framework import serializers

from evaluation.permissions import IsStudentUser
from evaluation.models import Submission,Answer
from evaluation.serializers import SubmissionSerializer,AnswerSerializer

from problem.models import Question


from exams.models import Assessment

# Create your views here.

class SubmissionStartView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsStudentUser]

    def post(self,request,pk = None):

        assessment_id = pk

        assessment_object = get_object_or_404(Assessment,id = assessment_id)

        instance = Submission.objects.create(assessment = assessment_object,student = request.user)

        serializer_instance = SubmissionSerializer(instance)

        return Response(data = serializer_instance.data)

class AnswerCreateView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsStudentUser]

    def post(self,request,pk = None):

        submission_id = pk

        submission_object = get_object_or_404(Submission,id = submission_id)

        form_data = request.data

        # validation start

        assessment_object = submission_object.assessment

        assessment_question = Question.objects.filter(assessment = assessment_object).values_list("id",flat=True)

        question = form_data.get("question")

        if question not in assessment_question:

            raise serializers.ValidationError("invalid question,question not exist in assessment")

        # validation end

        serializer_instance = AnswerSerializer(data = form_data)

        if serializer_instance.is_valid():

            serializer_instance.save(submission = submission_object)

            return Response(data = serializer_instance.data)
        
        else:

            return Response(data = serializer_instance.errors)

class SubmissionRetrieveView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAdminUser]

    def get(self,request,pk = None):

        instance = get_object_or_404(Submission,id = pk)

        serializer_instance = SubmissionSerializer(instance)

        return Response(data = serializer_instance.data)

        