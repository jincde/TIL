## Django Auth

Django 인증 시스템은 인증`Authentication`과 권한`Authorization` 부여를 함께 제공

- User
- 권한 및 그룹
- 암호 해시 시스템
- Form 및 View 도구
- 기타 적용가능 시스템

```django
project/settings.py

INSTALLED_APPS = [
	...
	'django.contribu.auth',
	...
]
```

<br>

#### Authentication(인증)

신원 확인

사용자가 자신이 누구인지 확인

####  Authorization(권한, 허가)

권한 부여

인증된 사용자가 수행할 수 있는 작업을 결정

<br>

### 설정

- **accounts app 생성/등록**

  ```bash
  $ python manage.py startapp accounts
  ```

  ```python
  INSTALLED_APPS = [
    'articles',
    'accounts',
  ]
  ```

  > auth와 관련한 경로나 키워드들을 django 내부에서 accounts로 사용하고 있기 때문에 accounts로 지정하는 것을 권장

- **urls.py 설정**

  ```python
  # project/urls.py
  
  urlpatterns = [
    path('accounts/', include('accounts.urls')),
  ]
  ```

  ```python
  # accounts/urls.py
  
  app_name = 'accounts'
  # URL을 변수화
   
  urlpattenrns = [
    
  ]
  ```

- **Django User Model**

  기본적인 인증 시스템, 여러 필드가 포함된 User Model 제공,

  대부분 개발 환경에서 Custom User Model로 대체,

  커스텀 User 모델을 설정하는 것을 강력히 권장`highly recommended`

  > 모델 대체 작업은 프로젝트의 모든 migrations, 첫 migrate를 실행 전 끝내야 함

- **AUTH_USER_MODEL**

  User를 나타낼 때 사용하는 모델 

  프로젝트 진행 중 (마이그레이션 후) 변경할 수 없음

  프로젝트 시작 시 설정, 참조하는 모델은 첫 마이그레이션에서 사용할 수 있어야 함(첫 마이그레이션 전에 확정지어야 함)

  ```python
  # project/setting.py
  
  AUTH_USER_MODEL = 'auth.User'
  ```

- **커스텀 유저 모델 대체**

  AbstractUser를 상속받는 커스텀 User 클래스 작성

  기존 User 클래스도 AbstractUser를 상속받기 때문에 커스텀 User 클래스도 같은 모습

  ```python
  # accounts/models.py
  
  from django.contrib.auth.models import AbstarctUser
  
  class User(AbstractUser):
    pass
  ```

  ```bash
  $ python manage.py makemigrations
  $ python manage.py migrate
  ```

  ```bash
  $ python manage.py createsuperuser
  
  # accounts_user에서 admin 정보 확인
  # user model 사용 준비 완료
  ```

  > User 모델 상속 관계
  >
  > models.Model > class AbstractBaseUser > class AbstractUser > class User

- 암호 관리

  회원가입시 일반적으로 암호 저장이 필수적, 별도의 처리가 필요하다

  > Django 기본 `PBKDF2`를 사용해 저장

  단방향 해시함수를 활용해 비밀번호를 다이제스트로 암호화하며 복호화 불가

  > MD5, SHA-1, SHA-256등이 존재, Django에서는 SHA-256 활용

  User 객체는 `objects.create()`코드를 사용해 생성하면 안됨

  > 패스워드 암호화가 필요
  >
  > 암호화된 코드를 반대로 복호화가 불가능해야 한다

  해시함수 : 복호화가 불가능한 단방향 함수

  > 이미 MD5, SHA-1 알고리즘은 뚫림. 레인보우 테이블, 브루트포스 공격 이슈
  >
  > 솔팅`salting` : 같은 암호라도 개개인마다 특수 문자열을 추가해 레인보우 공격을 방어
  >
  > 키 스트레칭 : 브루트포스 공격을 방어

  User 객체 활용`.create_user() 메소드`

  ```python
  # User 생성
  
  user = User.objects.create_user('john', 'john@email.com', '1q2w!')
  ```

  > 자동으로 패스워드가 암호화되어 저장

  ```python
  # User 비밀번호 변경
  
  user = user.objects.get(pk=2)
  User.set_password('new password')
  User.save()
  ```

  > .set_password() 메소드도 패스워드 변경시 자동으로 암호화

  ```python
  # User 인증(비밀번호 확인)
  
  from django.contrib.auth import authenticate
  
  user = authenticate(username='john', password='secret')
  ```

  > authenticate(username='ss', password='12') 비밀번호가 틀리면 User 객체를 반환하지 않음

<br>

---

## 회원가입 기능 구현

```python
# accounts/urls.py

from django.urls import path

app_name = 'accounts'

urlpatterns = [
  path('signup/', views.signup, name='signup'),
]
```

```python
# accounts/views.py

from django.contrib.auth.forms import UserCreationForm

def signup(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    
    if form.is_valid():
      form.save()
      return redirect('articles:index')
    
  else:
    form = UserCreationForm()
  
  context = {
    'form' : form
  }
  
  return render(request, 'accounts/signup.html', context)
```

```python
# accounts/forms.py (생성)

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomerCreationForm(UserCreationForm):
  
  class Meta:
    model = get_user_model()
    fileds = ('username', 'password1', 'password2', 'email')
    labels = {
      'username': '닉네임',
      'password1': '비밀번호',
      'password2': '비밀번호 확인',
      'email': '이메일'
    }
```

> 기존 UserCreationForm을 상속 받아 User 모델 재정의
>
> `get_user_model()`으은 현재 프로젝트에서 활성화된 사용자 모델을 반환

```python
# accounts/views.py

from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:     
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)
```

> VIEW에 반영하기

```python
# accounts/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

admin.site.register(get_user_model(), UserAdmin)
```

> admin 사이트에서 회원정보 조회가능

<br>

## 프로필 조회

```python
# accounts/urls.py

app_name = 'accounts'

urlpatterns = [
  path('<int:pk>/', views.detail, name='detail'),
]
```

> url 등록

```python
# accounts/views.py

# from .models import User
from django.contrib.auth import get_user_model

def detail(request, pk):
  User = get_user_model()
  user = User.objects.get(pk=pk)
  # user = get_user_model().objects.get(pk=pk)
   
  context = {
    'user': user
  }
  
  return render(request, 'accounts/detail.html', context)
```