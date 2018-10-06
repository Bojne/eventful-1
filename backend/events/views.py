from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from . models import *
from . serializers import *
from rest_framework.response import Response

# API for accessing Event objects
class EventAPI(ObtainAuthToken):
    
    def get(self, request, *args, **kwargs):
        """
        List all User objects
        """
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
        
#API for accessing user objects        
class UserAPI(ObtainAuthToken):
    def get(self, request, *args, **kwargs):
        """
        List all User objects
        """
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)