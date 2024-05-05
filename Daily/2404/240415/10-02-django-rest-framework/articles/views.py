from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from .models import Article, Comment
from django.shortcuts import get_object_or_404, get_list_or_404


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        # articles = Article.objects.all()
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(
            article, data=request.data, partial=True
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        # 전체 댓글 조회
        # comments = Comment.objects.all()
        comments = get_list_or_404(Comment)
        # 직렬화 진행
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    # 단일 댓글 조회
    # comment = Comment.objects.get(pk = comment_pk)
    comment = get_object_or_404(Comment, pk = comment_pk)

    if request.method == 'GET':
        # 직렬화 진행
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def comment_create(request, article_pk):
    # 게시글 조회
    # article = Article.objects.get(pk = article_pk)
    article = get_object_or_404(Article, pk = article_pk)
    
    # 사용자 입력 데이터를 받아 직렬화를 진행
    serializer = CommentSerializer(data=request.data)
    # 유효성 검사 (article까지 검사해서 에러가 날 수 있음 -> 유효성 검사에서는 제거하고 데이터 조회 시에는 출력 설정되어야 함)
    if serializer.is_valid(raise_exception=True):
        # 이름만 같고 restapi 역할이기 때문에 기존에 쓰던 commit을 사용하는 게 아니라
        # 인자로 외래키를 바로 넣어줘야 함
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)