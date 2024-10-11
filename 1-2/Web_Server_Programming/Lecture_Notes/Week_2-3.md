# Week 2-3

- HTML: data 저장
- CSS: view 저장

## HTML and Table

- 케이스 스타일 종류
  - 카멜 케이스
  - 스네이크 케이스
  - 케밥 케이스
  - 파스칼 케이스
- Heading, Paragraph
  - h1, h2, ... , h6
  - p
- List
  - Unordered List: ul
  - Ordered List: ol
  - List item: li
- Anchor (Hyperlink)
  - `<a href=""/>`
  - 새 창에서 열기: target="\_blank"
- Image
  - Block level(수직): div
  - Inline level(수평): span
  - `<img src=""/>`
- 주석
  - `<!-- -->`
- 참고
  - `<figure>`
  - `<picture>`
- table, thead, tbody, caption
  - Table Header: th
  - Table Row: tr
  - Table Data: td

## CSS

- selector (선택자)
  - div 같은 태그
  - 순서: 마지막 것이 적용됨
  - `ul div {}`: ul 자손 div
    - `ul > div {}`: ul 바로 밑에 있는 div
  - `li > div, h1 {}`: 콤마는 여러 태그 설정
  - `<div class = "" />` 지정: .으로 선택자 불러옴
  - `<div id = "" />` 지정: #으로 선택자 불러옴
  - 가상 선택자: Pseudo-class selector
    - `li:nth-child(odd)`: 숫자, odd(홀수), even(짝수)
    - `div:hover {}`
- Emmet(에밋): 편하게 코드 생성 가능
  - `ul>li*3>div` 후 tab 누르기
- 외부 css 파일 생성
  - `<link rel="stylesheet" href="style.css" />`
- 주석: `/* */`
