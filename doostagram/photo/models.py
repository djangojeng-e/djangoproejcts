from django.db import models

# Create your models here.


from django.contrib.auth.models import User
from django.urls import reverse


class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos')
    # related_name = 'user_photos'
    # 연결된 객체에서 하위 객체의 목록을 부를 때 사용.
    # 예 ) User 객체에 달려있는 photo user_photos
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/no-image.png')
    # 사진필드. upload_to 는 사진이 업로드 될 경로를 설정, 업로드가 되지 않을경우 기본값으로 대신
    text = models.TextField()
    # 문자열의 길이에 제한이 없는 텍스트필드

    created = models.DateTimeField(auto_now_add=True)
    # 글 작성일을 저장. auto_now_add = True
    updated = models.DateTimeField(auto_now=True)
    # 글 수정일을 저장. auto_now=True

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.author.username + " " + self.created.strftime("%Y-%m-%d %H:%M:%S")

# author -> Foreign 키를 사용해서 User 테이블과 관계를 만듦
# User 모델은 장고에서 기본적으로 사용하는 사용자 모델
# on_delete = CASCADE : 연결된 모델이 삭제될 경우 어떻게 할지 함. CASCADE는 연결된 객체가 삭제되면 해당 객체도 같이 삭제
# CASCADE
# PROTECT   : 하위 객체가 남아 있으면, 연결된 객체가 지워지지 않음.
# SET_NULL  : 연결된 객체를 삭제하고, 필드값을 null로 설정
# SET()     : 연결된 객체만 삭제하고, 지정한 값으로 변경
# DO_NOTHING : 아무 엑션도 취하지 않음.

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[str(self.id)])

# get_absolute_url 객체의 상세 페이지의 주소를 반환
# reverse -> URL 패턴 이름을 가지고, 해당 패턴을 찾아 주소를 만들어줌.

