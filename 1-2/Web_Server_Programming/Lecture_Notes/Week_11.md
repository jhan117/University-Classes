# Week 11

- [Week 11](#week-11)
  - [Node.js](#nodejs)

## Node.js

- JavaScript
  - 웹브라우저에서 실행
  - Java와 다름
  - SPA (Single Page Application): 단일 페이지에서 전체 페이지를 새로고침 하지 않고 내용을 동적으로 업데이트함
- Node.js

  - 웹브라우저 외의 플랫폼에서 실행 가능 (서버 측 실행 가능)
  - 패키지 관리 도구: NPM (node package manager)
    - npm: 패키지를 생성하고 관리하기 위한 명령어
    - package.json: 어떤 패키지들에 의해 종속적인지 리스트로 가지고 있음 (의존성 관리)
    - 종속성 Dependency: 실제로 실행될 때 필요한 패키지들
    - package-lock.json: 정확한 버전 저장, 프로젝트 의존성 트리(node_modules) 정확하게 기록하기 위해 자동으로 생성
    - node -v(= --version), npm -v(= --version): 버전 확인

- JavaScript
  `console.log("안녕")`

  - 세미콜론 안 써도 됨
  - terminal의 cmd 에서 node 파일명(또는 .js) 입력 하면 실행됨
  - 서버 실행도 가능 -> 서버 중지 ctrl + c
    - http 모듈을 들고 와서 .createServer로 서버를 생성 후 반환된 서버에 .listen으로 서버를 실행함
    - createServer에서 request와 response를 파라미터로 받아서 response에 .wirteHead, .end를 입력해줌
    - wirteHead(status code, headers): 헤더 넘기기
    - end(body): 데이터 넘기기
      - JSON.stringify(data): javascript data값(object = 객체)을 JSON(JavaScript Object Notation) string으로 바꿔줌
    - server.listen(port, listeningListener): 비동기 실행이고 연결을 위해 서버 listening 이벤트를 발생하게 되고 후행 파라미터 콜백 함수가 listening 이벤트를 위해 리스너로 추가됨

- React.js
  - component 사용
  - .jsx: JSX 문법을 사용하는 JavaScript 코드 (Html + JavaScript)
  - 명령어
    - npx create-react-app 폴더명: 생성
    - npm start: 실행
    - powershell에서 오류 해결하는 법
    - 관리자 권한으로 실행
    - `executionpolicy`
    - `set-executionpolicy remotesigned`
  - `index.html`
    - `html:5`: 이걸로 쉽게 만들 수 있음
    - `<div id=root />`: 여기가 index.js 에서 가져오는 지점
