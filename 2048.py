import random
from colored import fg, bg, attr
import os
os.system('cls' if os.name == 'nt' else 'clear')

color_code = {
    '-': 0,
    2: 20,
    4: 25,
    8: 30,
    16: 35,
    32: 41,
    64: 45,
    128: 50,
    256: 55,
    512: 60,
    1024: 65,
    2048: 70
    }

table = {
    '11': '-',
    '21': '-',
    '31': '-',
    '41': '-',
    '12': '-',
    '22': '-',
    '32': '-',
    '42': '-',
    '13': '-',
    '23': '-',
    '33': '-',
    '43': '-',
    '14': '-',
    '24': '-',
    '34': '-',
    '44': '-'}


def savegame():
    with open('savegame.csv', 'w') as f:
        t = []
        for k, v in table.items():
            t.append('{key}: {value}'.format(key=str(k), value=(v)))
        f.write(','.join(t))
    print('Saved!')


def loadgame():

    def isint(x):
        try:
            int(x)
            return int(x)
        except ValueError:
            return str(x)

    with open('savegame.csv', 'r') as f:
        global table
        table = {}
        t = f.read().split(',')
        for i in t:
            values = i.split(': ')
            table[values[0]] = isint(values[1])


def printtable():
    os.system('cls' if os.name == 'nt' else 'clear')
    score = []
    for k, v in table.items():
        score.append(v)
    score = filter(lambda x: type(x) == int, score)
    print("You can 'save' and 'load'!")
    print('\n')
    print("Score: ", sum(score))
    print('\n')
    print(
        '{background} {:^4}'.format(table['11'], background=bg(color_code[table['11']])),
        '{background} {:^4}'.format(table['21'], background=bg(color_code[table['21']])),
        '{background} {:^4}'.format(table['31'], background=bg(color_code[table['31']])),
        '{background} {:^4}'.format(table['41'], background=bg(color_code[table['41']])))
    print(
        '{background} {:^4}'.format(table['12'], background=bg(color_code[table['12']])),
        '{background} {:^4}'.format(table['22'], background=bg(color_code[table['22']])),
        '{background} {:^4}'.format(table['32'], background=bg(color_code[table['32']])),
        '{background} {:^4}'.format(table['42'], background=bg(color_code[table['42']])))
    print(
        '{background} {:^4}'.format(table['13'], background=bg(color_code[table['13']])),
        '{background} {:^4}'.format(table['23'], background=bg(color_code[table['23']])),
        '{background} {:^4}'.format(table['33'], background=bg(color_code[table['33']])),
        '{background} {:^4}'.format(table['43'], background=bg(color_code[table['43']])))
    print(
        '{background} {:^4}'.format(table['14'], background=bg(color_code[table['14']])),
        '{background} {:^4}'.format(table['24'], background=bg(color_code[table['24']])),
        '{background} {:^4}'.format(table['34'], background=bg(color_code[table['34']])),
        '{background} {:^4}'.format(table['44'], background=bg(color_code[table['44']])))
    print(attr(0))


def span2():
    table[random.choice(list([i for i, j in table.items() if j == '-']))] = 2


def upCollumn(x):
    for y in range(3):
        z = 0
        for b in range(3):
            z = z + 1
            if table[str(x) + str(z)] == '-':
                table[str(x) + str(z)] = table[str(x) + str(z + 1)]
                table[str(x) + str(z + 1)] = '-'
    for y in range(3):
        z = 0
        for b in range(3):
            z = z + 1
            if table[str(x) + str(z)] != '-' and table[str(x) + str(z)] == table[str(x) + str(z + 1)]:
                table[str(x) + str(z)] = table[str(x) + str(z)] * 2
                table[str(x) + str(z + 1)] = '-'


def downCollumn(x):
    for y in range(3):
        z = 5
        for b in range(3):
            z = z - 1
            if table[str(x) + str(z)] == '-':
                table[str(x) + str(z)] = table[str(x) + str(z - 1)]
                table[str(x) + str(z - 1)] = '-'
    for y in range(3):
        z = 5
        for b in range(3):
            z = z - 1
            if table[str(x) + str(z)] != '-' and table[str(x) + str(z)] == table[str(x) + str(z - 1)]:
                table[str(x) + str(z)] = table[str(x) + str(z)] * 2
                table[str(x) + str(z - 1)] = '-'


def leftRow(x):
    for y in range(3):
        z = 0
        for b in range(3):
            z = z + 1
            if table[str(z) + str(x)] == '-':
                table[str(z) + str(x)] = table[str(z + 1) + str(x)]
                table[str(z + 1) + str(x)] = '-'
    for y in range(3):
        z = 0
        for b in range(3):
            z = z + 1
            if table[str(z) + str(x)] != '-' and table[str(z) + str(x)] == table[str(z + 1) + str(x)]:
                table[str(z) + str(x)] = table[str(z + 1) + str(x)] * 2
                table[str(z + 1) + str(x)] = '-'


def rightRow(x):
    for y in range(3):
        z = 5
        for b in range(3):
            z = z - 1
            if table[str(z) + str(x)] == '-':
                table[str(z) + str(x)] = table[str(z - 1) + str(x)]
                table[str(z - 1) + str(x)] = '-'
    for y in range(3):
        z = 5
        for b in range(3):
            z = z - 1
            if table[str(z) + str(x)] != '-' and table[str(z) + str(x)] == table[str(z - 1) + str(x)]:
                table[str(z) + str(x)] = table[str(z - 1) + str(x)] * 2
                table[str(z - 1) + str(x)] = '-'


def up():
    for z in range(3):
        z = 0
        for w in range(4):
            upCollumn(z + 1)
            z = z + 1


def down():
    for z in range(3):
        z = 0
        for w in range(4):
            downCollumn(z + 1)
            z = z + 1


def left():
    for z in range(3):
        z = 0
        for w in range(4):
            leftRow(z + 1)
            z = z + 1


def right():
    for z in range(3):
        z = 0
        for w in range(4):
            rightRow(z + 1)
            z = z + 1


def keypress():
    valid = ['a', 'w', 's', 'd', 'save', 'load']
    while True:
        try:
            L = input('next move: ')
            if L not in valid:
                raise ValueError
            break
        except BaseException:
            print('Invalid input!')
    return L


span2()  # Here starts the game
span2()
printtable()
while True:
    try:
        L = keypress()
        if L == 'w':
            up()
        elif L == 's':
            down()
        elif L == 'a':
            left()
        elif L == 'd':
            right()
        elif L == 'save':
            savegame()
        elif L == 'load':
            loadgame()
        if L == 'load' or L == 'save':
            pass
        else:
            span2()
        printtable()
    except IndexError:
        print('\nNot allowed move!')
        break
