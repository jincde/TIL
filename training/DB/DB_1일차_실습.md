# 사전 설정

## 실행

```bash
$ sqlite3 healthcare.sqlite3 
```

## Column 출력 설정

```sql
sqlite3> .headers on 
sqlite3> .mode column
```

## table 및 스키마 조회

```sql
sqlite3> .tables
healthcare

sqlite3> .schema healthcare
CREATE TABLE healthcare (
id PRIMARY KEY,        
sido INTEGER NOT NULL, 
gender INTEGER NOT NULL,
age INTEGER NOT NULL,  
height INTEGER NOT NULL,
weight INTEGER NOT NULL,
waist REAL NOT NULL,   
va_left REAL NOT NULL, 
va_right REAL NOT NULL,

blood_pressure INTEGER 
NOT NULL,
smoking INTEGER NOT NULL,
is_drinking BOOLEAN NOT NULL
);
```

# 문제

### 1. 추가되어 있는 모든 데이터의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare;
```

```
COUNT(*)
--------
1000000
```

### 2. 나이 그룹이 10(age)미만인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE age < 10;
```

```
COUNT(*)
--------
156277
```

### 3. 성별이 1인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE gender = 1;
```

```
COUNT(*)
--------
510689
```

#### 3-1. 성별 값 확인

```sql
SELECT DISTINCT gender FROM healthcare;
```

```sql
gender
------
1     
2   
```



### 4. 흡연 수치(smoking)가 3이면서 음주(is_drinking)가 1인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare 
WHERE smoking = 3 AND is_drinking = 1;
```

```
COUNT(*)
--------
150361
```

### 5. 양쪽 시력이(va_left, va_right) 모두 2.0이상인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare
WHERE va_left >= 2.0 and va_right >= 2.0
```

```
COUNT(*)
--------
2614
```

### 6. 시도(sido)를 모두 중복 없이 출력하시오.

```sql
SELECT DISTINCT sido FROM healthcare;
```

```
sido
----
36  
27  
11  
31  
41  
44  
48  
30  
42  
43  
46  
28  
26  
47  
45  
29  
49
```



### 자유롭게 조합해서 원하는 데이터를 출력해보세요.

> 예) 허리 둘레가 x이상이면서 몸무게가 y이하인 사람hem.

#### ex1. 성별이 1인 10대인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare
WHERE gender = 1 AND age >= 10 AND age <= 20;
```

```sql
COUNT(*)
--------
422254
```



#### ex2. 성별이 2면서 키 180이상인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare
WHERE gender = 2 AND height >= 180;
```

```sql
COUNT(*)
--------
31
```

##### ex2-1. ex2 중 가장 큰 사람의 키를 출력하시오.

```sql
SELECT height
FROM healthcare
WHERE gender = 2 AND height >= 180 
ORDER BY height DESC LIMIT 1;
```

```sql
height
------
185
```



#### ex3. 허리 둘레가 80이상이면서 몸무게가 50이하인 사람

```sql
SELECT COUNT(*) FROM healthcare 
WHERE waist >= 80 AND weight <= 50;
```

```sql
COUNT(*)
--------
26774
```



#### ex4. 키가 180이상인 사람의 수

```sql
SELECT COUNT(*) FROM healthcare 
WHERE height >= 180;
```

```sql
COUNT(*)
--------
28829
```



#### ex5. 키가 160이하인 사람의 수

```sql
SELECT COUNT(*) FROM healthcare 
WHERE height <= 160;
```

```sql
COUNT(*)
--------
559703
```



#### ex6. 흡연수치가 3이고, 음주가 0이면서, 혈압이 130 이상인 사람

```sql
SELECT COUNT(*) FROM healthcare 
WHERE smoking = 3 AND is_drinking = 0 
AND blood_pressure >= 130;
```

```sql
COUNT(*)
--------
11416 
```



#### ex7. 흡연수치가 3이고, 음주가 1이면서, 혈압이 130 이상인 사람

```sql
SELECT COUNT(*) FROM healthcare 
WHERE smoking = 3 AND is_drinking = 1 
AND blood_pressure >= 130;
```

```sql
COUNT(*)
--------
59424 
```



#### ex8. 흡연수치가 1이고, 음주가 0이면서, 혈압이 130 이상인 사람

```sql
SELECT COUNT(*) FROM healthcare 
WHERE smoking = 1 AND is_drinking = 0 
AND blood_pressure >= 130;
```

```sql
COUNT(*)
--------
136895 
```



#### ex9. 흡연수치가 1이고, 음주가 1이면서, 혈압이 130 이상인 사람

```sql
SELECT COUNT(*) FROM healthcare 
WHERE smoking = 1 AND is_drinking = 1 
AND blood_pressure >= 130;
```

```sql
COUNT(*)
--------
96364  
```

