#1


#2
numbers = range(1, 11)
sqrt_list = list(map(lambda x: (x, x ** 0.5), numbers))

for number, sqrt in sqrt_list:
    print("{}의 제곱근은 {:.2f}".format(number, sqrt))