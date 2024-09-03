from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializers import UserSerializer, UserProfileSerializer
from members.models import UserProfile

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
