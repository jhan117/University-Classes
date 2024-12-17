# Week 14

보강주 포함

- [Week 14](#week-14)
  - [Backend (MongoDB)](#backend-mongodb)
  - [Axios](#axios)
  - [Spring Security](#spring-security)
  - [Deployment](#deployment)

## Backend (MongoDB)

목표

- Spring Boot 사용
- swagger 사용

1. RESTful API
   - REST: HTTP 프로토콜 기반 (HTTP 메소드 사용: GET, POST, PUT, DELETE)
   - RESTful API: REST를 위한 API (JSON)
2. Project 생성
   - MongoDB와 연결하려면 중요한 정보를 넘겨야 하는데
   - properties 파일을 못 올리게 .gitignore로
     - src/main/resources 하단에 파일을 생성함
     - example 파일로 다른 이들이 사용할 수 있도록
     - application.properties에 `spring.config.import`로 파일을 부르고 `spring.data.mongodb.uri`에 주소 변수를 저장함
     - `spring.config.import=mongodb-connection.properties`
     - `spring.data.mongodb.uri=${MONGODB_URI}`
   - 환경변수로 관리
   - 두 가지 방법으로 github에 못 올리도록
   - Spring Data MongoDB 추가
3. Spring Data MongoDB에서 사용하는 어노테이션
   - `@Document`
     - MongoDB Collection 지정 가능(collation이랑 혼동 유의)
     - `@Document(collection="songs")`
   - `@Id`
     - ObjectId에 해당하는 필드를 지정
     - `@Id val id: String? = null`
     - 널로 지정해주면 mongodb가 알아서 id를 넣어준다

- Repository
  - `interface SongRepository : MongoRepository<Song, String>{}`
    - `<type, id의 type>`
  - 기본적인 메소드는 알아서 구현됨
    - `fun getAllSongs(): List<Song> = repository.findAll()`
    - service에서 이렇게 사용 가능(repo에 추가하지 않아도)
    - `repository.save(song)`
    - `repository.findById(id).orElse(null)`
    - `songTarget.isPresent`: 값이 존재하면
      - `songTarget.get()`: 가져와
      - `oldSong.copy(title = song.title,...)`: 복사하고 업뎃해
    - `repository.existsById(id)`
    - `repository.deleteById(id)`
  - `fun findBySinger(singer: String): List<Song>`
    - 위의 함수처럼 추가해주기만 해도 알아서 구현됨!
  - 물론 복잡한 로직은 본인이 작성해야 함
- CRUD
  - Create (insert, add, insertOne)
  - Read (select, fetch, find)
  - Update (update, updateOne, replaceOne)
  - Delete (delete, deleteOne)
- Controller
  - `@RequestMapping("")`: 주소의 기본값?이랄까 앞에 자동으로 추가해줌
  - `@GetMapping`: RequestMapping의 주소 뒤에 찍힘, 괄호 안붙이면 안붙이는 주소대로
  - `@PostMapping`: 생성하거나 데이터 전송
  - `@PutMapping`: 전체 업데이트
    - put, post에서 바디 값은 `(@RequestBody songDetailes: Song)`
  - `@DeleteMapping`: 삭제
  - `@--Mapping("/{id})`
    - 동적 경로의 id 값을 `(@PathVariable id:String)` 이렇게 가져옴
- Swagger (springdoc-openapi): spring boot의 api 테스트 기능

  - dependencies에 추가: `implementation("org.springdoc:springdoc-openapi-starter-webmvc-ui:2.7.0")`
  - 웹 브라우저: `http://localhost:8080/swagger-ui/index.html`
  - OpenAPI Specification을 JSON 형식으로 확인 가능: `http://localhost:8080/v3/api-docs`

- swagger 대신 postman, talend 사용 가능

## Axios

- backend 실행

1. intelliJ에서 실행하기
2. Power Shell에서 실행하기(권장)  
   `./gradlew bootRun`  
   보통 빌드가 되어있긴 하지만 안되어있다면 `./gradlew build` 후 실행
3. jar 파일로 실행

```powershell
./gradlew bootJar
java -jar .\build\libs\ (여기까지 입력하고 Tab 누르면 jar 파일 한 개만 있어서 자동 완성됨)
```

- Asynchronous, Synchronous
  - Asynchronous : 비동기 처리  
      - 시간이 오래 걸릴 때 사용하며 요청 작업이 끝나면 전달받은 callback 함수 실행함  
      - 좋아보이지만 콜백함수가 중첩되어 많으면 코드가 복잡해지고 문제가 생기므로 동기 처리로 해결하는 게 좋음
  - Synchronous: 동기 처리  
      - 순서가 중요하고 여러 작업을 순차적으로 수행하여 직관적인 흐름이 필요할 때 유용함  
      - 함수에 async를 붙여서 axios 코드에 await를 붙여 기다린 후 다음 줄 실행하게 만듦(동기처럼 보임). 물론 함수 자체는 비동기임  
      - Cuard Clause로 문제 생길시 바로 return 함을 통해 중첩 if문을 줄일 수 있음

`npm i axios`

- 서버와 클라이언트 간 HTTP 요청 처리

```jsx
const getSong = async () => {
  try {
    const res = await axios.get(SERVER_URL);
    console.log(res);

    setSongs(res.data);
  } catch (err) {
    console.log(err);

    setSongs([]);
  }
};
```

- useEffect

  - Side effect 담당하는 react hook 임
    - hook 이란 useState, 뭐 이런거, 컴포넌트에 연결하거나 걸어두는 역할  
      `useEffect(() => {}, []);`
  - dependency를 뜻하는 두번째 인자에 빈배열 넣으면 딱 한번 실행, state or props 넣으면 변경되는 경우에 작업이 실행됨

- CORS

  - Cross-Origin Resource Sharing: 다른 출처의 자원을 공유할 때 제한 거는거
  - origin (원래 출처)를 넘어 다른 출처로 간다
    - Protocol: HTTP/HTTPS
    - Host: Domain 이름
    - Port: 포트번호
  - 작동방식

    - Client의 options request
    - web browser가 요청 허용할지 말지 확인함 Preflight request로 불리는 Options 요청 보내서 실제 요청 허용할 수 있는지 확인
    - origin 서버의 response
    - CORS 헤더를 포함해서 아까의 reqeust에 응답함
    - Client가 서버의 응답의 CORS 헤더를 확인해서 결정함

  - CORS 해결 방법
    - backend에서 설정이 필요함
    - requestmapping 밑에 쓰면 됨!
    - `@CrossOrigin(origins = ["http://localhost:3000"])`
    - origin은 front 주소, 배포시 주소가 변경되면 추가해줘야 함

## Spring Security

- JWT (JSON Web Token)
  - 정보 변조 여부 확인 용도
  - 구성
    - 헤더: 토큰의 타입과 알고리즘 정보
    - 페이로드: 실제 전달하고자 하는 데이터
    - 서명: 변조되지 않았음을 확인하는 부분, 비밀 키 이용해생성
    - <https://jwt.io/>
  - 사용 흐름
    - 로그인 -> 서버가 JWT 생성 -> 이걸 클라이언트에 전달 -> 요청시 JWT 서버로 보내고 서버는 서명 검증 후 요청 처리
  - 장점
    - 서버 상태 유지 불필요
    - 여러 서버 인증 정보 공유 가능
    - 토큰 자체에 정보가 있어 과정이 빠름

## Deployment

- Frontend: Netlify 이용 => 정적 사이트 무료 배포
  - testing-library/react 버전 에러 해결 방법: `npm i web-vitals`
  - 환경변수: $env:REACT_APP_API_URL="" 터미널에 입력

```jsx
const fetchData = async () => {
  try {
    const apiUrl = process.env.REACT_APP_API_URL;

    const response = await fetch(apiUrl);

    if (!response.ok) {
      throw new Error("Network response was not ok");
    }

    const data = await response.json();

    setMessage(data.status);
  } catch (error) {
    console.error("Error fetching data: ", error);
  }
};
```

- Backend: Render 이용
  - CrossOrigin 주소 추가하는 거 까먹지 말자
  - build 에러 없애는 방법
    - 정석: Docker 이용해서 만든 컨테이너에서 Gradle 설치 후 build
    - Intellj에서 빌드 후 build/libs 하단에 있는 .jar 파일을 프로젝트 rott에 app.jar로 복사한다
      - 그 후 Dockerfile을 생성해 내용을 입력한다.

```Dockerfile
FROM openjdk:21-jdk
COPY app.jar /app/app.jar
WORKDIR /app
EXPOSE 8080
ENTRYPOINT ["java","-jar","app.jar"]
```

-> 만약 jdk 버전이 다르다면 구글에 docker jdk 17을 검색해서 복사해온다.

- 배포가 되었다면 배포된 주소 뒤에 주소를 덧붙혀서 netlify의 환경변수란에 추가한다 이때 자동으로 재deploy 되지 않으니 수동으로 deploy 해준다.
- Github에 push 되면 내용이 업데이트 되기 때문에 ghitub에 올리는 것이 중요하다.

- CI/CD
  - CI: Continuous Integration (지속적인 통합)
  - CD: Continuous Delivery (지속적인 배달? 제공) 또는 Continuous Deployment (지속적인 배포)
