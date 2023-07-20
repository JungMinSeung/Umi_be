from rest_framework.views import APIView
from rest_framework.response import Response
from .models import LoginUser
from django.contrib.auth.hashers import make_password, check_password
from .serializer import LoginUserSerializer

class AppLogin(APIView):
    def post(self, request):
        user_id = request.data.get('user_id', "")
        user_pw = request.data.get('user_pw', "")
        user = LoginUser.objects.filter(user_id=user_id).first()
        
        if user is None:
            return Response(dict(msg="해당 ID의 사용자가 없습니다."))
        if check_password(user_pw, user.user_pw) is False:
            return Response(dict(msg="로그인 성공", user_id=user.user_id, birth_day=user.birth_day,
                                gender=user.gender, email=user.email, name=user.name, age=user.age))
        else:
            return Response(dict(msg="비밀번호가 일치하지 않습니다."))
        
class RegistUser(APIView):
    def post(self, request):
        serializer = LoginUserSerializer(data=request.data)
        
        if LoginUser.objects.filter(user_id=serializer.data["user_id"]).exists():
            user = LoginUser.objects.filter(user_id=serializer.data["user_id"]).first()
            data = dict(
                msg="이미 존재하는 ID입니다.",
                user_id=user.user_id,
                user_pw=user.user_pw,
            )
            return Response(data)
        
        user = serializer.create(serializer.data)
        
        return Response(data=LoginUserSerializer(user).data)