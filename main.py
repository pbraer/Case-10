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