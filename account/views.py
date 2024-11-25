from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpRequest

from .models import Profile
from .serializers import ProfileSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request: HttpRequest) -> Response:
    user =  request.user
    profile = Profile.objects.filter(user=user)
    serializer = ProfileSerializer(profile, many=True)
    return Response(serializer.data)
