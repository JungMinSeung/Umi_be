from django.db import models

class LoginUser(models.Model):
    user_id = models.CharField(max_length=20, null=False, default=False)
    user_pw = models.CharField(max_length=255, null=False, default=False)
    
    birth_day = models.DateField(verbose_name='생년월일', null=True)
    gender = models.CharField(verbose_name='성별', max_length=10, null=False, default='male')
    email = models.EmailField(verbose_name='이메일', max_length=255, null=False, default="")
    name = models.CharField(verbose_name='이름', max_length=20, null=False, default="")
    age = models.IntegerField(verbose_name='나이', null=False, default=20)
    
    
    class Meta:
        db_table = 'login_user'
        verbose_name = '로그인 테스트 테이블'