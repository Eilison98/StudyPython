
# 리스트로 구하기
dice = [1, 2, 3, 4, 5, 6]  # 주사위 숫자 리스트
dice_sums_list = []
for roll1 in dice:
    for roll2 in dice:
        dice_sums_list.append(roll1 + roll2)
print("주사위 합(리스트):", dice_sums_list)

# 집합으로 구하기
dice = [1, 2, 3, 4, 5, 6]  # 주사위 숫자 리스트
dice_sums_set = set()
for roll1 in dice:
    for roll2 in dice:
        dice_sums_set.add(roll1 + roll2)
print("주사위 합(집합):", dice_sums_set)
