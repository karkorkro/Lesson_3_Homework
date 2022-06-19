list1 = input('Введите элементы 1 списка через запятую: ')
list1 = list1.replace(',', ' ').split()
list2 = input('Введите элементы 2 списка через запятую: ')
list2 = list2.replace(',', ' ').split()
combined_list = set(list1) - set(list2)
print(list(combined_list))


list1 = input('Введите элементы 1 списка через запятую: ')
list1 = list1.replace(',', ' ').split()
list2 = input('Введите элементы 2 списка через запятую: ')
list2 = list2.replace(',', ' ').split()
list3 = []
for i in list1:
    if i not in list2:
        list3.append(i)
print(list3)