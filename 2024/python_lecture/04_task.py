from random import choice


# 색상 코드
END = "\033[0m"
WHITE = "\033[1;37m"
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
# 상수
POSSIBLE_ACTIONS = ["가위", "바위", "보"]
WIN = f"{GREEN}* 축하합니다. 당신이 이겼습니다.{END}"
LOSE = f"{RED}* 컴퓨터가 이겼습니다.{END}"
DRAW = f"{WHITE}* 비겼습니다.{END}"


def outcome(user_action, computer_action, counts):
    """
    출력 및 count 반환
    counts = [win, lose, draw]
    """

    if user_action == computer_action:
        print(DRAW)
        counts[2] += 1
    else:
        match user_action:
            case "가위":
                if computer_action == "보":
                    print(WIN)
                    counts[0] += 1
                else:
                    print(LOSE)
                    counts[1] += 1
            case "바위":
                if computer_action == "가위":
                    print(WIN)
                    counts[0] += 1
                else:
                    print(LOSE)
                    counts[1] += 1
            case "보":
                if computer_action == "바위":
                    print(WIN)
                    counts[0] += 1
                else:
                    print(LOSE)
                    counts[1] += 1
    return counts


while True:
    # 총 승패 횟수 : win, lose, draw
    counts = [0, 0, 0]

    # 횟수 입력
    round_input = input("가위, 바위, 보 게임을 몇 회 실시하겠습니까? (press q to quit) : ")

    # 나가기
    if round_input == "q":
        break

    # 숫자 입력 체크
    if not round_input.isdigit():
        print("숫자를 입력해 주세요...")
        continue

    # 숫자 횟수 조건 체크
    round_input = int(round_input)
    if round_input < 5:
        print("5 이상 숫자를 입력해주세요...")
        continue

    # 횟수 출력
    print("=" * 80)
    print(f">>> 지금부터 가위, 바위, 보 게임을 총 {YELLOW}{round_input}{END} 회 실시합니다")

    # 게임 시작
    for i in range(1, round_input+1):
        print(f"> {YELLOW}{i}{END} 회차 게임을 시작합니다.")

        # 유저 입력
        while True:
            user_action = input("가위, 바위, 보를 선택하세요 : ")

            # 유저 입력 예외
            if user_action not in POSSIBLE_ACTIONS:
                print("다시 입력해주세요...")
                continue

            # 컴퓨터 랜덤 및 각 선택 출력
            computer_action = choice(POSSIBLE_ACTIONS)
            print(f"YOU : {user_action}, COMPUTER : {computer_action}")

            # 승패 결정
            counts = outcome(user_action, computer_action, counts)
            break

    # 게임 종료
    print("=" * 80)
    print(">>> 게임이 종료되었습니다.\n>>> 최종 결과는 다음과 같습니다.")
    print(f"컴퓨터가 이긴 횟수 : {RED}{counts[1]}{END}\n비긴 횟수 : {WHITE}{
          counts[2]}{END}\n당신이 이긴 횟수 : {GREEN}{counts[0]}{END}")

    print("=" * 80)
