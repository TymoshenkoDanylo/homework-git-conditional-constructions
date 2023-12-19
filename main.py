# 1. Користувач вводить три цифри з клавіатури.
# Залежно від вибору користувача програма виводить на екран максимум із трьох,
# мінімум із трьох або середньоарифметичне трьох чисел.

number1 = int(input("Please, enter a number 1:\t"))
number2 = int(input("Please, enter a number 2:\t"))
number3 = int(input("Please, enter a number 3:\t"))

word: str = str(input("Choose a solution (\'max\', \'min\', \'average\'):\t"))

if word == 'max':
    if number1 >= number2 and number1 >= number3:
        print("max = " + str(number1))
    elif number2 >= number3 and number2 >= number1:
        print("max = " + str(number2))
    else:
        print("max = " + str(number3))
elif word == 'min':
    if number1 <= number2 and number1 <= number3:
        print("min = " + str(number1))
    elif number2 <= number1 and number2 <= number3:
        print("min = " + str(number2))
    else:
        print("min = " + str(number3))
elif word == 'average':
    print("Average = " + str((number1+number2+number3)/3))
else:
    print("Error! Incorrect input value!")

# 2. Користувач вводить з клавіатури кількість метрів.
# Залежно від вибору користувача програма переводить метри милі, дюйм або ярди.
#
# meters = float(input("Enter the number of meters :\t"))
#
# values = str(input("Enter the value (\'mil\', \'duim\', \'yard\':\t"))
#
# if values == 'mil':
#     print("Miles = " + str((meters / 1000) * 0.6214))
# elif values == 'yard':
#     print("Yards = " + str(meters * 1.0936133))
# elif values == 'duim':
#     print("Inches = " + str(meters * 39.3700787))
# else:
#     print("Error! Incorrect input value!")
