from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name = 'post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # post_detail이라는 이름으로 views.post_detail이라는 뷰를 path에 연결한다는 패턴
    path('post/new/',views.post_new, name = 'post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]