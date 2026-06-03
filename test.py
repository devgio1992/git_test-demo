numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

double = [x**2 for x in numbers]
print(double)


odd = [x for x in numbers if x % 2 != 0]
print(odd)
