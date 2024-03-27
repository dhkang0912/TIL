from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


# def new(request):
#     # ArticleForm을 사용
#     form = ArticleForm()
#     context = {
#         'form' : form,
#     }
#     return render(request, 'articles/new.html', context)


# def create(request):
#     # title = request.POST.get('title')
#     # content = request.POST.get('content')
#     # article = Article(title=title, content=content)
#     # article.save()

#     form = ArticleForm(request.POST)
#     # 유효성 검사
#     if form.is_valid():
#         # 저장된 객체를 반환해줌
#         article = form.save()
#         return redirect('articles:detail', article.pk)
    
#     # is_valid가 False이면 에러가 나는 이유를 가져다줌
#     context = {
#         'form' : form,
#     }
#     # 에러 난 경우 입력하던 곳을 다시 보여주면서 에러 메시지를 띄워줌
#     return render(request, 'articles/new.html', context)
#     # return redirect('articles:detail', article.pk)

def create(request):
    form = ArticleForm(request.POST)
    if request.method == 'POST': # POST일 때만 봐야 함
        # 유효성 검사, Create
        if form.is_valid():
            # 저장된 객체를 반환해줌
            article = form.save()
            return redirect('articles:detail', article.pk)
    # if, else 내용 순서를 바꾸면 GET이 아닐 때 모두 유효성 검사를 하게 됨
    else: # GET 일때? X => POST가 아닌 다른 모든 경우, 
        form = ArticleForm()
    
    # POST method라서 들어갔지만 valid가 False인 경우 에러 메시지를 가지고 들여쓰기가 동일한 위치인 context로 옴
    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form' : form
    }
    return render(request, 'articles/edit.html', context)


def update(request, pk): 
    # title = request.POST.get('title')
    # content = request.POST.get('content')

    # article.title = title
    # article.content = content
    # article.save()

    article = Article.objects.get(pk=pk)
    # 생성과 수정을 구분해줘야 함 -> instance 키워드로 달라짐 (기존 객체 넣기)
    form = ArticleForm(request.POST, instance=article)
    if form.is_valid():
        form.save()
        return redirect('articles:detail', article.pk)
    
    context = {
        'form' : form,
        'article' : article,
    }
   

    return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    
    context = {
        'form' : form,
        'article' : article,
    }
    return render(request, 'articles/edit.html', context)



