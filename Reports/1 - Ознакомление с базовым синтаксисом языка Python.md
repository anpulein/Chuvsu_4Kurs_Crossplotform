<div>
<p align="center" style="font-size=14pt; font-weight: bolder;">МИНИСТЕРСТВО НАУКИ И ВЫСШЕГО ОБРАЗОВАНИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ
<br>
Федеральное государственное бюджетное учреждение высшего образования
<br>
«Чувашский государственный университет И.Н. Ульянова»
<br>
Факультет информатики и вычислительной техники 
<br>
Кафедра вычислительной техники
<br> <br> <br> <br> <br> <br> <br><br> <br> <br>
Кросс-платформенные средства разработки программного обеспечения
<br>
Лабораторная работа 1
<br>
«Ознакомление с базовым синтаксисом языка Python»
</p>

<br> <br> <br> <br><br> <br><br>

<span>
<p align="right" style="font-size=14pt; font-weight: bolder;">Выполнил:</p>
<p align="right" style="font-size=14pt;">Студент группы ИВТ-41-20 <br>
Галкин Д.С.
</p>
</span> <br>

<span>
<p align="right" style="font-size=14pt; font-weight: bolder;">Проверил:</p>
<p align="right" style="font-size=14pt;">Ковалев С.B.</p>
</span>

<br> <br>
<br> <br>
<br> <br>
<br> <br>
<p align="center" style="font-size=10pt;">Чебоксары, 2023</p>
<div style="page-break-after:always;  visibility:hidden"></div>
</div>

### Цель работы:

1. Установка интерпретатора Python
2. Усановка и ознакомление со средой разработки JetBrains PyCharm
3. Ознакомление с базовым синтаксисом языка Python, прежде всего, с операторами цикла и ветвления
4. Получение практических навыков программирования приложений с использованием консольного ввода/вывода
5. Реалезация простейшей программы, взаимодействия с пользователем

> [!info] Задание для выполнения
> В лабораторной работе необходимо реализовать простейший вариант игры «угадай число». Компьютер загадывает число от одного до ста и предлагает пользователю угадать это число. После каждого ответа от пользователя, компьютер сообщает, больше или меньше загаданного числа введенное пользователем значение. Игра продолжается до тех пор, пока пользователь не угадает число. Пример диалога с пользователем приведен ниже

![[CleanShot 2023-11-03 at 19.31.15@2x.png]]

К программе предъявляются следующие требования:
1. Число, загаданное компьютером, должно выбираться заново при каждом запуске программы, что потребует использования дополнительного модуля из стандартной библиотеки Python
2. Сообщения для пользователя должны быть максимально информативны. Для формирования сообщений необходимо использовать f-string
3. В рамках данной лабораторной работы считается что пользователь всегда корректно вводит данные (только числа) и выполнять дополнительную проверку не требуется
<div style="page-break-after:always;  visibility:hidden"></div>
### Полный текст программы:

```python
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
```