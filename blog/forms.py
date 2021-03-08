#forms 모델을 import
from django import forms

# Post 모델도 import
from .models import Post


# PostForm이름으로 폼 만들것.
# ModelsForm임 = 장고가 어떤 마술 부릴거래.
class PostForm(forms.ModelForm):

    #이 폼 만들기 위해 어떤 model이 쓰이는지 알려줌 
    class Meta:
        #(model = Post 쓸 것.)
        model = Post
        fields = ('title', 'text',)
