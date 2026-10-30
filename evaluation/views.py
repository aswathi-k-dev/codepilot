from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView
from rest_framework import authentication,permissions
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.generics import UpdateAPIView

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


class AnswerUpdateView(APIView):


    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAdminUser]

    # serializer_class = AnswerSerializer
    
    # queryset = Answer.objects.all()



    def patch(self,request,pk = None):

        answer_id = pk

        form_data = request.data

        # validation start

        answer_object = get_object_or_404(Answer,id = answer_id)

        marks = form_data.get("marks_awarded")

        if marks > answer_object.question.score:

            raise serializers.ValidationError("marks must be less than score")

        serializer_instance = AnswerSerializer(data = form_data,instance = answer_object,partial = True)

        serializer_instance.fields["marks_awarded"].read_only = False

        serializer_instance.fields["feedback"].read_only = False


        if serializer_instance.is_valid():

            serializer_instance.save()

            # Answer.objects.filter(id = answer_id).update(**form_data)

            # response_data = {"message":"answer evaluated"}

            # serializer_instance.save()

            return Response(data = serializer_instance.data)

        else:

            return Response(data = serializer_instance.errors)
        
