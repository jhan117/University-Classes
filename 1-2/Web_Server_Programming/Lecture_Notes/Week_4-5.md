# Week 4-5

## Controller

- Annotation이 중요함
- 적절한 Annotation을 사용하면 알아서 관리해 줌
  - @RestController 사용
- Spring Bean이라고 부름
  - SongController
- Spring Container라는 놈이 자동으로 관리
- 처리 순서
  1. 사용자가 요청 (/song/list)
  2. Spring의 Dispatcher Servlet이 사용자의 요청을 받았는데 누가 필요한지 알아야 함
     - Handler Mapping에게 /song/list는 누가 처리하는지 알아봐 달라고 요청함
  3. Handler Mapping이 /song/list는 SongController가 처리한다고 응답
  4. Dispatcher Servlet이 Handler Adapter에게 SongController 처리해 달라고 요청
  5. Handler Adapter는 우리가 만든 SongController에게 요청
  6. SongController는 Song에 대한 business logic 처리를 담당하고 있는 SongService에게 요청
  7. SongService는 Song을 저장하고 있는 SongRepository에게 요청
  8. 계속 응답을 전달하여 최종적으로 사용자에게 응답

```kotlin
@GetMapping("/song/random")
    fun getRandomSong(): String {
        return """
            <html>
            <body>
                <h1>추천 노래</h2>
                <p>사랑에 연습이 있었다면</p>
            </body>
            </html>
        """.trimIndent()
    }
```

- HTML 반환 가능 그러나 자주 쓰이지 않음
