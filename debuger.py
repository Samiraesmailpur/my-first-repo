
import re
print(re.match("^\s$", " ") is not None)
print(re.match("^\s$", "3") is not None)

#2
print(re.match("^\d$", "D") is not None)
print(re.match("^\d$", "4") is not None)

#3
print(re.match("^\d\d$", "32") is not None)
print(re.match("^\d\d$", "3") is not None)

#4
print(re.match("^\s\s\s$", '   ') is not None)
print(re.match("^\s\s\s$", '333') is not None)

#5
print(re.match("^\w\w\w$", "a4v") is not None)

print(re.match("^a\dv$", "a4v") is not None)


#6
print(re.match("^a\d+c$", "a34c") is not None)

#7
print(re.match("^a\d*c$", "a23c") is not None)
print(re.match("^a\d*c$", "ac") is not None)
print(re.match("^(a\d+c|ac)$", "ac") is not None)

#8
print(re.match("^a\d*c$", "a23c") is not None)

#9
x = re.match("^<privet>(.+)<privet>$", "<privet> privet kak dela<privet>").groups()
print(x[0])

#10
def func(x):
    try:
        y = re.match("^\d{4}-\d{2}-\d{2}\s\d{2}:(\d{2}):\d{2}$", x).groups()
        return y[0]
    except Exception as e:
        print('not a time')

print(func("2018-01-09 12:32:04"))


#11
def func1(x):
    try:
        y = re.match("^(\w+.\w+\d+)@gmail.com$", x).groups()
        return y[0]

    except Exception as e:
        print('only email')
print(func1('super.sonya1223@gmail.com'))



# x = None
# while x != '3':
#     x = input('Меню:\n1. Добавить новый контакт'
#               '\n2. Посмотреть список всех номеров'
#               '\n3. Выход\n')
#     if x == '1':
#         with open('data.txt', 'a') as file:
#             answer = input('Введите имя и фамилию:') + ' '
#             file.write(answer)
#             answer = input('Введите номер:') + ' '
#             file.write(answer + '\n')
#             print('Абонент сохранен')
#     elif x == '2':
#         with open('data.txt', 'r') as file:
#             data = file.read()
#         for y in data.split('\n'):
#             print(y)
#
# print('bye')


x = None
while x != '4':
    x = input('Меню:\n1. Добавить новый контакт'
              '\n2. Посмотреть список всех номеров'
              '\n3. Обновить контакт'
              '\n4. Выход\n')
    if x == '1':
        with open('data.txt', 'a') as file:
            answer = input('Введите имя и фамилию:') + ' '
            file.write(answer)
            answer = input('Введите номер:') + ' '
            file.write(answer + '\n')
            print('Абонент сохранен')
    elif x == '2':
        with open('data.txt', 'r') as file:
            data = file.read()
        for y in data.split('\n'):
            print(y)
    elif x == '3':
        with open('data.txt', 'r') as file:
            data = file.read()
        n = 0
        slovar = {}
        for y in data.split('\n'):
            n += 1
            slovar[n] = y
            print(str(n) + '.' + y)
        answer2 = input('Какого абонента хотите обновить?')
        answer3 = input('Что хотите обновить(имя или номер?')
        a = slovar[int(answer2)]
        с = slovar[int(answer2)]
        if answer3 == 'имя':
            name = input('Введите имя и фамилию:')
            b = a.split(' ')
            b[0] = name
            b = ' '.join(b)
            slovar[int(name)] = b
            with open('data.txt', 'w') as file:
                v = '\n'.join(slovar.values())
                data = file.write(v)

        elif answer3 == 'номер':
            number = input('Введите номер:')
            s = с.split(' ')
            s[1] = number
            s = ' '.join(s)
            slovar[int(number)] = s
            with open('data.txt', 'w') as file:
                p = '\n'.join(slovar.values())
                data = file.write(p)













print('bye')

