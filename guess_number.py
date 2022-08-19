import random

print('Добро пожаловать в числовую угадайку!')
print('Хотите выбрать диапазон загадывания случайного числа? Введите да или нет')
#print('Введите число от 1 до 100')

def is_valid(s):
    return s.isdigit() and 1 <= int(s) <= 100


def is_valid_num():
    while True:
        number = input()
        if is_valid(number):
            return int(number)
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')


def digit_generation():
    answer = input()
    while answer != 'да' or answer != 'нет':
        if answer.lower() == 'да':
            print('Пожалуйста, введите число правой границы диапазона')
            right_edge = int(input())
            print('Теперь введите число от 1 до', right_edge)
            break
        elif answer.lower() == 'нет':
            right_edge = 100
            print('Теперь введите число от 1 до', right_edge)
            break
        elif answer.lower() != 'да' and answer.lower() != 'нет':
            print('Введите корректный ответ')
            answer = input()
    count = 0
    rand_num = random.randrange(1, right_edge + 1)
    while True:
        num = is_valid_num()
        if num == rand_num:
            count += 1
            if count == 1:
                print('Вы угадали всего за', count,'попытку, поздравляем!')
                one_more_time()
                break
            elif 2 <= count <= 4:
                print('Вы угадали всего за', count,'попытки, поздравляем!')
                one_more_time()
                break
            elif 5 <= count < 21:
                print('Вы угадали всего за', count,'попыток, поздравляем!')
                one_more_time()
                break
            else:
                print('Количество ваших попыток не счесть, но вы молодец!')
                one_more_time()
                break
        elif num < rand_num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            count += 1
        elif num > rand_num:
            print('Ваше число больше загаданного, попробуйте еще разок')
            count += 1
    #print('Спасибо, что играли в числовую угадайку. Еще увидимся...')

def one_more_time():
    print('Хотите сыграть ещё разок? Введите да или нет')
    answer_omt = input()
    while answer_omt != 'да' or answer_omt != 'нет':
        if answer_omt.lower() == 'да':
            digit_generation()
            break
        elif answer_omt.lower() == 'нет':
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break
        else:
            print('Не понимаю ваш ответ, повторите еще раз')
            answer_omt = input()

digit_generation()