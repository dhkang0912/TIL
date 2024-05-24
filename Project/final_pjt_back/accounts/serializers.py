from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
# from .models import AbstractUser
from movies.models import Movie, Actor, Genre, HashTag, Review


class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(
        required=True,
        allow_blank=False,
    )
    like_actor = serializers.ReadOnlyField(source='actor.pk')
    like_genre = serializers.ReadOnlyField(source='genre.pk')

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            # 추가한 필드
            'nickname': self.validated_data.get('nickname', ''),
        }


class EditNicknameSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('nickname',)


class EditPreferenceSerializer(serializers.ModelSerializer):

    class LikeActorSerializer(serializers.ModelSerializer):

        class Meta:
            model = Actor
            fields = '__all__'
    
    class LikeGenreSerializer(serializers.ModelSerializer):

        class Meta:
            model = Genre
            fields = '__all__'
    
    like_actor = LikeActorSerializer()
    like_genre = LikeGenreSerializer()
    
    class Meta:
        model = get_user_model()
        fields = ('like_actor', 'like_genre',)


class UserProfileSerializer(serializers.ModelSerializer):
    
    class LikeActorSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Actor
            fields = '__all__'
    
    
    class LikeGenreSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Genre
            fields = '__all__'
    
    
    class LikeMovieSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Movie
            fields = '__all__'
    
    
    like_actor = LikeActorSerializer()    
    like_genre = LikeGenreSerializer()
    like_movie = LikeMovieSerializer(many=True)
    
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'nickname', 'like_actor', 'like_genre', 'like_movie',)