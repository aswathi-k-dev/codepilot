from django.urls import path
from problem.views import QuestionCreateView
from problem.views import QuestionRetrieveUpdateDeleteView

urlpatterns = [
    path("assessment/<int:pk>/question/",QuestionCreateView.as_view()),
    path("assessment/question/<int:pk>/",QuestionRetrieveUpdateDeleteView.as_view()),



  
]