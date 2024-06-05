from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from movies.models import Actor, Genre
from .serializers import EditNicknameSerializer, EditPreferenceSerializer, UserProfileSerializer
from movies.models import Movie

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_detail(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    serializer = UserProfileSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_nickname(request):
    if request.method == 'PUT':
        serializer = EditNicknameSerializer(request.user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            result = EditNicknameSerializer(user)
            return Response(result.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def edit_preference(request):
    user = request.user
    if request.method == 'GET':
        serializer = EditPreferenceSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        print(request.data.get('like_actor')[11:-3])
        print(request.data.get('like_genre')[11:-3])
        user.like_actor = get_object_or_404(Actor, name=request.data.get('like_actor')[11:-3])
        user.like_genre = get_object_or_404(Genre, name=request.data.get('like_genre')[11:-3])
        user.save()
        after_user = get_user_model().objects.get(pk=user.pk)
        serializer = EditPreferenceSerializer(after_user)
        return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def password_check(request):
    if request.method == 'POST':
        password = request.data.get('password')
        if check_password(password, request.user.password):
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def sign_out(request):
    if request.method == 'DELETE':
        user = request.user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

