-- 성별 1(남자), 2(여자)

```sql
SELECT id,
CASE 
	WHEN gender = 1 THEN '남자' -- integer는 ''생략 가능?
	WHEN gender = 2 THEN '여자'
END AS 성별
FROM healthcare
LIMIT 5;

```

```
id  성별
--  --
1   남자
2   여자
3   여자
4   남자
5   여자
```





-- 흡연(smoking)값 확인

```sql
SELECT DISTINCT smoking FROM healthcare;
```

```
smoking
-------
1      
3      
2      
     
```



-- 흡연여부값 변경

```sql
SELECT id,
CASE
	WHEN smoking = 1 THEN '비흡연자'
	WHEN smoking = 2 THEN '흡연자'
	WHEN smoking = 3 THEN '헤비 스모커'
	ELSE '무응답'
END AS '흡연여부'
FROM healthcare
LIMIT 5;
```

```
id  흡연여부
--  ----
1   비흡연자
2   비흡연자
3   비흡연자
4   비흡연자
5   비흡연자
```



-- 나이에 따라서 구분

--청소년(~18), 청년(~40), 중장년(~90)

```sql
SELECT id,
CASE
	WHEN age <= 18 THEN '청소년'
	WHEN age <= 40 THEN '청년'
	WHEN age <= 90 THEN '중장년'
	ELSE '나이불명'
END AS '연령대'
FROM healthcare
LIMIT 5;
```

```sql
id  연령대
--  ---
1   청소년
2   청소년
3   청소년
4   청소년
5   청소년
```



-- 가장 작은 나이와 수

```sql
SELECT age, COUNT(*)
FROM users
GROUP BY age
ORDER BY age
LIMIT 1;
```

 ```
 age  COUNT(*)
 ---  --------
 15   39      
 ```



-- 가장 작은나이 확인하기

```sql
SELECT MIN(age) FROM users;
```

```
MIN(age)
--------
15      
```

-- 가장 작은나이 사람 수 확인하기

```sql
SELECT COUNT(*) FROM users WHERE age = 15;
```

```
COUNT(*)
--------
39      
```



-- 평균 계좌 잔고

```sql
SELECT AVG(balance) FROM users;
```

-- 평균 계좌 잔고보다 높은 사람의 수

```sql
SELECT COUNT(*) FROM users
WHERE balance > (SELECT AVG(balance) FROM users);
```

```
COUNT(*)
--------
222     
```



-- 유은정의 지역은?

```sql
SELECT last_name || first_name AS 이름, country FROM users
WHERE 이름 = '유은정';
```

```
이름   country
---  ------- 
유은정  강원도   
```



-- 유은정과 같은 지역에 사는 사람의 수?

```sql
SELECT country, COUNT(*) FROM users
WHERE country = (SELECT country FROM users WHERE last_name = '유' AND first_name = '은정');
```

```
country  COUNT(*)
-------  --------
강원도      101    
```



-- 이은정의 지역은?

```sql
SELECT last_name || first_name AS 이름, country FROM users
WHERE 이름 = '이은정';
```

```
이름   country
---  -------
이은정  전라북도   
이은정  경상북도
```



-- 이은정과 같은 지역에 사는 사람의 수?

```sql
SELECT country, COUNT(*) FROM users
WHERE country IN 
(SELECT country FROM users WHERE last_name = '이' AND first_name = '은정') 
GROUP BY country;
```

```
country  COUNT(*)
-------  --------
경상북도     103     
전라북도     115 
```





-- 성씨별 가장 작은 나이

```sql
SELECT last_name AS '성', MIN(age) AS '가장 작은 나이'
FROM users GROUP BY last_name LIMIT 5;
```

```
성  가장 작은 나이
-  --------
강  15      
고  15      
곽  15      
구  17      
권  16      
```



-- 특정 성씨별로 가장 적은 나이 사람 모두를 출력

```sql
SELECT last_name || first_name AS '이름', age FROM users
WHERE (last_name, age) IN 
(SELECT last_name, MIN(age) FROM users GROUP BY last_name) ORDER BY 이름 LIMIT 5;
```

```
이름   age
---  ---
강정수  15 
고시우  15
고우진  15 
곽현숙  15 
구성현  17 
```

