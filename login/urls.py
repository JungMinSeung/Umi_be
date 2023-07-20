from django.urls import re_path as url
from . import views

urlpatterns = [
    url('regist_user', views.RegistUser.as_view(), name='regist_user'),
]