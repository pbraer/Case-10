# Case-study №10
# Developers:   Braer P. (%),
#               Kokorina D. (%),
#               Novoselov V. (%)

print("""Case-study Игра
Разработчики:
Браер П.С., Кокорина Д.Е., Новоселов В.В.
""")

from random import randint

# start info

info = {}
info['treasury'] = 1000
info['land'] = 0
info['seedling'] = 0
info['population'] = 10000
info['opposite'] = 0
info['money'] = 600
# menu function


def menu(info, step, price):
    if step == 2:
        return
    print('''
    1. Хозяйство
    2. Магазин земли
    3. Магазин растений
    3. Казна
    4. Ополченцы
    5. Ничего не делать сегодня
    6. Завершить игру досрочно
    ''')
    choice = int(input())
    if choice == 1:
        land_info(info, step, price)
    elif choice == 2:
        earth_buy(info, step, price)
    elif choice == 3:
        plant_buy(info, step, price)
    elif choice == 4:
        treasury_info(info, step, price)
    elif choice == 5:
        opposite_info(info, step, price)
    elif choice == 6:
        return info
    elif choice == 7:
        return {}



# action functions


def land_info(info, step, price):
    print()
    print('Земля: ', info['land'], ' Га.    Саженцы: ', info['seedling'], ' шт.', sep='')
    print()
    menu(info, step, price)


def earth_buy(info, step, price):
    if step == 2:
        return info
    print('---------------------------')
    print('''
    1. Маленький участок  10 Га  100 Либров
    2. Средний участок    25 Га  250 Либров
    3. Большой участок    50 Га  500 Либров
    4. Выход из магазина
    ''')
    print('---------------------------')
    print('Ваш баланс: ', info['money'], ' Л.', sep='')
    print()
    to_buy = int(input('Выберите действие: '))
    if to_buy == 1:
        if info['money'] < 100:
            print('Недостаточно средств!')
            earth_buy(info, step, price)
        info['money'] = info['money'] - 100
        info['land'] = info['land'] + 10
        earth_buy(info, step, price)
        step += 1
    if to_buy == 2:
        if info['money'] < 250:
            print('Недостаточно средств!')
            earth_buy(info, step, price)
        info['money'] = info['money'] - 250
        info['land'] = info['land'] + 25
        earth_buy(info, step, price)
        step += 1
    if to_buy == 3:
        if info['money'] < 500:
            print('Недостаточно средств!')
            earth_buy(info, step, price)
        info['money'] = info['money'] - 500
        info['land'] = info['land'] + 50
        step += 1
        earth_buy(info, step, price)
    if to_buy == 4:
        menu(info, step, price)


def plant_buy(info, step, price):
    if step == 2:
        return info
    print('---------------------------')
    print('Сегодня один саженец Инопланта стоит ', price, ' Л.', sep='')
    print('(С одного саженца можно получать 1 Либр ежедневно!)')
    print('---------------------------')
    print('Ваш баланс: ', info['money'], ' Л.', sep='')
    print('Чтобы вернуться в Меню, введите "0"')
    print()
    to_buy = int(input('Введите число саженцев, которое вы хотите купить: '))
    if to_buy == 0:
        menu(info, step, price)
    elif to_buy * price > info['money']:
        print('Недостаточно средств!')
    else:
        info['seedling'] = info['seedling'] + to_buy
        info['money'] -= price * to_buy
        step += 1
        plant_buy(info, step, price)


def treasury_info(info, step, price):
    print()
    print('В казне планеты Кеплер лежит ', info['treasury'], ' Л.', sep='')
    print()
    menu(info, step, price)


def opposite_info(info, step, price):
    number = info['opposite']
    if number % 10 == 1 and number // 10 % 10 != 1:
        word = 'инопланетянин.'
    elif 2 <= number % 10 <= 4 and number // 10 % 10 != 1:
        word = 'инопланетянина.'
    else:
        word = 'инопланетян.'
    print()
    print('Сейчас против вас', info['opposite'], ' ', word, sep='')
    print()
    menu(info, step, price)


# random events functions


def tornado(info):
    print('На планете Кеплер произошло торнадо. Количество растений уменьшилось')
    if info['treasury'] < 100:
        info['treasury'] = 0
    else:
        info['treasury'] -= 100
    if info['seedling'] < 50:
        info['seedling'] = 0
    else:
        info['seedling'] -= 50


def space_flights(info):
    print('Обязательное пожертвование на полеты в другие галактики для увеличения населения!')
    info['population'] += 1000
    if info['treasury'] <= 200:
        info['treasury'] = 0
    else:
        info['treasury'] -= 200


def research(info):
    print('..')
    if info['land'] <= 300:
        info['land'] = 0
    else:
        info['land'] += 300
    if info['opposite'] >= 50:
        info['opposite'] -= 50
    else:
        info['opposite'] = 0


def war(info):
    print('На планету Кеплер прилетели захватчики и развязалась война... срочно нужны средства на оборону.')
    info['opposite'] += 100
    if info['treasury'] <= 300:
        info['treasury'] = 0
    else:
        info['treasury'] -= 300
    if info['land'] <= 200:
        info['land'] = 0
    else:
        info['land'] = info['land'] - 200


def purchases(info):
    info['seedling'] = info['seedling'] + 50
    print('Сборы средств на государственные закупки рассады')
    if info['treasury'] < 50:
        info['treasury'] = 0
    else:
        info['treasury'] = 50


def explosion(info):
    print('Из-за неправильной работы разработчиков на космической станции произошел взрыв.')
    info['opposite'] += 300
    if info['population'] < 500:
        info['population'] = 0
    else:
        info['population'] = info['population'] - 500


def var(info):
    x = randint(1, 7)
    if x == 1:
        tornado(info)
    elif x == 2:
        space_flights(info)
    elif x == 3:
        research(info)
    elif x == 4:
        war(info)
    elif x == 5:
        purchases(info)
    elif x == 6:
        explosion(info)
    return info


# main function



for day in range(1, 21):
    if info == {}:
        break
    if info['money'] <= 5 or info['opposite'] >= 1000 or info['population'] <= 10: #?
        print('''

        ▄▀▀░ ▄▀▄ █▄░▄█ █▀▀     ▄▀▄ ▐▌░▐▌ █▀▀ █▀▀▄ 
        █░▀▌ █▀█ █░█░█ █▀▀     █░█ ░▀▄▀░ █▀▀ █▐█▀ 
        ▀▀▀░ ▀░▀ ▀░░░▀ ▀▀▀     ░▀░ ░░▀░░ ▀▀▀ ▀░▀▀ 

        ''')
        break
    print('---------------------------')
    print('          ДЕНЬ ', day, sep='')
    print('---------------------------')
    step = 1
    price = randint(1, 50)
    info = menu(info, step, price)
    probability = randint(0, 1)
    if probability == 1:
        info = var(info)


