import requests
import ast
from django.shortcuts import get_list_or_404, get_object_or_404
from django.db.models import Q
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Movie, Actor, Genre, HashTag, Review
from .serializers import MovieListSerializer, HashtagListSerializer, ActorListSerializer, GenreListSerializer, ReviewListSerializer
from accounts.serializers import UserProfileSerializer


@api_view(['GET'])
def all_movies(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def all_actors(request):
    if request.method == 'GET':
        actors = get_list_or_404(Actor)
        serializer = ActorListSerializer(actors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def all_genres(request):
    if request.method == 'GET':
        genres = get_list_or_404(Genre)
        serializer = GenreListSerializer(genres, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommended_movies(request):
    if request.method == 'GET':
        # filtered_movies = get_list_or_404(Movie, actor=request.user.actor, genre=request.user.genre)
        filtered_movies = Movie.objects.filter(
            Q(actor=request.user.like_actor) | 
            Q(genre=request.user.like_genre)
        ).distinct()  # 중복 제거
        # filtered_movies = Movie.objects.filter(actors__in=[request.user.like_actor], genres__in=[request.user.like_genre]).distinct()/
        serializer = MovieListSerializer(filtered_movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_review(request, movie_pk):
    if request.method == 'POST':
        # 해시태그 추가 관련
        selected_tags = request.data.get('tags')
        text = request.data.get('review')

        # 리뷰 본문 관련
        review = Review()
        review.user = request.user
        review.movie = get_object_or_404(Movie, pk=movie_pk)
        review.text = text
        review.save()

        # 해시태그 등록 관련
        for tag in selected_tags:
            hashtag = get_object_or_404(HashTag, tag=tag)
            hashtag.review.add(review.pk)
        return Response(data={'message': '리뷰 및 관련 해시태그 등록 성공'}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def movie_reviews(request, movie_pk):
    if request.method == 'GET':
        reviews = get_list_or_404(Review, movie=movie_pk)
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def personal_reviews(request):
    if request.method == 'GET':
        personal_reviews = Review.objects.filter(user=request.user)
        serializer = ReviewListSerializer(personal_reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def review(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.user:
        if request.method == 'PUT':
            review.text = request.data.get('text')
            review.save()
            return Response(data={'message': '리뷰 수정 성공'}, status=status.HTTP_202_ACCEPTED)
        elif request.method == 'DELETE':
            review.delete()
            return Response(data={'message': '리뷰 삭제 성공'}, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(data={'message': '현재 로그인한 사용자가 작성한 리뷰가 아닙니다.'}, status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_movie(request, movie_pk):
    if request.method == 'POST':
        print(request.POST)
        user = request.user
        movie = get_object_or_404(Movie, pk=int(movie_pk))
        if user.like_movie.filter(pk=int(movie_pk)).exists():
            user.like_movie.remove(movie)
        else:
            user.like_movie.add(movie)
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_hashtag(request):
    tags = get_list_or_404(HashTag)
    serializer = HashtagListSerializer(tags, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def hashtag_to_movie(request):
    tags = request.data.get('tags')
    print(tags)
    movies = []
    for tag in tags:
        hashtag = get_object_or_404(HashTag, tag=tag)
        reviews = get_list_or_404(Review, hashtag=hashtag.pk)
        if reviews:
            for review in reviews:
                movie = get_object_or_404(Movie, pk=review.movie.pk)
                movies.append(movie)
    movies = list(set(movies))
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)









'''
### movie 테이블 seed data 관련 코드
def update_movie():
    combined_data = []
    
    URL_Movie_lists_Now_playing = 'https://api.themoviedb.org/3/movie/now_playing'
    URL_Movie_lists_Upcoming = 'https://api.themoviedb.org/3/movie/upcoming'

    # movie_id = 1
    # URL_Movies_Detail = f'https://api.themoviedb.org/3/movie/{movie_id}'

    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {settings.SECRET_KEY}'
    }

    # 개봉 이후 영화 데이터 불러오기
    for page in range(1, 20):
        params = {
            'language': 'ko-KR',
            'page': page,
        }
        
        response = requests.get(URL_Movie_lists_Now_playing, headers=headers, params=params)

        data = response.json()
        # pprint(len(data.get('results')))
        combined_data.extend(data.get('results'))
    
    # 개봉 예정 영화 불러오기
    for page in range(1, 20):
        params = {
            'language': 'ko-KR',
            'page': page,
        }
        
        response = requests.get(URL_Movie_lists_Upcoming, headers=headers, params=params)
        
        data = response.json()
        # pprint(len(data.get('results')))
        combined_data.extend(data.get('results'))
    
    print("length of combined_data list : ", len(combined_data))
    return combined_data


# 1차 : 불러오기 완료한 영화 데이터 리스트
first_lst = update_movie()


def data_store():
    Movie.objects.all().delete()

    for data in first_lst:
        # 단일 레코드 인스턴스 생성
        movie = Movie()
        
        movie.code = data.get('id')
        movie.title = data.get('title')
        movie.title_origin = data.get('original_title')
        movie.release_date = data.get('release_date')
        movie.status = False
        movie.overview = data.get('overview')
        movie.language = data.get('original_language')
        movie.poster = data.get('poster_path')
        
        movie.save()

data_store()
'''






'''
### movie 테이블 status 필드값 업데이트 코드
def update_movie_status():
    movies = Movie.objects.all()
    
    for movie in movies:
        movie_id = movie.code
                
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=ko_KR"

        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {settings.SECRET_KEY}"
        }

        response = requests.get(url, headers=headers)
        status = response.json().get("status")
        
        if status == 'Released':
            movie.status = True
        else:
            movie.status = False
        
        movie.save()

update_movie_status()
'''






'''
### genre 테이블 seed data 관련 코드
def update_genre():
    URL_GENRE = "https://api.themoviedb.org/3/genre/movie/list?language=ko"

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {settings.SECRET_KEY}"
    }

    response = requests.get(URL_GENRE, headers=headers)
    print(response.json())
    datas = response.json().get('genres')
    
    Genre.objects.all().delete()
    
    for data in datas:
        genre = Genre()
        
        genre.code = data.get('id')
        genre.name = data.get('name')
        
        genre.save()

update_genre()
'''







'''
### hashtag 테이블 seed data 관련 코드
def update_hashtag():
    hashtags = [
        "감동영화", "재밌는영화", "스릴넘치는", "명작영화", "눈물샘자극", "힐링영화", "긴장감", "인생영화", "감성영화", "여운남는", 
        "웃긴영화", "가족영화", "로맨틱", "공포영화", "액션영화", "서스펜스", "드라마영화", "감동적인", "재미있는", "기분좋은", 
        "대박영화", "눈물나는", "웃음터짐", "설레는", "소름돋는", "감성자극", "흥미진진", "웃음폭발", "진한여운", "긴장감있는", 
        "따뜻한영화", "무서운영화", "잔잔한감동", "흥미로운", "멋진영화", "기대되는", "생각하게하는", "환상적인", "몰입감", "강추영화", 
        "가슴뭉클", "재밌음", "소름", "잊지못할", "영화추천", "신나는", "코미디영화", "슬픈영화", "놀라운", "충격적인", 
        "공감되는", "매력적인", "흥미유발", "흥미롭다", "이야기꾼", "독특한영화", "재밌다", "짜릿한", "여운", "호러영화", 
        "눈물버튼", "서사적", "대서사시", "서정적인", "예술영화", "영화의밤", "감탄사", "새로운시도", "인상적인", "극적전개", 
        "상상초월", "비극적", "따뜻한", "우정영화", "음악영화", "감동받다", "기억에남는", "새로운발견", "반전있는", "유쾌한", 
        "애니메이션영화", "고전영화", "명작추천", "강력추천", "웃긴", "진지한", "심오한", "독립영화", "멜로영화", "감명깊은", 
        "철학적", "의미있는", "휴먼드라마", "스펙터클", "반전영화", "눈물샘", "웃음가득", "화제작", "카리스마", "삶의교훈"
    ]

    HashTag.objects.all().delete()

    for tag in hashtags:
        hashtag = HashTag()
        
        hashtag.tag = tag
        hashtag.save()

update_hashtag()
'''







'''
### actor 테이블 seed data 관련 코드
def update_actor():
    movies = Movie.objects.all()
    for movie in movies:
        movie_id = movie.code
    
        url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?language=ko-KR"

        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {settings.SECRET_KEY}"
        }

        response = requests.get(url, headers=headers)
        datas = response.json().get('cast')
        
        if datas == None:
            continue
        
        for data in datas:
            if data.get('known_for_department') != 'Acting':
                continue
            
            actor = Actor()
            
            actor.code = data.get('id')
            actor.name = data.get('name')
            actor.profile = data.get('profile_path')
            actor.save()
            
            actor.movie.add(Movie.objects.get(pk=int(movie_id)))

update_actor()
'''





'''
### genre_movie M:N 테이블 seed data 관련 코드
def update_genre_movie():
    movies = Movie.objects.all()
    
    for movie in movies:
        movie_id = movie.code
        
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=ko_KR"

        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {settings.SECRET_KEY}"
        }

        response = requests.get(url, headers=headers)
        datas = response.json().get("genres")
        
        for data in datas:
            genre_id = int(data.get('id'))
            
            genre = Genre.objects.get(pk=genre_id)
            genre.movie.add(movie)

update_genre_movie()
'''