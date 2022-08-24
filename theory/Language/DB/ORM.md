# ORM

- Object-Realtional-Mapping
- 객체 지향 프로그래밍 언어를 사용해 호환되지 않는 유형의 **시스템 간의 데이터를 변환**하는 프로그래밍 기술
- 파이썬에는 SQLAlchemy, peewee 등 라이브러리가 있다
- Django 프레임워크에서는 내장 Django ORM 활용

> 객체로 DB를 조작한다

```sql
Genre.objects.all()
# 클래스 이름. manager. 쿼리셋 API
```



### 모델 설계

- 클래스를 생성해 DB 구조를 만든다

  ```python
  class Genre(models.Model):
    # 기본키는 자동 생성됨
    name = models.CharField(max_length = 30)
  ```

  

### 모델 반영

- 클래스 내용으로 DB에 반영하기 위한 `마이그레이션` 파일을 생성

  ```bash
  $ python manage.py makemigrations
  $ python manage.py migrate
  ```

  

### 마이그레이션

- Model에 생긴 변화를 DB에 반영하기 위한 방법

- 마이그레이션 파일을 만들어 DB 스키마를 반영

  ```
  makemigrations : 마이그레이션 파일 생성
  migrate : 마이그레이션을 DB에 반영
  ```

  

### 기본 조작

- Create

  ```bash
  $ Genre.objects.create(name='Pop')
  
  $ genre = Genre()
  $ genre.name = '인디밴드'
  $ genre.save()
  ```

  

- Read

  ```bash
  $ Genre.objects.all() # 전체 데이터 조회
  $ Genre.objects.get(id=1) # 일부 데이터 조회
  $ Genre.objects.filter(id=1) # 일부 데이터 조회
  ```



- Update

  ```bash
  $ genre = Genre.objects.get(id=1)
  $ genre.name = '락'
  $ genre.save()
  ```

  

- Delete

  ```bash
  $ genre = Genre.objects.get(id=1)
  $ genre.delete()
  ```

  

### get과 filter의 차이

- `get`은 쿼리에 해당하는 객체 하나만을 반환
- `filter`는 쿼리에 해당하는 객체 여러개(쿼리셋)들을 반환

#### 발생되는 오류

```
DoesNotExist: Director matching query does not exist.
```

> get()은 오직 하나의 데이터만 가져올 수 있다. (데이터가 0개인 경우 오류)



```python
MultipleObjectsReturned: get() returned more than one Director -- it returned 8!
```

> get()은 오직 하나의 데이터만 가져올 수 있다. (데이터가 2개 이상인 경우 오류)

- `filter`는 새 쿼리셋을 생성 후, 필터 조건에 맞는 객체들을 삽입 후 리턴
- 따라서, `filter`는 데이터가 0개인 경우에도 에러가 아닌, 빈 쿼리셋을 리턴