from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('university/create', views.create_unversity),
    path('university/<int:uni_id>/update', views.update_university),
    path('university/<int:uni_id>/delete', views.delete_university),
    path('university/<int:uni_id>', views.university),
    path('university/', views.university_list),
    path('student/create', views.create_student),
    path('student/<int:student_id>/update', views.update_student),
    path('student/<int:student_id>/delete', views.delete_student),
    path('student/<int:student_id>', views.student),
    path('student/', views.student_list),
]