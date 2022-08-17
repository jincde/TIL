# 2일차 실습

## 사전 확인

### 실행

```bash
$ sqlite3 healthcare.sqlite3 
```

### Column 출력 설정

```sql
sqlite3> .headers on 
sqlite3> .mode column
```

### table 및 스키마 조회

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

## 문제

### 1. 추가되어 있는 모든 데이터의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare
```

```
COUNT(*)
--------
1000000 
```

### 2. 연령 코드(age)의 최대, 최소 값을 모두 출력하시오. 

```sql
SELECT MAX(age), MIN(age) FROM healthcare;
```

```
MAX(age)  MIN(age)
--------  --------
18        9
```

### 3. 신장(height)과 체중(weight)의 최대, 최소 값을 모두 출력하시오.

```sql
SELECT 
MAX(height), MAX(weight), 
MIN(height), MIN(weight) FROM healthcare;
```

```
MAX(height)  MAX(weight)  MIN(height)  MIN(weight)
-----------  -----------  -----------  -----------
195          135          130          30         
```

### 4. 신장(height)이 160이상 170이하인 사람은 몇 명인지 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare 
WHERE height BETWEEN 160 AND 170;
```

```
COUNT(*)
--------
516930
```

### 5. 음주(is_drinking)를 하는 사람(1)의 허리 둘레(waist)를 높은 순으로 5명 출력하시오. 

```sql
SELECT * FROM healthcare 
WHERE is_drinking = 1 AND waist != '' 
ORDER BY waist DESC LIMIT 5;
```

```
-- SELECT waist
waist
-----
146.0
142.0
141.4
140.0
140.0
```

### 6. 시력 양쪽(va_left, va_right)이 1.5이상이면서 음주(is_drinking)를 하는 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare 
WHERE va_left >= 1.5 AND va_right >= 1.5 AND is_drinking = 1;
```

```
COUNT(*)
--------
36697   
```

### 7. 혈압(blood_pressure)이 정상 범위(120미만)인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare 
WHERE blood_pressure < 120;
```

```
COUNT(*)
--------
360808
```

### 8. 혈압(blood_pressure)이 140이상인 사람들의 평균 허리둘레(waist)를 출력하시오.

```sql
SELECT AVG(waist) FROM healthcare 
WHERE blood_pressure >= 140;
```

```
AVG(waist)      
----------------
85.8665098512525
```

### 9. 성별(gender)이 1인 사람의 평균 키(height)와 평균 몸무게(weight)를 출력하시오.

```sql
SELECT AVG(height), AVG(weight) FROM healthcare WHERE gender = 1;     
```

```
AVG(height)       AVG(weight)     
----------------  ----------------
167.452735422145  69.7131620222875
```

### 10. 키가 가장 큰 사람 중에 두번째로 무거운 사람의 id와 키(height), 몸무게(weight)를 출력하시오.

```sql
SELECT id, height, weight FROM healthcare 
ORDER BY height DESC LIMIT 1 OFFSET 1;
```

```
id     height  weight
-----  ------  ------
46642  195     100   
```

### 11. BMI가 30이상인 사람의 수를 출력하시오. 

> BMI는 체중/(키*키)의 계산 결과이다. 
> 키는 미터 단위로 계산한다.

```sql
SELECT COUNT(*) FROM healthcare 
WHERE weight / (height * height) >= 30;
```

```
```

### 12. 흡연(smoking)이 3인 사람의 BMI지수가 제일 높은 사람 순서대로 5명의 id와 BMI를 출력하시오.

> BMI는 체중/(키*키)의 계산 결과이다. 
> 키는 미터 단위로 계산한다.

```sql
SELECT id, weight*10000 / (height*height) AS BMI FROM healthcare WHERE smoking = 3
ORDER BY weight*10000 / (height*height) DESC LIMIT 5;
```

```
id      BMI
------  ---
935250  57 
491048  54 
469704  52 
480533  52 
777586  52 
```

### 13. 건강이 가장 안좋은 사람의 정보를 출력

`* 저혈압은 제외

```sql
SELECT *, weight*10000 / (height*height) AS BMI 
FROM healthcare 
WHERE is_drinking = 1 
ORDER BY weight*10000 / (height*height) DESC, 
waist DESC, 
va_left ASC, 
va_right ASC, 
blood_pressure DESC, 
smoking DESC 
LIMIT 1;
```

```
```

### 14. 자유롭게 쿼리를 작성해주시고, 결과와 함께 공유해주세요.

```sql
```

```
```

### 15. 자유롭게 쿼리를 작성해주시고, 결과와 함께 공유해주세요.

```sql
```

```
```