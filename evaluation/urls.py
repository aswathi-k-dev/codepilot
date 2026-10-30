from django.urls import path
from evaluation.views import SubmissionStartView
from evaluation.views import AnswerCreateView
from evaluation.views import SubmissionRetrieveView
from evaluation.views import AnswerUpdateView

urlpatterns = [
    path("assessment/<int:pk>/submission/",SubmissionStartView.as_view()),
    path("submission/<int:pk>/answer/",AnswerCreateView.as_view()),
    path("submission/<int:pk>/",SubmissionRetrieveView.as_view()),
    path("answers/<int:pk>/",AnswerUpdateView.as_view()),
    
]