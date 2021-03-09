"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# 
from django.contrib import admin
# 1.include = 다른 URLconf를 참조할 수 있게 도와줌 (blog.urls 사용 가능)
# 2.여기서 URLconf는 URL과 일치하는 뷰를 찾아주는 기능가짐.
# 3.admin.site.urls를 제외한건 다 include 써야됨
# 4.blog/urls.py에 url등록하면 -> 최상위 URLconf인 mysite/urls.py에 
#   include()를 이용해 blog.urls전체를 등록하게 되는것.
from django.urls import path, include

urlpatterns = [
    # admin/으로 들어오는 접속을 admin.site.urls (admin사이트로 보내주는 듯 ?)
    path('admin/', admin.site.urls),
    # http://127.0.0.1:8000/ 여기로 들어오는 모든 접속을 blog.urls로 전송해 추가 명령 찾게함
    path('', include('blog.urls')),
]
