'''
Задание 1
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
'''
divisible1 = []
divisible2 = []
divisible3 = []
divisible4 = []
divisible5 = []
divisible6 = []
divisible7 = []
divisible8 = []
divisible9 = []

for i in range(9):
    for number in range(2, 100):
        if number % 2 == 0 and number not in divisible2:
            divisible2.append(number)
        elif number % 3 == 0 and number not in divisible3:
            divisible3.append(number)
        elif number % 4 == 0 and number not in divisible4:
            divisible4.append(number)
        elif number % 5 == 0 and number not in divisible5:
            divisible5.append(number)
        elif number % 6 == 0 and number not in divisible6:
            divisible6.append(number)
        elif number % 7 == 0 and number not in divisible7:
            divisible7.append(number)
        elif number % 8 == 0 and number not in divisible8:
            divisible8.append(number)
        elif number % 9 == 0 and number not in divisible9:
            divisible9.append(number)

# print(f'''В диапазоне чисел [2;99]:
#            кратных 2 -- {(divisible2)}
#            кратных 3 -- {(divisible3)}
#            кратных 4 -- {(divisible4)}
#            кратных 5 -- {(divisible5)}
#            кратных 6 -- {(divisible6)}
#            кратных 7 -- {(divisible7)}
#            кратных 8 -- {(divisible8)}
#            кратных 9 -- {(divisible9)}
#            ''')

print(f'''В диапазоне чисел [2;99]:
            кратных 2 -- {len(divisible2)}
            кратных 3 -- {len(divisible3)}
            кратных 4 -- {len(divisible4)}
            кратных 5 -- {len(divisible5)}
            кратных 6 -- {len(divisible6)}
            кратных 7 -- {len(divisible7)}
            кратных 8 -- {len(divisible8)}
            кратных 9 -- {len(divisible9)}
            ''')
