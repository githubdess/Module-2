# print('Первый вариант решения: ')
# while True:
#     my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
#     my_list = [i for i in my_list if i > 0]
#     for i in my_list:
#         print(i)
#     break
#
# print('Второй вариант решения: ')
my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while i < len(my_list):
    if my_list[i] == 0:
        i += 1
    if my_list[i] < 0:
        break
    if my_list[i] > 0:
        print(my_list[i])
        i += 1
