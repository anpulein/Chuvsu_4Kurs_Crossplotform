import random

# Получаем случайное число в диапозоне (1 - 1000)
number = random.randint(1, 1000)
strMin = '{0} меньше загаданного мною числа!'
strMax = '{0} больше загаданного мною числа!'
inputNumber = 0
print('Здравствуйте, я загадал число от 1 до 1000. Попробуйте угадать число, которое я загадал?')

while inputNumber != number:
    inputNumber = int(input('Введите число: '))
    print(strMin.format(inputNumber)) if inputNumber < number else print(strMax.format(inputNumber))

print(f'Подзравляю, вы отгадали число правильно! Это {inputNumber}')