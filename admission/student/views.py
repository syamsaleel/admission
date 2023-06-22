
from django.shortcuts import render, redirect
from .forms import StudentForm
from django.views.generic import ListView
from .models import Student
from django.http import HttpResponse

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = StudentForm()
    return render(request, 'student/createstudent.html', {'form': form})

def Viewget(request):
    students = Student.objects.all()
    return render(request, 'student/view.html', {'students': students})