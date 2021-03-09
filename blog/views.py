from django.shortcuts import render, get_object_or_404
# 글 작성한 다음에 바로 post_detail 페이지로 가기 위해 사용
from django.shortcuts import redirect
from django.utils import timezone
#같은 폴더인 blog에 있는 models라는 파일에서 Post 객체 가져오겠다.
from .models import Post 
from .forms import PostForm



def post_list(request):
    # 글목록을 게시일 기준으로 정렬
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # 글 목록을 함께 html로 반환
    return render(request, 'blog/post_list.html', {'posts': posts})

    
def post_detail(request,pk):
    post = get_object_or_404(Post, pk = pk)
    return render(request, 'blog/post_detail.html', {'post':post})


def post_new(request):
    # 템플릿에서 <form method="POST"이렇게 지정함. (템플릿 -> URL -> VIEW)
    if request.method == "POST":
        # 데이터 받는 매개변수..?
        form = PostForm(request.POST)
        # 값이 유효한지 검사
        if form.is_valid():
            # 작성자 추가하고 저장하기 위해 바로 저장하지 말라고 제지.
            post = form.save(commit=False)
            # post 객체의 author에 넘어온 작성자 저장.
            post.author = request.user
            # post 객체에 게시일 변수에 현재 시간을 저장.
            post.published_date = timezone.now()
            # 변경사항 유지 + 새 블로그 글 만들어짐.
            post.save()
            # post_detail은 pk 번호 필요하니까 함께 redirect url 다시 쏴줌.
            return redirect('post_detail', post.pk)
    else:
        # POST형식 아니면~ (맞나..?^)
        form = PostForm()
    # view에서 사용하던 파이썬 변수를 html템플릿으로 넘겨주면서 화면에 띄우는것.
    return render(request, 'blog/post_edit.html', {'form': form})
    


def post_edit(request, pk):
    # 수정하려는 글의 Post모델 인스턴스로 가져옴 (pk로 원하는 글 찾는것.)
    post = get_object_or_404(Post, pk=pk)
    # POST 형식이면
    if request.method == "POST":
        # ???
        form = PostForm(request.POST, instance=post)
        # 값이 유효한지 검사
        if form.is_valid():
            # 작성자 넣기 전에 바로 저장하지 않게 
            post = form.save(commit=False)
            # 작성자를 post객체 author변수에 넣음
            post.author = request.user
            # 게시일에 현재 시간 넣음
            post.published_date = timezone.now()
            # 변경사항 유지 + 저장
            post.save()
            # 다시 post_detail 페이지 url 쏴줌
            return redirect('post_detail', post.pk)
    else:
        # ??? 몰까 객체 인스턴스를 가져오는 곤가
        form = PostForm(instance=post)
    # 파이썬 변수 form과 함께 post_edit 템플릿 화면 보여줌.
    return render(request, 'blog/post_edit.html', {'form': form})


