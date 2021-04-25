'''
Задание 4

Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
'''

diction = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('task4_final_data.txt', 'w', encoding='utf-8') as file1:
    with open('task4_file.txt', encoding='utf-8') as file2:
        file1.writelines([data.replace(data.split()[0], diction.get(data.split()[0])) for data in file2])
