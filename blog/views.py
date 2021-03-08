from django.shortcuts import render, get_object_or_404
from django.utils import timezone
#같은 폴더인 blog에 있는 models라는 파일에서 Post 객체 가져오겠다.
from .models import Post 



def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

    
def post_detail(request,post_id):
    post = get_object_or_404(Post, pk = post_id)
    return render(request, 'blog/post_detail.html', {'post':post})
