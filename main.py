# Case-study №10
# Developers:   Braer P. (75%),
#               Kokorina D. (50%),
#               Novoselov V. (0%)

print("""Case-study Игра
Разработчики:
Браер П.С., Кокорина Д.Е., Новоселов В.В.
""")

from random import randint

# start info

info = {'treasury': 1000, 'land': 0, 'seedling': 0, 'population': 10000, 'opposite': 0, 'money': 500}


# menu function


def menu(info, step, price):
    if step == 2:
        return
    print('Баланс: ', info['money'], ' Л.', sep='')
    print('''
    1. Хозяйство
    2. Магазин земли
    3. Магазин растений
    4. Казна
    5. Ополченцы
    6. Ничего не делать сегодня
    7. Завершить игру досрочно
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
    elif choice == 7:
        info = {}
    return info



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
        earth_buy(info, step + 1, price)
    elif to_buy == 2:
        if info['money'] < 250:
            print('Недостаточно средств!')
            earth_buy(info, step, price)
        info['money'] = info['money'] - 250
        info['land'] = info['land'] + 25
        earth_buy(info, step + 1, price)
    elif to_buy == 3:
        if info['money'] < 500:
            print('Недостаточно средств!')
            earth_buy(info, step, price)
        info['money'] = info['money'] - 500
        info['land'] = info['land'] + 50
        earth_buy(info, step + 1, price)
    elif to_buy == 4:
        menu(info, step, price)
    else:
        print('Неправильно введен ответ. Попробуйте еще раз!')
        earth_buy(info, step, price)



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
    to_buy = int(input('Введите число наборов саженцев, которое вы хотите купить: '))
    if to_buy == 0:
        menu(info, step, price)
    elif to_buy * price > info['money']:
        print('Недостаточно средств!')
        plant_buy(info, step, price)
    elif to_buy > info['land']:
            print('Недостаточно земли!')
            plant_buy(info, step, price)
    else:
        info['seedling'] = info['seedling'] + to_buy
        info['money'] -= price * to_buy
        plant_buy(info, step + 1, price)


def treasury_info(info, step, price):
    print()
    print('В казне планеты Кеплер лежит ', info['treasury'], ' Л.', sep='')
    print()
    print('Сколько Либров вы хотите пожертвовать в казну? (Введите "0", если не хотите жертвовать.)')
    print('Ваш баланс: ', info['money'], ' Л.', sep='')
    answer = int(input())
    if answer == 0:
        menu(info, step, price)
    info['money'] -= answer
    info['treasury'] += answer
    menu(info, step + 1, price)


def opposite_info(info, step, price):
    number = info['opposite']
    if number % 10 == 1 and number // 10 % 10 != 1:
        word = 'инопланетянин.'
    elif 2 <= number % 10 <= 4 and number // 10 % 10 != 1:
        word = 'инопланетянина.'
    else:
        word = 'инопланетян.'
    print()
    print('Сейчас против вас ', info['opposite'], ' ', word, sep='')
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
    return info


def space_flights(info):
    print()
    print('Обязательное пожертвование на полеты в другие галактики для увеличения населения!')
    info['population'] += 1000
    if info['treasury'] <= 200:
        print('-', info['treasury'], ' Л. из казны      +1000 к населению', sep='')
        info['treasury'] = 0
    else:
        print('-200 Л. из казны     +1000 к населению')
        info['treasury'] -= 200
    print()
    return info


def research(info):
    print('''
    Планируются научные исследования. Срочно необходимы земли для экспериментов!
    Поделитесь ли вы землей с учеными?
    1. Да
    2. Нет
    ''')
    answer = int(input())
    if answer == 1:
        if info['land'] <= 300:
            print('-', info['land'], ' Га      ', sep='', end='')
            info['land'] = 0
            info['seedling'] = 0
        else:
            print('-300 Га      ', sep='', end='')
            info['land'] -= 300
            info['seedling'] = 0
        if info['opposite'] >= 50:
            info['opposite'] -= 50
            print('-50 к оппозиции', sep='')
        else:
            print('-', info['opposite'], ' к оппозиции', sep='')
            info['opposite'] = 0
    return info


def war(info):
    print()
    print('На планету Кеплер прилетели захватчики и развязалась война... срочно нужны средства на оборону.')
    info['opposite'] += 100
    print('+100 к оппозиции     ', sep='', end='')
    if info['treasury'] <= 300:
        print('-', info['treasury'], ' Л. из казны      ', sep='', end='')
        info['treasury'] = 0
    else:
        info['treasury'] -= 300
        print('-300 Л. из казны     ', sep='', end='')
    if info['land'] <= 200:
        print('-', info['land'], ' Га', sep='')
        info['land'] = 0
        info['seedling'] = 0
    else:
        info['land'] = info['land'] - 200
        info['seedling'] = 0
        print('-200 Га', sep='')
    return info
    print()


def purchases(info):
    print()
    print('Сборы средств на государственные закупки рассады')
    info['money'] -= 100
    print('-100 Л.', sep='')
    print()
    return info


def explosion(info):
    print()
    print('Из-за неправильной работы разработчиков на космической станции произошел взрыв.')
    info['opposite'] += 300
    print('+300 к оппозиции     ', sep='', end='')
    info['population'] -= 500
    print('-1000 от населения')
    print()
    return info


def var(info):
    x = randint(1, 7)
    if x == 1:
        info = tornado(info)
    elif x == 2:
        info = space_flights(info)
    elif x == 3:
        info = research(info)
    elif x == 4:
        info = war(info)
    elif x == 5:
        info = purchases(info)
    elif x == 6:
        info = explosion(info)
    return info


# main functions

def greetings():
    print('''
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      Приветствуем вас! К сожалению, вы больше не на планете Земля... Вы попали на планету Кеплер.
    Чтобы выжить, необходимо не только прокормить себя, но и наладить контакт с местными жителями
     - инопланетянами.
      Правительство выделило вам 500 Либров на обустройство. Вы можете выращивать растения на 
    собственной земле, предварительно купив ее, и зарабатывать на этом себе на жизнь. Не забывайте 
    жертвовать Либры в инопланетную казну, иначе население может разозлиться...
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ''')


def game(info):
    death = 0
    for day in range(1, 21):
        info['money'] += info['seedling']
        if death == 5:
            print('''
            ▄▀▀░ ▄▀▄ █▄░▄█ █▀▀     ▄▀▄ ▐▌░▐▌ █▀▀ █▀▀▄ 
            █░▀▌ █▀█ █░█░█ █▀▀     █░█ ░▀▄▀░ █▀▀ █▐█▀ 
            ▀▀▀░ ▀░▀ ▀░░░▀ ▀▀▀     ░▀░ ░░▀░░ ▀▀▀ ▀░▀▀ 
            в ы  п о г и б л и  о т  г о л о д а
            ''')
            break
        if info['money'] <= 0:
            print('''
            ▄▀▀░ ▄▀▄ █▄░▄█ █▀▀     ▄▀▄ ▐▌░▐▌ █▀▀ █▀▀▄ 
            █░▀▌ █▀█ █░█░█ █▀▀     █░█ ░▀▄▀░ █▀▀ █▐█▀ 
            ▀▀▀░ ▀░▀ ▀░░░▀ ▀▀▀     ░▀░ ░░▀░░ ▀▀▀ ▀░▀▀ 
            у  в а с  з а к о н ч и л и с ь  л и б р ы
            ''')
            break
        elif info['opposite'] >= 1000:
            print('''
            ▄▀▀░ ▄▀▄ █▄░▄█ █▀▀     ▄▀▄ ▐▌░▐▌ █▀▀ █▀▀▄ 
            █░▀▌ █▀█ █░█░█ █▀▀     █░█ ░▀▄▀░ █▀▀ █▐█▀ 
            ▀▀▀░ ▀░▀ ▀░░░▀ ▀▀▀     ░▀░ ░░▀░░ ▀▀▀ ▀░▀▀ 
            с л и ш к о м  м н о г о  о п п о з и ц и о н е р о в
            ''')
            break
        elif info['treasury'] <= 0:
            print('''
            ▄▀▀░ ▄▀▄ █▄░▄█ █▀▀     ▄▀▄ ▐▌░▐▌ █▀▀ █▀▀▄ 
            █░▀▌ █▀█ █░█░█ █▀▀     █░█ ░▀▄▀░ █▀▀ █▐█▀ 
            ▀▀▀░ ▀░▀ ▀░░░▀ ▀▀▀     ░▀░ ░░▀░░ ▀▀▀ ▀░▀▀ 
            в  к а з н е  з а к о н ч и л и с ь  л и б р ы
            ''')
            break
        print('---------------------------')
        print('          ДЕНЬ ', day, sep='')
        print('---------------------------')
        step = 1
        price = randint(1, 50)
        info = menu(info, step, price)
        print()
        if info == {}:
            print()
            print('ИГРА ЗАВЕРШЕНА ДОСРОЧНО')
            break
        probability = randint(0, 1)
        if probability == 1:
            info = var(info)
        print()
        if day == 20:
            print('''
            ▄▀▀░ ▄▀▄ ▄▀▄ █▀▄     ▄▀▀░ ▄▀▄ █▄░▄█ █▀▀ 
            █░▀▌ █░█ █░█ █░█     █░▀▌ █▀█ █░█░█ █▀▀ 
            ▀▀▀░ ░▀░ ░▀░ ▀▀░     ▀▀▀░ ▀░▀ ▀░░░▀ ▀▀▀ 
            п о з д р а в л я е м  с  п о б е д о й !
            ''')
        if info['land'] <= 0 or info['seedling'] <= 0:
            death += 1
        else:
            death -= 1


greetings()
game(info)
