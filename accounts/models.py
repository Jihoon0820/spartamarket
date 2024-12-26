from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # AbstractUser를 상속받아 기본 사용자 모델을 확장
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    bio = models.TextField(blank=True, max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # 팔로우 기능을 위한 M2M 필드
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    
    def __str__(self):
        return self.username