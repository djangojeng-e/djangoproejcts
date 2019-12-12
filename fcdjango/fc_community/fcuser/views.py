from django.shortcuts import render
from django.http import HttpResponse
from .models import Fcuser
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.

def login(request):
    if request.method == "GET": 
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        
        res_data = {}

        if not (username and password): 
            res_data['error'] = "모든값을 입력해야 합니다."
        else:
            fcuser = Fcuser.objects.get(username=username)
            if check_password(password, fcuser.password):
            
            
            # 비밀번호가 일치, 로그인 처리 
                
                pass
            else:
                res_data["error"] = "비밀번호가 틀렷습니다."

        return render(request, 'login.html', res_data)


def register(request):
    if request.method == "GET":
        return render(request, 'register.html') # 경로는 template 폴더를 바라보고 있기때문에 자동으로 찾음
    elif request.method == "POST":
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        repassword = request.POST.get('repassword', None)
        
        res_data = {}

        # if not (username and password and repassword):
        #     res_data['error'] = "모든필드를 입력해야 합니다."
        if password != repassword:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            fcuser = Fcuser(
                username = username,
                useremail = useremail,
                password = make_password(password) 
            )

            fcuser.save()
        return render(request, 'register.html', res_data)


