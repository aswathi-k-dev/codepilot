from django.urls import path
from accounts.views import AdminCreateView
from accounts.views import StudentCreateView

urlpatterns = [
    path("admin/register/",AdminCreateView.as_view()),
    path("student/register/",StudentCreateView.as_view()),
]