from rest_framework import serializers
from .models import Movie, Actor, Genre, HashTag, Review
from django.contrib.auth import get_user_model



class MovieListSerializer(serializers.ModelSerializer):

    class ActorSerializer(serializers.ModelSerializer):

        class Meta:
            model = Actor
            fields = ('name',)
    
    class GenreSerializer(serializers.ModelSerializer):

        class Meta:
            model = Genre
            fields = ('name',)
            
    actor_set = ActorSerializer(many=True)
    genre_set = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'


# class MovieSerializer(serializers.ModelSerializer):
    
#     class ActorSerializer(serializers.ModelSerializer):

#         class Meta:
#             model = Actor
#             fields = ('name',)
    
#     class GenreSerializer(serializers.ModelSerializer):

#         class Meta:
#             model = Genre
#             fields = ('name',)
            
#     actor_set = ActorSerializer(many=True)
#     genre_set = GenreSerializer(many=True)
    
#     class Meta:
#         model = Movie
#         fields = '__all__'


class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'


class GenreListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


class HashtagListSerializer(serializers.ModelSerializer):
    movie = MovieListSerializer(many=True)

    class Meta:
        model = HashTag
        fields = '__all__'

class ReviewListSerializer(serializers.ModelSerializer):
    class MovieTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title', 'code',)
    
    class ReviewUserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'username', 'nickname',)
    
    class HashtagInnerSerializer(serializers.ModelSerializer):
        class Meta:
            model = HashTag
            fields = ('tag',)
    
    movie = MovieTitleSerializer()
    user = ReviewUserSerializer()
    hashtag_set = HashtagInnerSerializer(many=True)
    
    class Meta:
        model = Review
        fields = '__all__'