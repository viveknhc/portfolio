
from django.shortcuts import render
from .models import PersonalDetails
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import PersonalDetails
from .serializers import PersonalDetailsSerializer

from django.urls import reverse




@api_view(['GET'])
def personal_details(request):
    details = PersonalDetails.objects.all()
    serializer = PersonalDetailsSerializer(details, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    addSerializer = PersonalDetailsSerializer(data = request.data)
    if addSerializer.is_valid():
        addSerializer.save()
    return Response(addSerializer.data)

def index(request):
    context = {"is_index": True}
    return render(request, "web/index.html", context)
  