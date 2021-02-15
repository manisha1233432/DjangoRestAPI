from django.shortcuts import render
from userdata.models import Usermodel, ActivityPeriod
from userdata.serialize import Activityserializer, Usermodelserializer
from rest_framework import viewsets

class Userapi(viewsets.ModelViewSet):
    queryset = Usermodel.objects.all()
    serializer_class= Usermodelserializer

class Activityapi(viewsets.ModelViewSet):
    queryset = ActivityPeriod.objects.all()
    serializer_class= Activityserializer

