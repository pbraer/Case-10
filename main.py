# Case-study №10
# Developers:   Braer P. (%),
#               Kokorina D. (%),
#               Novoselov V. (%)

print("""Case-study Игра
Разработчики:
Браер П.С., Кокорина Д.Е., Новоселов В.В.
""")

# start info

info = {'treasury': 1000, 'land': 0, 'seedling': 0, 'population': 10000, 'opposite': 0, 'money': 500}

# action functions

def menu(info):
    print('''
    1. Хозяйство
    2. Магазин земли
    3. Магазин растений
    3. Казна
    4. Ополченцы
    5. Завершить игру досрочно
    ''')


def earth_buy(info):
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
            earth_buy(info)
        info['money'] = info['money'] - 100
        info['land'] = info['land'] + 10
        earth_buy(info)
    if to_buy == 2:
        if info['money'] < 250:
            print('Недостаточно средств!')
            earth_buy(info)
        info['money'] = info['money'] - 250
        info['land'] = info['land'] + 25
        earth_buy(info)
    if to_buy == 3:
        if info['money'] < 500:
            print('Недостаточно средств!')
            earth_buy(info)
        info['money'] = info['money'] - 500
        info['land'] = info['land'] + 50
        earth_buy(info)
    if to_buy == 4:
        menu(info)


def tornado(info):
    print('На планете Кеплер произошло торнадо. Количество растений уменьшилось')
    if info['treasury'] < 100:
        info['treasury'] == 0
    else:
        info['treasury'] -= 100
    if info['seedling'] < 50:
        info['seedling'] == 0
    else:
        info['seedling'] -= 50

def space_flights(info):
    print('Обязательное пожертвование на полеты в другие галактики для увеличения населения!')
    info['population'] += 1000
    if info['treasury'] <= 200:
        info['treasury'] == 0
    else:
        info['treasury'] -= 200

def research(info):
    print('..')
    if info['land'] <= 300:
        info['land'] == 0
    else:
        info['land'] += 300
    if info['opposite'] >= 50:
        info['opposite'] -= 50
    else:
        info['opposite'] == 0

def war(info):
    print('На планету Кеплер прилетели захватчики и развязалась война... срочно нужны средства на оборону.')
    info['opposite'] += 100
    if info['treasury'] <= 300:
        info['treasury'] == 0
    else:
        info['treasury'] -= 300
    if info['land'] <= 200:
        info['land'] == 0
    else:
        info['land'] -= 200

def purchases(info):
    info['seedling'] += 50
    print('Сборы средств на государственные закупки рассады')
    if info['treasury'] < 50:
        info['treasury'] == 0
    else:
        info['treasury'] -= 50

def explosion(info):
    print('Из-за неправильной работы разработчиков на космической станции произошел взрыв.')
    info['opposite'] += 300
    if info['population'] < 500:
        info['population'] == 0
    else:
        info['population'] -= 500




