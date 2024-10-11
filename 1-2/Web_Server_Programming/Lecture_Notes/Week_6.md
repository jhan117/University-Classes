# Week 6

- [Week 6](#week-6)
  - [강의 날짜](#강의-날짜)
  - [Thymeleaf](#thymeleaf)

## 강의 날짜

- **1차시**: 2024-10-07
- **2차시**: 2024-10-10

## Thymeleaf

- html에 모델 전달
  - `[[${song}]]`
- namespace
  - `xmlns:th="http://www.thymeleaf.org"`
- Thymleaf
  - `<span th:text="${song}" />`
  - `<div th:object="${song}" />`: 상위에 object
    - `<p th:text="*{title}"/>`: 하위는 \*로
  - `<span th:if="${song} != null />"`: if 사용
