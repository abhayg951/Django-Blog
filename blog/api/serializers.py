from rest_framework import serializers
from django.contrib.auth.models import User
from members.models import UserProfile

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            "id",
            "url",
            "bio",
            "profile_pic",
            "linkedin_url",
            "stackOverflow_url",
            "github_url",
            "instagram_url",
            "user"
        ]

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(many=False, read_only=True)
    class Meta:
        model = User
        # fields = "__all__"
        fields = [
            "url",
            'first_name',
            'last_name',
            'username',
            'email',
            'last_login',
            "date_joined",
            'profile'
        ]