from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from accounts.serializers import UserSerializer
from accounts.models import User


# Create your views here.

class AdminCreateView(APIView):

    def post(self,request):

        form_data = request.data

        serializer_instance = UserSerializer(data = form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            instance = User.objects.create_superuser(role = "admin",**cleaned_data)

            serializer_instance = UserSerializer(instance)

            return Response(data = serializer_instance.data)
        
        else:

            return Response(data = serializer_instance.errors)

class StudentCreateView(APIView):

    def post(self,request):

        form_data = request.data

        serializer_instance = UserSerializer(data = form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            instance = User.objects.create_user(**cleaned_data)

            serializer_instance = UserSerializer(instance)

            return Response(data = serializer_instance.data)

        else:

            return Response(data = serializer_instance.errors)
