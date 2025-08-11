from django import forms 
from .models import Article

# class ArticleForm(forms.Form):
#     # max_length가 필수 인자가 아니며, textfield가 없음
#     # max_length가 제약 조건은 아님, 그냥 속성 정도, 바꿀 수 있음
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)

# model form이 meta를 통해서 알아서 model과 매칭시켜서 만들어줌
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label ='제목',
        widget=forms.TextInput(
            attrs = {
                'class' : 'my-title',
                'placeholder' : 'Enter the title'
            }
        )
    )

    class Meta:
        # 어떤 모델과 연동?
        model = Article

        # 그 모델에서 어떤 필드를 쓸지
        # 부분 선택시
        # fields = ('title', 'content')
        # 전체 선택시
        fields = '__all__'
        # 특정 model 제외하는 경우
        # exclude = ('title')