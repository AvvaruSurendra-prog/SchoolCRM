from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Teacher

# Create your views here.

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, "teachers/index.html", {"allteachers":teachers})

def add_teacher(request):
    if request.method == "POST":
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        image = request.FILES.get('image')

        teacher = Teacher(
            name = name,
            subject = subject,
            contact = contact,
            email = email,
            image = image if image else None
        )
        teacher.save()
        return redirect("all-teachers")
    return render(request, "index.html")

def update_teacher(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        image = request.FILES.get('image')

        teacher = Teacher(
            id = id,
            name = name,
            subject = subject,
            contact = contact,
            email = email,
            image = image if image else None
        )
        teacher.save()
        return redirect("all-teachers")
    return render(request, 'index.html',{'teacher': teacher} )

def delete_teacher(request, id):
    teacher = Teacher.objects.filter(id=id)
    teacher.delete()

    return redirect("all-teachers")
