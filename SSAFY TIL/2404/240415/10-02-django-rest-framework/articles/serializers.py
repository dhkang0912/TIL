from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)


class ArticleSerializer(serializers.ModelSerializer):
    class CommentDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('id', 'content',)

    # 역참조 매니저 필드를 생성해줘야 함, 조회하는 걸 유효성 검사할 것이 아니기 때문
    # 여러개 하면 many를 넣어줘야 함
    # 여기서 역참조 매니저 이름으로 가는 변수는 정해져있음, 역참조 매니저 이름으로만 가능함
    comment_set = CommentDetailSerializer(read_only = True, many = True) 
    comment_count = serializers.IntegerField(source = 'comment_set.count', read_only = True)

    class Meta:
        model = Article
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class ArticleTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title',)

    article = ArticleTitleSerializer(read_only = True)
    # article = ArticleListSerializer(read_only = True)


    class Meta:
        model = Comment
        fields = '__all__'
        # read_only_fields = ('article',)