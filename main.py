# 1. Користувач вводить три цифри з клавіатури.
# Залежно від вибору користувача програма виводить на екран максимум із трьох,
# мінімум із трьох або середньоарифметичне трьох чисел.

number1 = int(input("Please, enter a number 1:\t"))
number2 = int(input("Please, enter a number 2:\t"))
number3 = int(input("Please, enter a number 3:\t"))

word: str = str(input("Choose a solution (\'max\', \'min\', \'average\'):\t"))

if word == 'max':
    if number1 >= number2:
        print("max = " + str(number1))
    elif number2 >= number3:
        print("max = " + str(number2))
    else:
        print("max = " + str(number3))
elif word == 'min':
    if number1 <= number2:
        print("min = " + str(number1))
    elif number2 <= number3:
        print("min = " + str(number2))
    else:
        print("min = " + str(number3))
elif word == 'average':
    print("Average = " + str((number1+number2+number3)/3))
else:
    print("Error! Incorrect input value!")
