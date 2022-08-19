### 1. 모든 테이블의 이름을 출력하세요.

```sql
.table
```

```
albums          employees       invoices        playlists     
artists         genres          media_types     tracks        
customers       invoice_items   playlist_track
```



### 2. 모든 테이블의 데이터를 확인해보세요.

| 공백은 있는지 NULL은 있는지 데이터 타입은 어떤지 등등 데이터를 직접 확인해보세요.



### 3. 앨범(albums) 테이블의 데이터를 출력하세요.

| 단, `Title`을 기준으로 내림차순해서 5개까지 출력하세요.

```sql
SELECT * FROM albums ORDER BY title DESC LIMIT 5;
```

```
AlbumId  Title                         ArtistId
-------  ----------------------------  --------
208      [1997] Black Light Syndrome   136     
240      Zooropa                       150     
267      Worlds                        202     
334      Weill: The Seven Deadly Sins  264     
8        Warner 25 Anos                6       
```



### 4. 고객(customers) 테이블의 행 개수를 출력하세요.

| 단, 컬럼명을 `고객 수`로 출력하세요.

```sql
SELECT COUNT(*) AS '고객 수' FROM customers;
```

```
고객 수
----
59  
```



### 5. 고객(customers) 테이블에서 고객이 사는 나라가 `USA`인 고객의 `FirstName`, `LastName`을 출력하세요.

| 단, 각각의 컬럼명을 `이름`, `성`으로 출력하고, `이름`을 기준으로 내림차순으로 5개까지 출력하세요.

```sql
SELECT FirstName AS '이름', LastName AS '성'
FROM customers
WHERE Country = 'USA' ORDER BY 이름 DESC LIMIT 5;
```

```
이름        성         
--------  ----------
Victor    Stevens   
Tim       Goyer     
Richard   Cunningham
Patrick   Gray      
Michelle  Brooks    
```



### 6. 송장(invoices) 테이블에서 `BillingPostalCode`가 `NULL` 이 아닌 행의 개수를 출력하세요.

| 단, 컬렴명을 `송장수`로 출력하세요.

```sql
SELECT COUNT(*) AS '송장수' FROM invoices 
WHERE BillingPostalCode <> '';
```

```
송장수
---
384
```



### 7. 송장(invoices) 테이블에서 `BillingState`가 `NULL` 인 데이터를 출력하세요.

| 단, `InvoiceDate`를 기준으로 내림차순으로 5개까지 출력하세요.

```sql
SELECT InvoiceId, InvoiceDate, BillingState FROM invoices WHERE BillingSTate isnull ORDER BY InvoiceDate DESC LIMIT 5;
```

```
InvoiceId  InvoiceDate          BillingState
---------  -------------------  ------------
412        2013-12-22 00:00:00              
411        2013-12-14 00:00:00              
410        2013-12-09 00:00:00              
404        2013-11-13 00:00:00              
403        2013-11-08 00:00:00              
```



### 8. 송장(invoices) 테이블에서 `InvoiceDate`의 년도가 `2013`인 행의 개수를 출력하세요.

| `strftime`를 검색해서 활용해보세요.

```sql
SELECT COUNT(*) FROM invoices 
WHERE strftime('%Y', InvoiceDate) = '2013';
```

```
COUNT(*)
--------
80      
```



### 9. 고객(customers) 테이블에서 `FirstName`이 `L` 로 시작하는 고객의 `CustomerId`, `FirstName`, `LastName`을 출력하세요.

| 단, 각각의 컬럼명을 `고객ID`, `이름`,`성`으로 출력하고, `고객ID`을 기준으로 오름차순으로 출력하세요.

```sql
SELECT CustomerId AS '고객ID', FirstName AS '이름', 
LastName AS '성'
FROM customers
WHERE FirstName LIKE 'L%'
ORDER BY 고객ID ASC;
```

```
고객ID  이름        성        
----  --------  ---------
1     Luís      Gonçalves
2     Leonie    Köhler   
45    Ladislav  Kovács   
47    Lucas     Mancini  
57    Luis      Rojas    
```



### 10. 고객(customers) 테이블에서 각 나라의 고객 수와 해당 나라 이름을 출력하세요.

| 단, 각각의 컬렴명을 `고객 수`,`나라`로 출력하고, 고객 수 상위 5개의 나라만 출력하세요.

```sql
SELECT COUNT(country) AS '고객 수', Country AS '나라' FROM customers
GROUP BY country
ORDER BY COUNT(country) DESC LIMIT 5;
```

```
고객 수  나라     
----  -------
13    USA    
8     Canada 
5     France 
5     Brazil 
4     Germany
```



### 11. 앨범(albums) 테이블에서 가장 많은 앨범이 있는 Artist의 `ArtistId`와 `앨범 수`를 출력하세요.

```sql
SELECT ArtistId, COUNT(*) AS '앨범 수' 
FROM albums 
GROUP BY ArtistId 
ORDER BY COUNT(*) DESC LIMIT 1;
```

```
ArtistId  앨범 수
--------  ----
90        21  
```



### 12. 앨범(albums) 테이블에서 보유 앨범 수가 10개 이상인 Artist의 `ArtistId`와 `앨범 수` 출력하세요

| 단, 앨범 수를 기준으로 내림차순으로 출력하세요.

```sql 
SELECT ArtistId, COUNT(*) AS '앨범 수' 
FROM albums 
GROUP BY ArtistId HAVING COUNT(*) >= 10
ORDER BY COUNT(*) DESC;
```

```
ArtistId  앨범 수
--------  ----
90        21  
22        14  
58        11  
50        10  
150       10  
```



### 13. 고객(customers) 테이블에서 `State`가 존재하는 고객들을 `Country` 와 `State`를 기준으로 그룹화해서 각 그룹의 `고객 수`, `Country`, `State` 를 출력하세요.

| 단, `고객 수`, `Country` 순서 기준으로 내림차순으로 5개까지 출력하세요.

```sql 
SELECT COUNT(*) AS '고객 수', Country, State
FROM customers
WHERE State != ''
GROUP BY Country, State
ORDER BY COUNT(*) DESC, Country DESC LIMIT 5;
```

```
고객 수  Country  State
----  -------  -----
3     USA      CA   
3     Brazil   SP   
2     Canada   ON   
1     USA      WI   
1     USA      WA   
```



### 14.  고객(customers) 테이블에서 `Fax` 가 `NULL`인 고객은 'X' NULL이 아닌 고객은 'O'로 `Fax 유/무` 컬럼에 표시하여 출력하세요.

| 단, `CustomerId`와 `Fax 유/무` 컬럼만 출력하고, `CustomerId` 기준으로 오름차순으로 5개까지 출력하세요. 

```sql 
SELECT CustomerId, 
CASE
	WHEN FAX isnull THEN 'X'
	WHEN FAX != '' THEN 'O'
END Fax
FROM customers
ORDER BY CustomerId ASC LIMIT 5;

```

```
CustomerId  Fax
----------  ---
1           O  
2           X  
3           X  
4           X  
5           O  
```



### 15. 점원(employees) 테이블에서 `올해년도 - BirthDate 년도 + 1` 를 계산해서 `나이` 컬럼에 표시하여 출력하세요.

| 단, 점원의 `LastName`, `FirstName`, `나이` 컬럼만 출력하고, `EmployeeId`를 기준으로 오름차순으로 출력하세요.

| cast(), strftime(), 오늘 날짜를 구하는 함수를 검색하고, 활용해보세요.

  CAST('[변환하고자 하는 데이터]' AS [데이터형식])

 strftime('%Y', InvoiceDate) = '2013';

```sql
SELECT 
EmployeeID,
LastName, 
FirstName, 
DATETIME("now") - CAST(BirthDate AS DATETIME) + 1 AS "나이" 
FROM employees ORDER BY EmployeeId;
```

```
EmployeeId  LastName  FirstName  나이
----------  --------  ---------  --
1           Adams     Andrew     61
2           Edwards   Nancy      65
3           Peacock   Jane       50
4           Park      Margaret   76
5           Johnson   Steve      58
6           Mitchell  Michael    50
7           King      Robert     53
8           Callahan  Laura      55
```



### 16. 가수(artists) 테이블에서 앨범(albums)의 개수가 가장 많은 가수의 `Name`을 출력하세요.

| artists 테이블과 albums 테이블의 `ArtistId` 활용하세요.

```sql 
SELECT
ArtistId,
Name
FROM artists
WHERE ArtistId =
(SELECT ArtistId FROM albums  
 GROUP BY ArtistId 
 ORDER BY COUNT(*) DESC LIMIT 1);
```

```
ArtistId  Name       
--------  -----------
90        Iron Maiden
```



### 17. 장르(genres) 테이블에서 음악(tracks)의 개수가 가장 적은 장르의 `Name`을 출력하세요.

| genres 테이블과 tracks 테이블의 `GenreId` 활용하세요.

```sql 
SELECT
GenreId,
Name
FROM Genres
WHERE GenreId =
(SELECT GenreId FROM tracks  
 GROUP BY GenreId 
 ORDER BY COUNT(*) ASC LIMIT 1);
```

```
GenreId  Name 
-------  -----
25       Opera
```



### 예습. 장르 테이블과 트랙 테이블을 조회하여 장르별로 장르명과 트랙의 개수를 출력하시오.

```sql
SELECT
g1.genreId,
g1.Name,
COUNT(g1.Name)
FROM genres g1
INNER JOIN tracks t1 on g1.GenreId = t1.GenreId
GROUP BY g1.Name
ORDER BY COUNT(g1.Name) DESC;
```

```
GenreId  Name                COUNT(g1.Name)
-------  ------------------  --------------
1        Rock                1297          
7        Latin               579           
3        Metal               374           
4        Alternative & Punk  332           
2        Jazz                130           
19       TV Shows            93            
6        Blues               81            
24       Classical           74            
21       Drama               64            
14       R&B/Soul            61            
8        Reggae              58            
9        Pop                 48            
10       Soundtrack          43            
23       Alternative         40            
17       Hip Hop/Rap         35            
15       Electronica/Dance   30            
16       World               28            
13       Heavy Metal         28            
20       Sci Fi & Fantasy    26            
12       Easy Listening      24            
22       Comedy              17            
11       Bossa Nova          15            
18       Science Fiction     13            
5        Rock And Roll       12            
25       Opera               1             
```





genre track

SELECT a.컬럼, a.주소, a.성별, b.컬럼, b.특기

FROM A a 

inner join B b on a.이름 = b.이름

GenreId