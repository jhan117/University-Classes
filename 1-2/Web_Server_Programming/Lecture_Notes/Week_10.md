# Week 10

- [Week 10](#week-10)
  - [Card Dealer](#card-dealer)

## Card Dealer

- 이미지 저장: `src/main/resources/static/images`
  - 요청: `localhost:8080/images/2_of....png`
- thymeleaf에서 url 표현하는 방법: @{}
  - `<img th:src="@{'/images/' + ${cards}}" />`
  - 파라미터 사용을 권장 `<img th:src="@{/images/{imageName}(imageName=${cards})}" />`
    - 여러개 사용가능 `<img th:src="@{/images/{cardRank}_of_{cardSuit}.png(cardRank=${rank}, cardSuit=${suit})}"` 이때 model.addAttribute를 두 줄 작성하면 됨
- `MutableList<Card>`: `cards.size`, `cards.add()`, `cards.clear`

```kt
override val size: Int
	get() = cards.size
```

- `uniqueCards.toList().sortedWith(compareBy({ suits.indexOf(it.suit) }, { ranks.indexOf(it.rank) }))`
  - `sortedCards.forEach { repository.add(it) }`
- `model.addAttribute("cards", cards.map { it.imageName })`
- `return if () {} else {}`
