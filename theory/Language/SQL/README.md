# Database

- 체계화된 데이터의 모임
- 공유하고 사용할 목적으로 통합 관리되는 정보 집합
- 논리적으로 연관된 자료의 모음
- 자료 중복을 없애고 구조화해 기억시켜 놓은 자료의 집합체



### SQL

- DB에서 조작하는 언어. (`Query`: 질의), 단순

- RDBMS의 데이터 관리를 위해 설계된 프로그래밍 언어

- DB 스키마 생성 및 수정

  - DDL(정의) : 구조를 정의. CREATE, DROP, ALTER
  - DML(조작) : 데이터를 조작. INSERT, SELECT, UPDATE
  - DCL(제어) : DB 사용자의 권한 제어. GRANT, REVOKE

  

- 필드 제약 조건

  - NOT NULL : NULL값 입력 금지
  - UNIQUE : 중복 값 입력 금지(NULL 값은 중복 입력 가능)
  - PRIMARY KEY : NOT NULL + UNIQUE
  - FOREIGN KEY : 외래키, 다른 테이블의 키
  - CHECK : 조건으로 설정된 값만 입력 허용
  - DEFAULT : 기본 설정 값



### 스키마

- DB에서 자료의 구조, 표현방법, 관계등 전반적인 명세를 기술