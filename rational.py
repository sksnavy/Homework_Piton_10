# Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования 

import rational as rat
import sys

def x():
    firstnum = float(input('Введите первое рациональное число: ').replace(',', '.'))
    return firstnum

def y():
    secondnum = float(input('Введите второе рациональное число: ').replace(',', '.'))
    return secondnum

def selectoperation():
    global rateration
    operation = (input(f'Введите действие (+, -, *, /) одним символом:'))
    if operation == '+' or '-' or '/' or '*':
        return operation
    else:
        print('Неверное значение')

def res(num_1, num_2, operation):
    if  operation == '+':
        res = num_1 + num_2
        result = round(res, 3)
        return result
    elif operation == '-':
        res = num_1 - num_2
        result = round(res, 3)
        return result
    elif operation == '*':
        res = num_1 * num_2
        result = round(res, 3)
        return result
    elif operation == '/':
        res = num_1 / num_2
        result = round(res, 3)
        return result
    else:
        print('Неверное значение')

def main():
    global file
    x = rat.x()
    while True:
        y = rat.y()
        oper = rat.selectoperation()
        res = rat.res(x, y, oper)
        file = 'results.txt'
        with open('results.txt', 'a') as data:
            data.write(f'Результат: {x} {oper} {y} = {res}\n')
        print(f'Результат: {x} {oper} {y} = {res}\n(записано в файл results.txt)' )
        again = input('Хотите продолжить работу с комплексными числами? (Y or N)')
        if again == 'Y' or again == 'y':
            useresult = input('Хотите использовать последний результат операции? (Y/N): ')
            if useresult == 'Y' or useresult == 'y':
                x = res
                continue
            elif useresult == 'N':
                break
            else:
                sys.exit()           
        else:   
            sys.exit()