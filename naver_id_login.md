# 네이버 아이디로 로그인하기 연동 





## 1. 세션 유지 및 위조 방지용 상태 토큰 



웹 어플리케이션은 브라우저를 기반으로 작동. 

사이트 간 요청 위조 (cross-site request forgery) 공격 위험이 존재. CSRF 공격을 방지하기 위해서 어플리케이션과 사용자 간의 상태를 보유하는 고유한 세션 토큰을 만들어야 함. 



나중에 인증 과정의 결과값으로 전달하는 세션 토큰과 일치하는지 확인해 사용자가 요청하지 않은 요청과 사용자가 요청한 요청을 확인할수 있음. 이 세션 토큰을 '상태 토큰 (state token) 이라 하며, 



상태 토큰의 값은 사용자가 네이버 로그인을 진행하는 동안 유지되어야 하고 고유한 값이어야 함. 





**1. 네이버 아이디로 로그인 인증 요청문 생성**



상태 토큰을 생성후 네이버 로그인 페이지를 호출하는 인증 요청문 (authentication request)을 생성 하도록 함. 

인증 요청문은 URL 형식으로 되어 있으며, 네이버가 제공하는



- 인증 URL 
- Client ID 
- State Token 



인증 과정은 HTTPS 통신으로 이루어지며, 인증 요청문 형식은 아래와 같음. 



```python
https://nid.naver.com/oauth2.0/authorize?
    client_id={클라이언트 아이디}&
    response_type=code&
    redirect_uri={개발자 센터에 등록한 콜백 URL(URL 인코딩)}&
    state={상태 토큰}
    
    
# client_id : 어플리케이션 등록 후 발급받은 클라이언트 아이디 
# response_type: 인증 과정에 대한 구분값. code 로 값이 고정되어 있음. 
# redirect_uri : 네이버 로그인 인증의 결과를 전달받을 콜백 URL (URL 인코딩)
# 어플리케이션을 등록할때 Callback URL에 설정한 정보 
# state: 어플리케이션이 생성한 상태 토큰 

login_base_url = 'https://nid.naver.com/oauth2.0/authorize'
login_params = {
    'client_id': 'client_id',
    'response_type': 'code',
    'redirect_uri': 'http://localhost:8000/members/naver-login/',
    'state': 'RANDOM_STATE',
}
login_url = '{base}?{params}'.format(
		base=login_base_url,
		params='&'.join([f'{key}={value}' for key, value in login_params.items()])
)

context = {
    'login_url': login_url,
}

return render(request, 'members/login.html', context)
```



## 

**2. 접근 토큰 요청**

상태 토큰에 대한 검증이 성공적으로 끝났다면, 응답으로 전달받은 인증 코드를 이용해 최종 인증 값인 접근 토큰을 발급 받는다. 



인증 코드는 "ioejfokeji3o822"와 같이 랜덤으로 생성된 값이다. 

인증 코드는 접근 토큰을 발급할 때 1번만 사용하며, 이미 사용한 인증 코드는 더 이상 사용할수 없ㅅ다. 



접근 토큰 요청 과정은 모두 서버간 HTTPS 통신으로 이루어지고. 완성된 요청문은 다음과 같은 URL  형식 





```python
https://nid.naver.com/oauth2.0/authorize?
    client_id={클라이언트 아이디}&
    response_type=code&
    redirect_uri={개발자 센터에 등록한 콜백 URL(URL 인코딩)}&
    state={상태 토큰}
    
    
    # clinet_id : 어플리케이션 등록 후 발급받은 클라이언트 아이디 
    # client_secret : 어플리케이션 등록 후 발급받은 클라이언트 시크릿 
    # grant_type : 인증 타입에 대한 구분값. authorization_code로 값이 고정되어 있음 
    # state : 어플리케이션이 생성한 상태 토큰 
    # code : 콜백으로 전달받은 인증 코드 
    
def naver_login(request):
    code = request.GET.get('code')
    state = request.GET.get('state')
    if not code or not state:
        return HttpResponse('code또는 state가 전달되지 않았습니다')
    
    token_base_url = 'https://nid.naver.com/oauth2.0/token'
    token_params = {
        'grant_type': 'authorization_code',
        'client_id': 'client_id',
        'client_secret': 'client_secret',
        'code': code,
        'state': state,
        'redirectURI': 'https://localhost:8000/members/naver-login',
    }
    token_url = '{base}?{params}'.format(
    	base=token_base_url,
    	params='&'.join([f'{key}={vlaue}' for key, value in token_params.items()]))
    
    response = reqeusts.get(token_url)
    access_token = response.json()['access_token']
    print(access_token)
    
    
    
    
```



접근 토큰 요청에 성공하면, 접근 토큰과 갱신 토큰이 포함된 JSON  형식의 결괏겂을 반환받습니다. 접근 토큰은 expires_in 속성에 설정된 시간 동안 유효. 유효 기간이 지난뒤에는 갱신 토큰을 사용해 접근 토큰을 다시 발급 받아야함. 



```json
{
    "access_token": "AAAAQosjWDJieBiQZc3to9YQp6HDLvrmyKC+6+iZ3gq7qrkqf50ljZC+Lgoqrg",
    "refresh_token": "c8ceMEJisO4Se7uGisHoX0f5JEii7JnipglQipkOn5Zp3tyP7dHQoP0zNKHUq2gY",
    "token_type": "bearer",
    "expires_in": "3600"
}
```



**3. 네이버 사용자 프로필 정보 조회**



접근 토큰을 성공적으로 발급받았다면, 접근 토큰을 이용해 네이버 사용자의 프로필 정보를 조회 할수 있음. 

사용자 프로필 정보는 사용자를 구분할수 있는 식별값인, 아이디와 별명, 메일주소와 같은 사용자 정보를 포함하고 있습니다. 



사용자 프로필 정보 조회 요청 URL 



https://openapi.naver.com/v1/nid/me



요청 할때는 다음과 같은 형식으로 접근 토큰을 포함하는 요청 헤더를 보냅니다. 요청 헤더에 포함하는 토큰 타입은 Bearer 입니다. 



Authorization : {토큰타입} {접근 토큰} 



```
me_url = 'https://openapi.naver.com/v1/nid/me'
me_headers = {
'Authorization': f'Bearer {access_token}',
}
me_response = requests.get(me_url, headers=me_headers)
me_response_data = me_response.json()

unique_id = me_response_data['response']['id']

naver_username = f'n_{unique_id}'
if not User.objects.filter(username=naver_username).exists()
	user = User.objects.create_user(username=naver_username)
else: 
	user = User.objects.get(username=naver_username)
	login(request, user)
	return redirect('index')
```

