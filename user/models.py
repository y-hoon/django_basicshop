from django.db import models


# Create your models here.
class User(models.Model):
    emaiil = models.EmailField(verbose_name='이메일')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    regiter_date = models.DateTimeField(auto_now_add=True, verbose_name='등록일자')

    class Meta:
        db_table = 'yh_user'
        verbose_name = '회원'
        verbose_name_plural = '회원'
