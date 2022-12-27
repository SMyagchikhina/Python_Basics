"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""


# вариант первый
from random import randint

with open('ex5.txt', 'w', encoding='utf-8') as f:
    lst = [randint(1, 20) for _ in range(50)]
    f.write(' '.join(map(str, lst)))

print(lst)
print('Сумма чисел: ', sum(lst))
print()


# вариант второй
str_obj = "1 2 3 4 5"
res = 0

with open("output_file.txt", "w", encoding='utf-8') as f_obj:
    f_obj.write(str_obj)

with open("output_file.txt", encoding='utf-8') as f_obj:
    content = f_obj.read().split(" ")
    for n in content:
        res = res + int(n)
    print(str_obj)
    print(f"Сумма чисел = {res}")

    
