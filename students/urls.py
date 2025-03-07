from django.urls import path
from . import views

urlpatterns = [
   
    path("student-list/", views.student_list, name="student_list"),
    path('add-student/', views.add_student, name="add-student"),
    path('update-student/<int:id>/', views.update_student, name="update-student"),
    path('delete-student/<int:id>/', views.delete_student, name="delete-student"),

]