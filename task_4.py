"""
4)	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

dic = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open('ex4_trans.txt', 'w', encoding='utf-8') as f_write:
    with open('ex4.txt', 'r', encoding='utf-8') as f_read:
        for line in f_read:
            f_write.writelines([line.replace(line.split()[0], dic[line.split()[0]])])


