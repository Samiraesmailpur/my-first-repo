# 1
import random

# 5 объявление функции generator с аргументом number
def generator(number):
    subject = random.randint(1, 4)
    if number > subject:
        print('number > ', subject);
        return False
    elif number == subject:
        print("==", subject)
        return True
    else:
        print('number < ', subject)
        return False

# 3 объявление функции main без аргументов
def main():
    print("hello player")
    while True:

        text = input("what is the number?")

        try:
            # Переменной number мы ПРИСВАЕВАЕМ РЕЗУЛЬТАТ ВЫПОЛНЕНИЯ ФУНКЦИИ int()
            # передавая как аргумент переменную text
            number = int(text)
        except ValueError:
            print('entered value is not a number')
            exit(0)

        # 4
        # Переменной is_correct мы ПРИСВАЕВАЕМ РЕЗУЛЬТАТ ВЫПОЛНЕНИЯ ФУНКЦИИ generator(number)
        # передавая как аргумент переменную number
        is_correct = generator(number)
        # если is_correct True
        if is_correct:
            print("you are winner")
            break
        else:
            end = input("Do you want to continue? [yes/no]")
            if end == "no":
                break

# 2 вызов функции main без аргументов
main()

