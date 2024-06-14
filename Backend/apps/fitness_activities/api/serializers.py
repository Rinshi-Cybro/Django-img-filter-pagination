from rest_framework import serializers
from ..models import *



class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = UserActivity
        fields = '__all__'




class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = '__all__'    

