
from django.urls import path
from . import views
from django.views.generic import TemplateView



app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
     path('personal-details/', views.personal_details, name='personal-details'),
     path('add-new/',views.addItem,name='add-new'),
]