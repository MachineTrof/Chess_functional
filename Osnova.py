from Peshka import *
from Horse import *
from Elephant import *
from Rook import *
from Queen import *
from King import *

#Функция по выводу игрового поля на экран
def print_Pole():
    for l in range(len(Pole)):
        print()
        for f in range(len(Pole[l])):
            print((Pole[l])[f] + ' ', end = '')
    print('\n')

#Функция хода игры
def XodIgroka(ig,fig):
    global OK #Переменная, отвечающая за изменение поля в ведённых координатах
    OK = True
    Xalph = '12345678'
    Yalph = 'ABCDIFGK'
    Konvert = {'A':1, 'B':2, 'C':3, 'D':4, 'I':5, 'F':6, 'G':7, 'K':8} #Словарь конвертации буквенных координат в цифровые
    print(ig + ', ваш ход! Ваши фигуры: ' + fig)
    print('Введите координаты фигуры, которой вы бы хотели походить:')
    #Ввод координат игроком, проверка на корректность введённых значений
    KorVvod = False
    while KorVvod == False:
        X = str(input('Введите нужную строку (1,2,3,4,5,6,7,8) = '))
        Y = str(input('Введите нужный столбец (A,B,C,D,I,F,G,K) = '))
        if (X in Xalph) and (Y in Yalph):
            try:
                X = int(X)
                Y = Konvert[Y]
                figure = (Pole[X])[Y]
                if figure in fig:
                    KorVvod = True
                else:
                    print('Там нет вашей фигуры, введите координаты ещё раз!')
            except:
                print('Некорректный ввод, попробуйте ещё раз!')
        else:
            print('Некорректный ввод, попробуйте ещё раз!')
    #Определение, какой фигурой будет ходить игрок
    if figure in 'Pp':
        XodPeshka(figure,X,Y,Pole)
    elif figure in 'Hh':
        XodHorse(figure,X,Y,Pole)
    elif figure in 'Ee':
        XodElephant(figure,X,Y,Pole)
    elif figure in 'Rr':
        XodRook(figure,X,Y,Pole)
    elif figure in 'Qq':
        XodQueen(figure,X,Y,Pole)
    else:
        XodKing(figure,X,Y,Pole)
    #Если ход несостоялся по причине его невозможности (например король окружён своими), то меняем переменную ОК на false, что не позволит в будущем перейти ходу в руки иного игрока
    if (Pole[X])[Y] in 'PpHhEeRrQqKk':
        OK = False

#Приветствуем игроков и рассказываем им об условных обозначениях
print('Приветствуем вас в симуляторе Шахмат!')
print('Правила игры стандартные, а обозначения фигур следующие:')
print('Пешка - P или p')
print('Конь - H или h')
print('Слон - E или e')
print('Ладья - R или r')
print('Ферзь - Q или q')
print('Король - K или k')
print('Один игрок будет играть за "строчных", другой - за "ЗАГЛАВНЫХ"')
print()

#Игроки вводят свои ники, создаётся словарь ников, игрокам присваиваются их фигуры (через словарь фигур)
Ig1 = str(input('Игрок "ЗАГЛАВНЫХ", введите свой ник = '))
Ig2 = str(input('Игрок "строчных", введите свой ник = '))
Ig = {0:Ig1, 1:Ig2}
F1 = 'PRHEQK'
F2 = 'prheqk'
Fig = {0:F1, 1:F2}

#Выводится игровое поле
strK = [' ','A','B','C','D','I','F','G','K',' ']
str1 = ['1','r','h','e','q','k','e','h','r','1']
str2 = ['2','p','p','p','p','p','p','p','p','2']
str3 = ['3','-','-','-','-','-','-','-','-','3']
str4 = ['4','-','-','-','-','-','-','-','-','4']
str5 = ['5','-','-','-','-','-','-','-','-','5']
str6 = ['6','-','-','-','-','-','-','-','-','6']
str7 = ['7','P','P','P','P','P','P','P','P','7']
str8 = ['8','R','H','E','Q','K','E','H','R','8']
Pole = [strK,str1,str2,str3,str4,str5,str6,str7,str8,strK]
print_Pole()

#Ход игры и её конец
Xod = 0
mat = False #Т.к. мат не был реализован, как и шах, игра будет идти "бесконечно" - атака короля шахматными фигурами не предусмотрена
while mat == False:
    XodIgroka(Ig[Xod%2],Fig[Xod%2])
    if OK == True:
        Xod += 1
        print_Pole()
print('Победил ' + Ig[(Xod-1)%2])
