# =================================================================== #
# =================================================================== #

def countdown(number, message):
    # 숫자를 역순으로 반복하며 출력
    for i in range(number, 0, -1):
        print(" " * (i - 1) + str(i))  # 현재 숫자를 출력하기 전에 공백을 삽입하여 정렬
    print(message)  # 마지막으로 전달된 메시지 출력

# 함수 호출
countdown(5, "Go!!!")

# =================================================================== #
# =================================================================== #

a_list = ['a', 'b', 'c', 'd', 'e']

# 1. append 메소드를 사용하여 숫자 '10' 추가
a_list.append(10)

# 2. del 명령어를 사용하여 'a' 삭제
del a_list[0]

# 3. remove 메소드를 사용하여 'c' 삭제
a_list.remove('c')

# 4. pop 메소드를 사용하여 'e' 삭제
a_list.pop()

# 결과 출력
print(a_list)

# =================================================================== #
# =================================================================== #

a_list = ['banana', 'orange', 'apple', 'kiwi', 10, 20]

# 1. 리스트에 'apple'이라는 문자열이 있으면 'apple'을 삭제
if 'apple' in a_list:
    a_list.remove('apple')

# 2. 리스트에 숫자 '30'이 없으면 '30' 추가
if 30 not in a_list:
    a_list.append(30)

# 결과 출력
print(a_list)

# =================================================================== #
# =================================================================== #

fruits = ['banana', 'orange', 'apple', 'kiwi', 'lemon']

# 1. for 문을 사용하여 'apple'의 인덱스를 출력
for index, fruit in enumerate(fruits):
    if fruit == 'apple':
        print("Index of 'apple':", index)

# 2. for 문을 사용하여 문자의 개수가 5이상인 문자열의 리스트 작성
result_list = []
for fruit in fruits:
    if len(fruit) >= 5:
        result_list.append(fruit)

# 결과 출력
print("Strings with 5 or more characters:", result_list)

# =================================================================== #
# =================================================================== #

text = "maritime"

# 1. 문자열을 오름차순으로 출력
sorted_text = sorted(text)
for char in sorted_text:
    print(char)

# 2. 개수가 2개 이상인 문자의 리스트 작성
result_list = []
for char in set(text):
    if text.count(char) >= 2:
        result_list.append(char)

# 결과 출력
print("Characters with 2 or more occurrences:", result_list)

# =================================================================== #
# =================================================================== #

list1 = ['a', 'b', 'c', 'b', 'd']
list2 = [10, 20, 30, 40, 50]

# 1. list1에 list1의 항목을 2번 복사하여 추가
list1 += list1 * 2

# 2. list1에 list2의 항목을 추가
list1 += list2

# 3. 정수에 10을 곱한 다음 리스트로 변환
for i in range(len(list1)):
    # x가 정수라면
    if isinstance(list1[i], int):
        list1[i] *= 10

# =================================================================== #
# =================================================================== #

list_a = [1, 50, 3, 60, 2, 7, 21, 31, 13]

# 짝수로 구성된 리스트 작성
even_list = sorted([num for num in list_a if num % 2 == 0])

# 홀수로 구성된 리스트 작성
odd_list = sorted([num for num in list_a if num % 2 != 0])

# =================================================================== #
# =================================================================== #

one_digit_count = 0
two_digit_count = 0
three_digit_count = 0
numbers = []

# 10개의 수 입력 받기
for _ in range(10):
    number = int(input("Enter a number: "))
    numbers.append(number)

    # 자릿수 카운트
    if number < 10:
        one_digit_count += 1
    elif number < 100:
        two_digit_count += 1
    else:
        three_digit_count += 1

# 결과 출력
print(numbers)
print(one_digit_count, two_digit_count, three_digit_count)

# =================================================================== #
# =================================================================== #

# 빈 딕셔너리 만들기
my_dict = {}

# one, two, three를 key로 하고 각각의 값이 하나, 둘, 셋인 딕셔너리 만들기
my_dict['one'] = '하나'
my_dict['two'] = '둘'
my_dict['three'] = '셋'

# 단어 입력 받기
word = input("단어를 입력하세요: ")

# 입력된 단어에 해당하는 값 출력
if word in my_dict:
    print(my_dict[word])
else:
    print("해당하는 단어의 값이 없습니다.")

# =================================================================== #
# =================================================================== #

# 빈 딕셔너리 만들기
info_dict = {}

# 이름, 나이, 몸무게를 key로 하는 딕셔너리 만들기
info_dict['이름'] = '홍길동'
info_dict['나이'] = 26
info_dict['몸무게'] = 82

# 정보 출력
for key, value in info_dict.items():
    print(f"{key} : {value}")

# =================================================================== #
# =================================================================== #

foods = {
    "떡볶이": "오뎅",
    "짜장면": "단무지",
    "라면": "김치",
    "피자": "피클",
    "맥주": "땅콩",
    "치킨": "치킨무",
    "삼겹살": "상추"
}

# key 맥주의 value를 오징어로 수정
foods["맥주"] = "오징어"

# 위의 딕셔너리에서 피자 항목이 있는지 알아보고 있으면 삭제
if "피자" in foods:
    del foods["피자"]

# 궁합 출력
print("다음 음식의 궁합은 좋아요.")
for food, side_dish in foods.items():
    print(f"{food}-{side_dish},", end=" ")

# =================================================================== #
# =================================================================== #

fruits = ("apple", "banana", "grape")

# 튜플을 리스트로 변환한 후 pear, kiwi 항목을 추가
fruits_list = list(fruits)
fruits_list.append("pear")
fruits_list.append("kiwi")
fruits = tuple(fruits_list)

# 튜플 간의 + 연산을 사용하여 pear, kiwi 항목을 추가
fruits = fruits + ("pear", "kiwi")

# =================================================================== #
# =================================================================== #

# 주사위를 두 번 던져 나오는 경우에 대한 프로그램

# 1. 각 경우의 합을 리스트, 집합으로 각각 구하기

dice_sums_list = []  # 리스트 초기화
dice_sums_set = set()  # 집합 초기화

for i in range(1, 7):
    for j in range(1, 7):
        dice_sum = i + j
        dice_sums_list.append(dice_sum)  # 리스트에 추가
        dice_sums_set.add(dice_sum)  # 집합에 추가

print("각 경우의 합 (리스트):", dice_sums_list)
print("각 경우의 합 (집합):", dice_sums_set)

# 2. 눈의 합이 6이 되는 경우를 리스트, 집합으로 각각 구하기

sum_6_list = []  # 리스트 초기화
sum_6_set = set()  # 집합 초기화

for i in range(1, 7):
    for j in range(1, 7):
        dice_sum = i + j
        if dice_sum == 6:
            sum_6_list.append((i, j))  # 리스트에 추가
            sum_6_set.add((i, j))  # 집합에 추가

print("눈의 합이 6인 경우 (리스트):", sum_6_list)
print("눈의 합이 6인 경우 (집합):", sum_6_set)

# =================================================================== #
# =================================================================== #

# 두 문자열에서 공통적인 글자 추출하는 프로그램

# 첫 번째 문자열 입력 받기
string1 = input("첫 번째 문자열: ")

# 두 번째 문자열 입력 받기
string2 = input("두 번째 문자열: ")

# 첫 번째 문자열과 두 번째 문자열을 집합으로 변환하여 공통된 글자 추출
common_chars = set(string1) & set(string2)

# 추출된 공통 글자 출력
print("공통적인 글자:", " ".join(common_chars))

# =================================================================== #
# =================================================================== #

# 입력 문장 받기
sentence = input("입력 문장: ")

# 문장을 공백을 기준으로 단어로 분리하여 집합으로 변환
words = set(sentence.split())

# 중복되지 않은 단어의 개수 출력
print("사용된 단어의 개수 =", len(words))
print(words)

# =================================================================== #
# =================================================================== #

import math

# 첫 번째 수식 계산
result1 = 7 * (2 + 2 * math.cos(450) * math.sin(600))

# 두 번째 수식 계산
result2 = 2 * math.sin(300) * math.sin(600) + math.exp(20)

# 결과 출력
print("첫 번째 수식 결과:", result1)
print("두 번째 수식 결과:", result2)

# =================================================================== #
# =================================================================== #

# 1. 1에서 100까지의 숫자를 5번 입력 받아 파일에 저장
with open('data5.txt', 'w') as f:
    for _ in range(5):
        num = int(input("숫자 입력: "))
        f.write(str(num) + '\n')

# 2. 저장된 파일을 읽어 숫자 중 홀수를 전부 곱한 결과 구하기
with open('data5.txt', 'r') as f:
    product = 1
    for line in f:
        num = int(line.strip())
        if num % 2 != 0:
            product *= num

print("홀수의 곱:", product)

# =================================================================== #
# =================================================================== #

def print_newline():
    print("[0, 6]")
    print("[0, 2, 3, 4, 6, 8, 9]")
    print("[0, 6]")

# 함수 호출
print_newline()

# =================================================================== #
# =================================================================== #

list1 = [10, 20, 30, 40, 50]
list2 = [sum(list1[0:i+1]) for i in range(len(list1))]

print("list1 =", list1)
print("list2 =", list2)

# =================================================================== #
# =================================================================== #

orders = [["1", "자장면", 5, 5500],  # 주문번호, 메뉴, 수량, 단가
          ["2", "짬뽕", 3, 6000],
          ["3", "볶음밥", 3, 6500],
          ["4", "탕수육", 2, 15000]]

result = []  # 결과를 담을 빈 리스트

# 주문 리스트를 순회하면서 각 주문에 대한 주문번호와 주문가격 계산
for order in orders:
    order_number = order[0]  # 주문번호
    order_price = order[2] * order[3]  # 수량 * 단가
    result.append((order_number, order_price))  # 결과 리스트에 주문번호와 주문가격을 튜플로 추가

print(result)  # 결과 출력

# =================================================================== #
# =================================================================== #

numbers = range(1, 11)
sqrt_values = map(lambda x: (x, x ** 0.5), numbers)

for number, sqrt in sqrt_values:
    print("{}의 제곱근은 {:.2f}".format(number, sqrt))

# =================================================================== #
# =================================================================== #