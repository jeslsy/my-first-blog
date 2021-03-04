from django.shortcuts import render
from django.utils import timezone
from .models import Post 
#같은 폴더인 blog에 있는 models라는 파일에서 Post 객체 가져오겠다.


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
# Create your views here.
