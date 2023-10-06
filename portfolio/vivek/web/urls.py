
from django.urls import path
from . import views
from django.views.generic import TemplateView



app_name = "web"

urlpatterns = [
    path('', views.personal_details, name='personal-details'),
    path('skill/', views.skill, name='skill'),
    path('experience/', views.experience, name='experience'),
    path('education/',views.education,name="education"),
    path('service/',views.service,name="service"),
    path('projects/',views.projects,name="projects"),
    path('add-new/',views.addItem,name='add-new'),
]