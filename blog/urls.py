# django.urls라는 곳에서 path라는 기능을 가져다 쓰겠다.
from django.urls import path
# 현재 폴더에서 views파일을 가져다 쓰겠다 ?
from . import views


urlpatterns = [
    # http://127.0.0.1:8000/ 뒤에 아무 것도 없는 모든 url을 view와 대조해 찾아냄
    path('', views.post_list, name = 'post_list'),
    # 이 패턴이 맞으면 post_detail이라는 view에 간다는 것
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/',views.post_new, name = 'post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]