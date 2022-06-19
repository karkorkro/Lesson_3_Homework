new_list = []
list_len = int(input('Задайте длину списка: '))
for i in range(1, list_len+1):
    element = int(input(f"Введите {i} элемент:"))
    new_list.append(element)
print(sorted(new_list))
