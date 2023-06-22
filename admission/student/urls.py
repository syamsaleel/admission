from django.urls import path
from student.views import create_student, Viewget


urlpatterns = [
    path('student/', create_student, name='createstudent'),
    path('getview/', Viewget, name='success'),
]
