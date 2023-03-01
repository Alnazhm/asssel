from django.urls import path
from . import views

urlpatterns = [
    path('api/student/', views.student_list, name='student_list'),
    path('api/students/<int:pk>/', views.student_detail, name='student_detail'),
]