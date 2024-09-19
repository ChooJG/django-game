from django.db import models
from django.contrib.auth.hashers import make_password, check_password


# Create your models here.
class User(models.Model):
    nickname = models.CharField(max_length=30)
    userid = models.CharField(max_length=30, unique=True)  # 아이디는 고유해야 함
    password = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # 비밀번호가 이미 해시된 상태인지 확인 후 해싱 처리
        if not self.pk or not check_password(self.password, self.password):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nickname