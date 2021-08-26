# Игра про выживание монстрика в мире Меча и Магии.
import random
import time
import pygame, sys
from pygame.locals import *

names = {1 : "Мышь Полевая", 2 : "Заяц", 3 : "Лиса", 4 : "Волк", 5 : "Лось", 6 : "Селянин", 7 : "Медведь", 8 : "Сельский Охотник"}
frq = {1:128, 2:64, 3:32, 4:16, 5:8, 6:4, 7:2, 8:1}   # С какой частотой встречаются мобы
hp = {1:2, 2:5, 3:10, 4:13, 5:18, 6:20, 7:25, 8:29}   #значение Жизней
damage = {1:0, 2:2, 3:5, 4:10, 5:10, 6:13, 7:25, 8:13}    #значение Урона
xp = {1:1, 2:3, 3:5, 4:7, 5:7, 6:10, 7:15, 8:20, 9:5, 10:3, 11:5}    #значение опыта получемого при победе
lovk = {1:4, 2:2, 3:2, 4:2, 5:1, 6:4, 7:1, 8:5, 9:2}  # Ловкость влияет на шансы уклониться
speed = {1:4, 2:3, 3:6, 4:4, 5:3, 6:3, 7:6, 8:7, 9:6, 10:3, 11:6} # Скорость влияет на шансы сбежать, избежав битвы
iq = {1:0, 2:0, 3:0, 4:0, 5:0, 6:1, 7:0, 8:2}    # Интеллект персонажа, влияет на скорость восполнения маны

# Переменные
myname = "a"
myxp = 0    # Опыт персонажа
mylevel = 0    # Уровень персонажа
myiq = 0    # Интеллект персонажа, влияет на скорость восполнения маны
mymana = 0    # Текущее количество Маны персонажа
myManaUses = 0    # Текущее количество Маны персонажа
myRegenChance = 1    # Шанс в 1% случайно отрегенерировать ХР
killed = 0    # Количество убитых врагов - сбрасывается при росте damag
killedTotal = 0    # Количество убитых врагов за всю игру
maxFreq = 0    # сумма всех соотношений встречи мобов
lenght = 0    # длина словаря
# генерируем параметры песонажа
myHpMax = random.randint(1,9)    # генерируем Макс.Жизней рандомом
myhp =  random.randint(1,myHpMax)    # генерируем значение Жизней
mydamag = random.randint(1,5)    # генерируем значение рандомом
mylovk = random.randint(1,5)    # генерируем значение Ловкости
myspeed = random.randint(1,5)    # генерируем значение рандомом
myManaMax = random.randint(1,5)   # генерируем значение рандомом

# Настройки PyGame
pygame.init()
DISPLAYSURF = pygame.display.set_mode((200, 500))
pygame.display.set_caption('Monter  RPG')

WHITE = (255, 255, 255)
Black = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
RED = (255, 0, 0)

fontObj = pygame.font.Font('freesansbold.ttf', 16)

# Game begin here
print('Ваш персонаж - монстр. Которого случайным порталом')
time.sleep(1)   # задержка между поялением следующей строчки 1 секунда
print('забросило в мир Меча и Магии')
time.sleep(1)
print('Чтоб вернуться домой вам нужно Выжить и найти портал')
time.sleep(1)
myname = input("Введите имя свого персонажа ")
time.sleep(1)
print(f'Жизней {myhp} из {myHpMax}, Урон {mydamag}, Ловкость {mylovk}, Скорость {myspeed}, Максимум Маны {myManaMax}')

lenght = len(names) + 1
for x in range (1,lenght):
    maxFreq = maxFreq + frq[x]

# Функция вывода Жизней
def Show_Hp():
    textSurfaceObj = fontObj.render(f'Жизней: {myhp}/{myHpMax} ', True, Black)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.topleft = (10, 10)

    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    pygame.display.update()
    return

# Функция описания нашей Героической смерти
def die(id):
    print(f"Вы умерли сражась с коварным {names[id]}")
    return

# Функция проверки роста максисмума жизней
def hp_growup():
    global myhp
    global myHpMax
    if myHpMax <= myhp:
        myHpMax = myHpMax + 1
        myhp = myHpMax
    return

# Функция роста Damaga
def damag_growup():
    global killed
    global killedTotal
    global mydamag
    killed = killed + 1    # Количество убитых врагов - сбрасывается при росте damag
    killedTotal = killedTotal + 1    # Количество убитых врагов за всю игру
    if killed >= 100:
        killed = 0
        mydamag = mydamag + 1
        print("убив очередную Сотню живых существ, вы научились делать это лучше")
        print(f"Ваш урон вырос и равен {mydamag}")
    return

# Функция Регенерации от поедания Пищи
def feed():
    global myhp
    print(f"перед вами тело {names[enemy_id]}, вы можете его съесть и восстановить {enemy_id} здоровъя.")
    do = input("Съедите ли вы его Да(д) или Нет(н)")
    if do not in ['д', 'н', 'y', 'n', 'Д', 'Н', 'Y', 'N']:
        print('Не правильный ввод! Вам засчитывается Отказ от поедания противника')
        do = 'н'
    if do =='д' or do =='y' or do =='Д' or do =='Y':
        myhp = myhp + enemy_id
        hp_growup()
        print(f"После питания у вас {myhp} жизней")
        return
    else:
        print(f"Вы бросили труп не тронутым")
        return

# Функция боя с противником
def fight():
    global myhp
    global myxp
    enHp = hp[enemy_id]
    while myhp > 0 or enHp > 0:# битва идёт пока наше здоровье или противника не опустилось в Ноль
        enHp = enHp - mydamag   # лупим врага со всей своей богатырской силушкой
        if enHp > 0:    # Если враг Всё ещё жив, то:
            myhp = myhp - damage[enemy_id]   # Он лупит нас в ответ
            if myhp <=0:   # Если после удара врага Ты уже НЕ жив, то:
                die(enemy_id)      # вызываем функцию с описанием нашей героической Смерти
                return
        else:    # Если враг уже НЕ жив, то Вы победили:
            myxp = myxp + xp[enemy_id]    # Опыт персонажа растёт
            print(f"Противник убит, вы получили опыт, теперь у вас {myhp} жизней и {myxp} опыта")
            damag_growup()
            feed()      # вызываем функцию поедания врага
            return

#  Функция Генерируем противника
def gen_enemy():
    global enemy_id
    global enemy
    chance = random.randint(1,2)    # генерируем шанс встретить противника рандомом
    if chance == 1:
        Q = random.randint(1,maxFreq)   # генерируем противника рандомом
        if Q <= frq[1]:
            enemy_id = 1
        elif frq[1] < Q <= (frq[1] + frq[2]):
            enemy_id = 2
        elif (frq[1] + frq[2]) < Q <= (frq[1] + frq[2] + frq[3]):
            enemy_id = 3
        elif (frq[1] + frq[2] + frq[3]) < Q <= (frq[1]+frq[2]+frq[3]+frq[4]):
            enemy_id = 4
        elif (frq[1]+frq[2]+frq[3]+frq[4])<Q<=(frq[1]+frq[2]+frq[3]+frq[4]+frq[5]):
            enemy_id = 5
        elif (frq[1]+frq[2]+frq[3]+frq[4]+frq[5])<Q<=(frq[1]+frq[2]+frq[3]+frq[4]+frq[5]+frq[6]):
            enemy_id = 6
        elif (frq[1]+frq[2]+frq[3]+frq[4]+frq[5]+frq[6])<Q<=(frq[1]+frq[2]+frq[3]+frq[4]+frq[5]+frq[6]+frq[7]):
            enemy_id = 7
        elif (frq[1]+frq[2]+frq[3]+frq[4]+frq[5]+frq[6]+frq[7])<Q<=(frq[1]+frq[2]+frq[3]+frq[4]+frq[5]+frq[6]+frq[7]+frq[8]):
            enemy_id = 8
        #enemy_id = random.randint(1,3)   # генерируем противника рандомом
        enemy = names[enemy_id]
        print(f"Вы встретили {names[enemy_id]}")
        do = input("Что будешь делать Убегать(у) или Атаковать(а)")
        if do not in ['у', 'а','y', 'a','Y', 'A','У', 'А']:
            print('Не правильный ввод! Вам засчитывается Трусливый побег')
            do = "у"
        if do =='а' or do =='a' or do =='A' or do =='А':
            print("Вы решили Атаковать противника")
            fight()
            return
        else:
            print(f"Вы решили Избежать боя с {names[enemy_id]}")
            return
    else:
        print("Вы мирно прошли по лесу")
    return

# Функция Случайной Регенерации
def rnd_regen():
    global myhp
    rnd = random.randint(1,100)   # генерируем значение рандомом
    if rnd == 1:
        myhp =  myhp + 1
        hp_growup()
        print(f"Вы случайно отрегенирировали 1ХР, теперь у вас {myhp}ХР")
    return

# Играем пока у нас остётся здоровье или жизни
while myhp > 0:
    DISPLAYSURF.fill(WHITE)
    Show_Hp()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            break
    pygame.display.update()
    gen_enemy()
    rnd_regen()
print(f"Игра для вас закончилась. За всё это время вы лишили жизней {killedTotal} живых существ")