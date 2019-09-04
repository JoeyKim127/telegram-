import random

def getLotto():
    winner = [1, 15, 19, 23, 28, 42]

    lotto = sorted(random.sample(range(1, 46), 6))

    cnt = len(set(winner) & set(lotto))

    # 6, 1등
    # 5, 3등
    # 4, 4등
    # 3, 5등

    rank = ''
    if cnt == 6:
        rank = '1등'
    elif cnt == 5:
        rank = '3등'
    elif cnt == 4:
        rank = '4등'
    elif cnt == 3:
        rank = '5등'
    else:
        rank = '꽝'

    print(f'{cnt}, {rank}')


# winner = [1,5,19,23,28,42]

# lotto = sorted(random.sample(range(1,46),6))

# print(set(winner) & set(lotto))

# print(len(set(winner) & set(lotto)))

# cnt = len(set(winner) & set(lotto)

# if cnt == 6:
#     print(len(set(winner) + ", " + "1등입니다"))

# elif cnt ==5:
#     print(len(set(winner) + ", " + "3등입니다"))

# elif  cnt == 4:
#     print(len(set(winner) + ", " + "4등입니다"))

# elif  cnt == 3:
#     print(len(set(winner) + ", " + "5등입니다"))

# else
#     print(len(set(winner) + ", " + "꽝입니다"))