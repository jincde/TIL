# 데이터베이스 07 - ORM

<aside>
💡 코드를 작성한 실습 파일을 압축해서 실라버스에 제출해주세요.

</aside>

### 1. `db/models.py` 파일에 아래의 모델 2개 `Director` `Genre` 를 작성하세요.

> 기본 코드
> 

```python
class Director(models.Model):
    name = models.TextField()
    debut = models.DateTimeField()
    country = models.TextField()

class Genre(models.Model):
    title = models.TextField()
```

### 2. 모델을 마이그레이트(migrate) 하세요.

```bash
# 가상환경 실행 확인 후 아래 명령어를 터미널에 입력합니다.
python manage.py makemigrations

python manage.py migrate
```

### 3. Queryset 메소드 `create` 를 활용해서  `Director` 테이블에 아래 데이터를 추가하는 코드를 작성하세요.

| name | debut | country |
| --- | --- | --- |
| 봉준호 | 1993-01-01 | KOR |
| 김한민 | 1999-01-01 | KOR |
| 최동훈 | 2004-01-01 | KOR |
| 이정재 | 2022-01-01 | KOR |
| 이경규 | 1992-01-01 | KOR |
| 한재림 | 2005-01-01 | KOR |
| Joseph Kosinski | 1999-01-01 | KOR |
| 김철수 | 2022-01-01 | KOR |

> 코드 작성
> 

```python
import datetime
directors = [
  ['봉준호',datetime.date(1993, 1, 1),'KOR'], 
  ['김한민',datetime.date(1999, 1, 1),'KOR'], 
  ['최동훈',datetime.date(2004, 1, 1),'KOR'], 
  ['이정재',datetime.date(2022, 1, 1),'KOR'],
  ['이경규',datetime.date(1992, 1, 1),'KOR'], 
  ['한재림',datetime.date(2005, 1, 1),'KOR'],
  ['Joseph Kosinski',datetime.date(1999, 1, 1),'KOR'], 
  ['김철수',datetime.date(2022, 1, 1),'KOR']
]

for i in range(len(directors)):
  director = Director()
  director.name = directors[i][0]
  director.debut = directors[i][1]
  director.country = directors[i][2]
  director.save()
```

### 4. `인스턴스 조작` 을 활용하여`Genre` 테이블에 아래 데이터를 추가하는 코드를 작성하세요.

| title |
| --- |
| 액션 |
| 드라마 |
| 사극 |
| 범죄 |
| 스릴러 |
| SF |
| 무협 |
| 첩보 |
| 재난 |

> 코드 작성
> 

```python
genres = ['액션', '드라마', '사극', '범죄', '스릴러', 'SF', '무협', '첩보', '재난']

for i in range(len(genres)):
  genre = Genre()
  genre.name = genres[i]
  genre.save()
```

### 5. Queryset 메소드 `all` 을 활용해서 `Director` 테이블의 모든 데이터를 출력하는 코드를 작성하세요.

> 출력 예시
> 

```
봉준호 1993-01-01 00:00:00 KOR
김한민 1999-01-01 00:00:00 KOR
최동훈 2004-01-01 00:00:00 KOR
이정재 2022-01-01 00:00:00 KOR
이경규 1992-01-01 00:00:00 KOR
한재림 2005-01-01 00:00:00 KOR
Joseph Kosinski 1999-01-01 00:00:00 KOR
김철수 2022-01-01 00:00:00 KOR
```

> 코드 작성
> 

```python
for i in range(len(Director.objects.all())):
  result = []
  result.append(Director.objects.all()[i].name)
  result.append(Director.objects.all()[i].debut)
  result.append(Director.objects.all()[i].country)
  print(*result)
```

### 6. Queryset 메소드 `get` 을 활용해서 `Director` 테이블에서 `id` 가 1인 데이터를 출력하는 코드를 작성하세요.

> 출력 예시
> 

```
봉준호 1993-01-01 00:00:00 KOR
```

> 코드 작성
> 

```python
director1 = Director.objects.get(id=1)
print(director1.name, director1.debut, director1.country)
```

### 7. Queryset 메소드 `get` 을 활용해서 `Director` 테이블에서 `country` 가 USA인 데이터를 출력하는 코드를 작성하세요.

> 코드 작성
> 

```python
director1 = Director.objects.get(country='USA')
print(director1.name, director1.debut, director1.country)
```

### 8. 위 문제에서 오류가 발생합니다. 출력된 오류 메세지와 본인이 생각하는 혹은 찾은 오류가 발생한 이유를 작성하세요.

> 오류 메세지
> 

```bash
DoesNotExist: Director matching query does not exist.
```

> 이유 작성
> 

```
get()은 오직 한 개의 데이터만 가져올 수 있다. (0개인 경우의 오류)
```

### 9. Queryset 메소드 `get` 과 `save` 를 활용해서 `Director` 테이블에서  `name` 이 Joseph Kosinski인 데이터를 조회해서 `country` 를 USA 로 수정하고, 출력하는 코드를 작성하세요.

> 출력 예시
> 

```
Joseph Kosinski 1999-01-01 00:00:00 USA
```

> 코드 작성
> 

```python
# 조셉 코신스키 정보 변경
joseph = Director.objects.get(name = 'Joseph Kosinski')
joseph.country = 'USA'
joseph.save()

# 변경 정보 출력
print(joseph.name, joseph.debut, joseph.country)
```

### 10. Queryset 메소드 `get` 을 활용해서 `Director` 테이블에서 `country` 가 KOR인 데이터를 출력하는 코드를 작성하세요.

> 코드 작성
> 

```python
director_kor = Director.objects.get(country = 'JP')
print(director_kor.name, director_kor.debut, director_kor.country)
```

### 11. 위 문제에서 오류가 발생합니다. 출력된 오류 메세지와 본인이 생각하는 혹은 찾은 오류가 발생한 이유를 작성하세요.

> 오류 메세지
> 

```bash
MultipleObjectsReturned: get() returned more than one Director -- it returned 8!
```

> 이유 작성
> 

```
get()은 오직 한 개의 데이터만 가져올 수 있다. (2개 이상인 경우의 오류)
```

### 12. Queryset 메소드 `filter` 를 활용해서 `Director` 테이블에서 `country` 가 KOR인 데이터를 출력하는 코드를 작성하세요.

> 출력 예시
> 

```
봉준호 1993-01-01 00:00:00 KOR
김한민 1999-01-01 00:00:00 KOR
최동훈 2004-01-01 00:00:00 KOR
이정재 2022-01-01 00:00:00 KOR
이경규 1992-01-01 00:00:00 KOR
한재림 2005-01-01 00:00:00 KOR
김철수 2022-01-01 00:00:00 KOR
```

> 코드 작성
> 

```python
director_kor = Director.objects.filter(country = 'KOR')

for i in range(len(director_kor)):
  print(director_kor[i].name, director_kor[i].debut, director_kor[i].country)
```

### 13. 본인이 생각하는 혹은 찾은 `get` 과 `filter` 의 차이를 작성하세요.

```
get()은 쿼리에 맞는 객체 하나만 반환,
filter()는 쿼리에 맞는 객체 여러개들을 반환
```

### 14. Queryset 메소드 `get` 과 `delete`를 활용해서  `Director` 테이블에서 `name` 이 김철수인 데이터를 삭제하는 코드를 작성하세요.

> 코드 작성
> 

```python
# 테이블에 김철수 두 명을 추가했기 때문에 filter로...
director_kim = Director.objects.filter(name = '김철수')

director_kim.delete()
```