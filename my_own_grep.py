import argparse
import os

def main(args):
    # объявили функцию main в которая ожидает аргументы file, query
    # в переменную text мы присваеваем результат выполнения функции open
    # результатом выполнения функции open есть открытый файл в режиме чтения
    # на отрытом файле вызывается метод
    print(len(args))
    if len(args) < 2:
        raise ValueError

    if not os.path.isfile(args[0]):
        raise NameError

    text = open(args[0], "r").readlines()
    for string in text:
        if args[1] in string:
            print(string)


# вызов функции main с предачей аргументов в виде 2-х строк
parser = argparse.ArgumentParser(description='Process some strings.')
parser.add_argument('strings', type=str, nargs='+',
                    help='an strings for the accumulator')


main(parser.parse_args().strings)
