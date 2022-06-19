numbers = input('Введите элементы списка через запятую: ')
numbers = numbers.replace(',', ' ').split()
print(list(set(numbers)))




