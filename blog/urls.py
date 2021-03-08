from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name = 'post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    # post_detail이라는 이름으로 views.post_detail이라는 뷰를 path에 연결한다는 패턴
]