from rest_framework import serializers
from userdata.models import Usermodel, ActivityPeriod

class Activityserializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields=('start_time','end_time')

class Usermodelserializer(serializers.ModelSerializer):
    Activity=Activityserializer(read_only=True,many=True)
    class Meta:
        model = Usermodel
        fields=('id', 'real_name','tz','Activity')

