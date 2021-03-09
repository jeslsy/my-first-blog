# from, import = 다른 파일에 있는 것을 추가
# ex) 장고.conf로 부터 settings 기능?함수?를 가져다 쓰겠음
from django.conf import settings
from django.db import models
from django.utils import timezone

# class = 객체 정의하겠다.
# Post = 객체(모델)이름
# models = 이 객체가 장고의 모델임을 의미. 그래서 Post를 데베에 저장할 것임.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # CharField = 글자 수 제한된 짧은 문자열
    title = models.CharField(max_length=200)
    # TextField = 글자 수 제한 없는 문자열
    text = models.TextField()
    # DataTimeField = 날짜와 시간
    created_date = models.DateTimeField(
            # 지금 시간
            default=timezone.now)
    published_date = models.DateTimeField(
            # 필드(열) 비워둘 것인지 설정 = 어떤 조건으로든 값을 비워둘 수 있음
            blank=True, null=True)

    # 현재 시간가져와 게시일로 저장.
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # title 반환해줌
    def __str__(self):
        return self.title