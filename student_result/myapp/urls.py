from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', views.admin, name='admin'),
    path('professor/', views.professor, name='professor'),
    path('student/', views.student, name='student'),
    path('result/', views.result, name='result'),
    path('add_student/', views.add_student, name='add_student'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('declare/', views.declare, name='declare'),
    path('delete/<str:pk>/', views.delete, name='delete'),
    path('edit/<str:pk>/', views.edit, name='edit'),
    path('print/<str:pk>/', views.print, name='print'),
]