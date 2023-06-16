def XodQueen(figure,X,Y,Pole):
    konvert = {1:'A', 2:'B', 3:'C', 4:'D', 5:'I', 6:'F', 7:'G', 8:'K'} #Конвертация цифр в буквы
    Konvert = {'A':1, 'B':2, 'C':3, 'D':4, 'I':5, 'F':6, 'G':7, 'K':8} #Конвертация букв в цифры
    if figure == 'Q':
        VragAlph = 'prheq'
    else:
        VragAlph = 'PRHEQ'
    VozmXods = {}
    k = 1
    kontrol = True #Засекает, если кто-то (или что-то) мешает "царице Катерине" пройти туда, куда она возжелала
    #Берём код у крылатых гусар-ладьиев
    Xt = X
    while kontrol == True: #Вверх
        Xt += 1
        if (Pole[Xt])[Y] == '-':
            VozmXods[k] = [Xt,konvert[Y]]
            k += 1
        else:
            if (Pole[Xt])[Y] in VragAlph:
                VozmXods[k] = [Xt,konvert[Y]]
                k += 1
            kontrol = False
    kontrol = True
    Xt = X
    while kontrol == True: #Вниз
        Xt -= 1
        if (Pole[Xt])[Y] == '-':
            VozmXods[k] = [Xt,konvert[Y]]
            k += 1
        else:
            if (Pole[Xt])[Y] in VragAlph:
                VozmXods[k] = [Xt,konvert[Y]]
                k += 1
            kontrol = False
    kontrol = True
    Yt = Y
    while kontrol == True: #Вправо
        Yt += 1
        if (Pole[X])[Yt] == '-':
            VozmXods[k] = [X,konvert[Yt]]
            k += 1
        else:
            if (Pole[X])[Yt] in VragAlph:
                VozmXods[k] = [X,konvert[Yt]]
                k += 1
            kontrol = False
    kontrol = True
    Yt = Y
    while kontrol == True: #Влево
        Yt -= 1
        if (Pole[X])[Yt] == '-':
            VozmXods[k] = [X,konvert[Yt]]
            k += 1
        else:
            if (Pole[X])[Yt] in VragAlph:
                VozmXods[k] = [X,konvert[Yt]]
                k += 1
            kontrol = False
    #Одалживаем код у мудрых индусов на слонах
    Xt, Yt = X, Y
    while kontrol == True: #По диагонали вправо вверх
        Xt += 1
        Yt += 1
        if (Pole[Xt])[Yt] == '-':
            VozmXods[k] = [Xt,konvert[Yt]]
            k += 1
        else:
            if (Pole[Xt])[Yt] in VragAlph:
                VozmXods[k] = [Xt,konvert[Yt]]
                k += 1
            kontrol = False
    kontrol = True
    Xt, Yt = X, Y
    while kontrol == True: #По диагонали влево вниз
        Xt -= 1
        Yt -= 1
        if (Pole[Xt])[Yt] == '-':
            VozmXods[k] = [Xt,konvert[Yt]]
            k += 1
        else:
            if (Pole[Xt])[Yt] in VragAlph:
                VozmXods[k] = [Xt,konvert[Yt]]
                k += 1
            kontrol = False
    kontrol = True
    Xt, Yt = X, Y
    while kontrol == True: #По диагонали влево вверх
        Xt += 1
        Yt -= 1
        if (Pole[Xt])[Yt] == '-':
            VozmXods[k] = [Xt,konvert[Yt]]
            k += 1
        else:
            if (Pole[Xt])[Yt] in VragAlph:
                VozmXods[k] = [Xt,konvert[Yt]]
                k += 1
            kontrol = False
    kontrol = True
    Xt, Yt = X, Y
    while kontrol == True: #По диагонали вправо вниз
        Xt -= 1
        Yt += 1
        if (Pole[Xt])[Yt] == '-':
            VozmXods[k] = [Xt,konvert[Yt]]
            k += 1
        else:
            if (Pole[Xt])[Yt] in VragAlph:
                VozmXods[k] = [Xt,konvert[Yt]]
                k += 1
            kontrol = False
    if k == 1:
        print('Данной фигурой невозможно походить, выберите другую!')
        return
    print(VozmXods)
    Korrekt = False
    while Korrekt == False:
        try:
            Vibor = int(input('Выберите, куда вы походите, введя нужную цифру = '))
            if Vibor >= 1 and Vibor <= k:
                Korrekt = True
                x = (VozmXods[Vibor])[0]
                y = Konvert[(VozmXods[Vibor])[1]]
            else:
                print('Некорректный ввод выбора! Попробуйте ещё раз!')
        except:
            print('Некорректный ввод выбора! Попробуйте ещё раз!')
    (Pole[X])[Y], (Pole[x])[y] = '-', figure
