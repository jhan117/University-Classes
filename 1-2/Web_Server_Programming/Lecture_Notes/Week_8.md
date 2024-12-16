# Week 8

- [Week 8](#week-8)
  - [Lotto](#lotto)

## Lotto

- `@RestController`: REST API를 처리하며, 반환값을 JSON 형식으로 클라이언트에 전달
- `@Controller`: HTML 뷰를 반환하는 웹 애플리케이션 컨트롤러
- `arrayOf(0, 0, 0)`, `타입: Array<Int>`
  - IntArray 사용하는게 더 효율적
  - `IntArray(6) { 0 }`
  - `numbers[i] = n` => `numbers = numbers.plus(n)`
- `numbers.indices`: 인덱스 범위 반환 ex) 0..2
- `Random.nextInt(45) + 1` = `Random.nextInt(1, 46)`: 46 제외
- `numbers.sort()`
- `numbers.contatins(n)`: 중복되어있다면 다시 뽑게 하기
  - `do {n = }while(numbers.contains(n))`
  - `while(numbers.size < 6) n= if(!numbers.contains(n))`
  - set을 이용하는 것도 좋죠
    - `mutableSetOf<Int>()`
    - `number.add()`바로 추가
    - `numbers.toSortedSet().toIntArray()`: sort는 이렇게
- nullable인 경우 확신을 줘야해 `!!`로 입력
