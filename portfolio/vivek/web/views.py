
from django.shortcuts import render
from .models import PersonalDetails
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import PersonalDetails,SkillSett,Experience,Education,Service,Projects
from .serializers import PersonalDetailsSerializer,ExperienceSerializer,SkillSettSerializer,EducationSerializer,ServiceSerializer,ProjectsSerializer

from django.urls import reverse


@api_view(['GET'])
def personal_details(request):
    detailsPersonalDetails = PersonalDetails.objects.all()
    serializerPersonal = PersonalDetailsSerializer(detailsPersonalDetails, many=True)
    return Response(serializerPersonal.data)

@api_view(['POST'])
def addItem(request):
    addSerializer = PersonalDetailsSerializer(data = request.data)
    if addSerializer.is_valid():
        addSerializer.save()
    return Response(addSerializer.data)

@api_view(['GET'])
def skill(request):
    skill = SkillSett.objects.all()
    serializerSkillSett = SkillSettSerializer(skill,many=True)
    return Response(serializerSkillSett.data)

@api_view(['GET'])
def experience(request):
    experience = Experience.objects.all()
    serializerexperience = ExperienceSerializer(experience,many=True)
    return Response(serializerexperience.data)

@api_view(['GET'])
def education(request):
    education = Education.objects.all()
    serializerEducation = EducationSerializer(education,many=True)
    return Response(serializerEducation.data)

@api_view(['GET'])
def service(request):
    service = Service.objects.all()
    serializerService = ServiceSerializer(service,many=True)
    return Response(serializerService.data)

@api_view(['GET'])
def projects(request):
    projects = Projects.objects.all()
    serializerProjects = ProjectsSerializer(projects,many=True)
    return Response(serializerProjects.data)
