from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Fcuser
from django.contrib.auth.hashers import make_password, check_password
from .forms import LoginForm

# Create your views here.

def home(request):
    user_id = request.session.get('user')

    if user_id:
        fcuser = Fcuser.objects.get(pk=user_id)
        return HttpResponse(fcuser.username)
    
    return HttpResponse('Home!')
    
def logout(request): 
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')

def login(request):
    form = LoginForm()
    return render(request, 'login.html', {'form':form})

    # if request.method == 'GET': 
    #     return render(request, 'login.html')
    # elif request.method == 'POST':
    #     username = request.POST.get('username', None)
    #     password = request.POST.get('password', None)
        
    #     res_data = {}

    #     if not (username and password): 
    #         res_data['error'] = "모든값을 입력해야 합니다."
    #     else:
    #         fcuser = Fcuser.objects.get(username=username)
    #         if password == fcuser.password:
                
    #             request.session['user'] = fcuser.id   

    #             return redirect('/')

    #         # '/' 만 써주면, 현재 사이트의 루트로 이동 
            
    #         # 비밀번호가 일치, 로그인 처리 
                
    #             # dfdf	333434
    #         else:
    #             res_data['error'] = '비밀번호가 틀렷습니다.'
    #             print(fcuser.username)
    #             print(fcuser.password)
    #             print(fcuser.id)
    #             print(password)

        # return render(request, 'login.html', res_data)


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


# 세션이란 무엇인가? 
# 