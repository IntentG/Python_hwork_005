'''Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.'''

list = ["boat", "car", "5", "cut", "12","floor", "67", "meat", "0", "cat"]

findNumber = input("Введите число, которое будем искать в списке:    ")

def FindNumberInList(number):
    if number.isdigit() == True:
        result = "Совпадений нет"
        for i, digit in enumerate(list):
            if digit.isdigit() == True:
                number = int(number)
                digit = int(digit)
                if number == digit:
                    result = (f"Число {number} присутствует в списке!")
    else:
        result = "Вы ввели не числовое значение!"
    return result

print(FindNumberInList(findNumber))
