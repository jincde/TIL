# git/github 기본 브랜치 설정

- 과거부터 활용된 기술 용어 `master` `slave`
- github는 2020년부터 master에서 `main`으로 변경
- 과거 자료 및 구글링시 `master`로 표현된 경우가 많아 `master`로 변경
- `black-lives-matter`



## 설정

### git

```bash
$ git config --global init.defaultBranch master
```



### github

- **`프로필 설정`** > `Repositories` > `Repository default branch` > `master`로 수정





## 확인

```bash
$ git config --global --list
```
