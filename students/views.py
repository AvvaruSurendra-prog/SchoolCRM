from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'allstudents': students})

def add_student(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        date_of_birth = request.POST.get('date_of_birth')
        image = request.FILES.get('image')

        student = Student(
            first_name=first_name,
            last_name=last_name,
            email=email,
            date_of_birth=date_of_birth,
            image=image if image else None
        )
        student.save()
        return redirect("student_list")
    return render(request, "index.html")

def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    
    if request.method == "POST":
        student.first_name = request.POST.get('first_name', student.first_name)
        student.last_name = request.POST.get('last_name', student.last_name)
        student.email = request.POST.get('email', student.email)
        student.date_of_birth = request.POST.get('date_of_birth', student.date_of_birth)
        
        if 'image' in request.FILES:
            student.image = request.FILES['image']

        student.save()
        return redirect("student_list")

    return render(request, 'index.html', {'student': student})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect("student_list")

