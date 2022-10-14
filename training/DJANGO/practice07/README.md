로그인

#### HTTP 특징

- 비 연결 지향`connectionless`

  서버는 요청에 대한 응답을 보낸 후 연결을 끊음

- 무상태`stateless`

  연결을 끊는 순간 클라이언트와 서버 간 통신이 끝나며 상태 정보가 유지되지 않음

  클라이언트와 서버가 주고 받는 메세지는 완전 독립적

<br>

#### 로그인 상태를 유지하는 방법

- 서버와 클라이언트 간 지속적 상태 유지를 위해 `쿠키`와 `세션`이 있다

<br>

#### 쿠키

- 서버가 클라이언트에 전송하는 작은 데이터 조각

- 사용자가 웹사이트를 방문할 경우 웹 서버를 통해 사용자 컴퓨터에 설치되는 작은 기록 정보 파일

  > 클라이언트는 쿠키를 로컬에 Key-Value 데이터 형식으로 저장
  >
  > 동일한 서버 재요청 시 저장된 쿠키를 함께 전송

- 서로 다른 요청이 동일한 브라우저에서 발생한 것인지 판단할 때 사용됨

  > 무상태 HTTP에서 상태 정보를 관리, 사용자는 로그인 상태를 유지

<br>

#### 쿠키 사용 목적

- 세션 관리

  로그인, 아이디 자동완성, 공지 하루 안 보기, 팝업 체크, 장바구니 등 정보관리

- 개인화

  사용자 선호, 테마 등의 설정

- 트래킹

  사용자 행동을 기록, 분석

<br>

#### 쿠키 Lifetime

- Session cookie

  현재 세션이 종료되면 삭제, 브라우저 종료와 함께 세션이 삭제됨

- Persistent cookies

  Expires 속성에 지정된 날짜 혹은 Max-Age 속성에 지정된 기간이 지나면 삭제

<br>

#### 세션

- 사이트와 특정 브라우저 사이의 상태`state`를 유지시키는 것

- 클라이언트가 서버에 접속하면 서버가 특정 `세션 ID`를 발급, 클라이언트는 `세션 ID`를 쿠키에 저장

  > 쿠키는 요청 때마다 서버에 함께 전송되므로 세션 ID를 확인해 알맞은 로직 처리

- `세션 ID`는 세션을 구별하기 위해 필요, 쿠키에는 `세션 ID`만 저장

<br>

#### AuthenticationForm

- 로그인을 위한 Built-in-form

  로그인하는 사용자 정보를 입력 받음

  `ModelForm`이 아닌 일반 Form을 상속 받고 있으며, `request`를 첫번째 인자로 취함

<br>

#### login()

- login(request, user, backend=None)

- 인증된 사용자 로그인

  > 유저 ID를 세션에 저장해 세션을 기록 

- HttpRequest 객체와 User 객체가 필요

  > 유저 정보는 반드시 인증된 유저 정보여야 함
  >
  > `authenticate()`함수를 활용한 인증
  >
  > `AuthenticationForm`을 활용한 is_valid

  ```python
  # views.py
  
  from django.contrib.auth import login as auth_login
  
  def login(request):
    if request.method == 'POST':
      form = AuthenticationForm(request, data=request.POST)
      if form.is_valid():
        auth.login(request, form.get_user())
        return redirect('articles:index')
    else:
      form = AuthenticationForm()
    context = {
      'form': form
    }
    return render(request, 'accounts/login.html', context
  ```

- ModelForm 기반의 Create 로직과 동일하지만 필수 인자 구성이 다름

  > DB에 저장하는 것 대신 세션에 유저를 기록하는 함수를 호출
  >
  > 로그인 URL`/accounts/login/`에서 변경될 때 settings에서 `LOGIN_URL`을 변경해야 함

<br>

#### get_user()

- AuthenticationForm의 인스턴스 메소드
- 유효성 검사를 통과했을 경우 로그인 한 사용자 객체를 반환

