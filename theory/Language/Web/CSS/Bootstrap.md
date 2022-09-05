## Bootstrap

빠른 디자인, 다양한 커스터마이징을 통해 반응형 웹을 만들자

- 반응형 `grid`시스템
- 미리 만들어진 컴포넌트들을 활용

`Reboot.css` : 부트스트랩에서 제공하는 CSS 파일 [reboot.css](https://getbootstrap.com/docs/4.0/content/reboot/)



### CDN

Content Delivery(Distribution) Network

컨텐츠를 효율적으로 전달하기 위해 여러 노드에 가진 네트워크에 데이터를 제공하는 시스템

- 개별 유저의 가까운 서버를 통해 빠르게 전달 가능
- 외부 서버를 활용함으로써 본인 서버 부하가 적어짐



### spacing

margin and padding

{property}{sides}-{size}

```html
mt-3

<div class="mt-3 mt-5">
  bootstrap-spacing
</div>
```

<br>

- property

  | attribute | value   |
  | --------- | ------- |
  | `m`       | margin  |
  | `p`       | padding |

  <br>

- sides

  | attribute | value                                 |
  | --------- | ------------------------------------- |
  | `t`       | top                                   |
  | `b`       | bottom                                |
  | `s`       | (start) `left` in LTR, `right` in RTL |
  | `e`       | (end) `right` in LTR, `left` in RTL   |
  | `x`       | `left&right`                          |
  | `y`       | `top&bottom`                          |
  | `blank`   | `all` 4 sides                         |

<br>

- sizes

  | attribute | value         |
  | --------- | ------------- |
  | 0         | 0rem          |
  | 1         | 0.25rem `4px` |
  | 2         | 0.5rem `8px`  |
  | 3         | 1rem `16px`   |
  | 4         | 1.5rem `24px` |
  | 5         | 3rem `48px`   |
  | auto      | auto          |

<br>

#### Text

| attribute     | value                |
| ------------- | -------------------- |
| text-start    | left                 |
| text-center   | center               |
| text-end      | right                |
| text-sm-start | sm, md, lg, xl(size) |
| fw-bold       | bold weight          |
| fw-normal     | normal               |
| fw-light      | light weight         |
| fst-italic    | Italic               |