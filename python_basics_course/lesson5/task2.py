'''
Задание 2

Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
'''
data = []
nums = []
with open('task2_file.txt') as file:
    for i in file:
        data.append(i)
    for i in data:
        nums.append(len(i))

print(f'Всего строк в файле: {len(data)}')
for i in range(len(data)):
    print(f'В {i}-й строке содержится {nums[i]} символов')
