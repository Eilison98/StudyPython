# 문자열 리스트
fruits = ['banana', 'apple', 'orange', 'kiwi']
print(fruits)

# 리스트 추가
fruits.append('bin')

# 리스트 삭제
del fruits[3]

fruits.remove('apple')

# in 연산자
if ('kiwi' in fruits):
    fruits.remove('kiwi')

# insert
fruits.insert(1, 'bery')