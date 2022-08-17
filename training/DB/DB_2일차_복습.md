-- 쿼리



-- 30세 이상인 사람들

```sql
SELECT * FROM users WHERE age >= 30;
```

```sql
828명
```

-- 30세 이상인 사람들의 이름

```sql
SELECT first_name FROM users WHERE age >= 30;
```

-- 30세 이상인 사람들의 이름 3명만

```sql
SELECT first_name FROM users 
WHERE age >= 30 LIMIT 3;
```

```sql
first_name
----------
정호        
경희        
정자
```

-- 30세 이상이고 성이 김인 사람

```sql
SELECT COUNT(*) FROM users 
WHERE age >= 30 AND last_name = '김'
```

```sql
COUNT(*)
--------
224
```

-- 30세 이상인 사람들의 숫자

```sql
SELECT COUNT(*) FROM users WHERE age >= 30;
```

```sql
COUNT(*)
--------
828
```



-- 전체 중에 가장 작은 나이

```sql
SELECT MIN(age) FROM users;
```

```sql
MIN(age)
--------
15  
```

-- 이씨 중에 가장 작은 나이

```sql
SELECT MIN(age) FROM users WHERE last_name = '이';
```

```sql
MIN(age)
--------
15
```

-- 이씨 중에 가장 작은 나이를 가진 사람의 이름과 계좌잔고

```sql
SELECT MIN(age), first_name, balance FROM users WHERE last_name = '이';
```

```sql
MIN(age)  first_name  balance
--------  ----------  -------
15        은영          78000
```



-- 30세 이상인 사람들의 평균 나이

```sql
SELECT AVG(age) FROM users WHERE age >= 30;
```

```sql
AVG(age)        
----------------
35.1763285024155
```



-- 계좌 잔액이 가장 높은 사람

```sql
SELECT MAX(balance), first_name FROM users;
```

```sql
MAX(balance)  first_name
------------  ----------
1000000       순옥
```





-- 지역번호가 02인 사람

```sql
SELECT first_name FROM users WHERE phone LIKE '02%';
```





-- 준으로 끝나는 사람

```sql
SELECT last_name, first_name FROM users 
WHERE first_name LIKE '%준';
```



-- 중간번호가 5114

```sql
SELECT phone FROM users WHERE phone LIKE '%-5114-%';
```

```sql
phone        
-------------
011-5114-9343
011-5114-9343
```





-- 나이 오름차순 

```sql
SELECT DISTINCT age FROM users ORDER BY age;
```

-- 나이, 성 순으로 오름차순

```sql
SELECT age, last_name FROM users ORDER BY age, last_name;
```



-- 계좌 잔액 순 내림차순 

```sql
SELECT balance FROM users ORDER BY balance DESC;
```



-- 계좌 잔액 내림차순(높은->낮은 것), 성 오름차순(ㄱ->ㅎ)

```sql
SELECT balance, age FROM users 
ORDER BY balance DESC, last_name ASC;
```

