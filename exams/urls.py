from django.urls import path

from rest_framework.authtoken.views import ObtainAuthToken
from exams.views import AssessmentListView
from exams.views import AssessmentCreateView
from exams.views import AssessmentRetrieveUpdateDeleteView

urlpatterns = [
    path("assessments/token/",ObtainAuthToken.as_view()),
    path('assessments/',AssessmentListView.as_view()),
    path('assessments/create/',AssessmentCreateView.as_view()),
    path('assessments/<int:pk>/',AssessmentRetrieveUpdateDeleteView.as_view()),


]