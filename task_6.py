"""
6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.

Примеры строк файла:

Информатика:   100(л)   50(пр)   20(лаб)
Физика:   30(л)   —   10(лаб)
Физкультура:   —   30(пр)   —

Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

my_f = open("task_6.txt", "r", encoding='utf-8')
my_dict = {}
buffer_count = ""
content = my_f.readline()
while content != "":
    buffer = content.split()
    amount = 0
    for el in range(1, 4):
        if buffer[el] != "-":
            buffer_str = buffer[el]
            for i in range(len(buffer[el])):
                if buffer_str[i] != "(":
                    buffer_count += buffer_str[i]
                else:
                    break
            amount += int(buffer_count)
            buffer_count = ""
    buffer[0] = buffer[0][:-1]
    my_dict[buffer[0]] = amount
    content = my_f.readline()
my_f.close()
print(my_dict)


