def XodPeshka(figure,X,Y,Pole):
    konvert = {1:'A', 2:'B', 3:'C', 4:'D', 5:'I', 6:'F', 7:'G', 8:'K'} #Конвертация цифр в буквы
    Konvert = {'A':1, 'B':2, 'C':3, 'D':4, 'I':5, 'F':6, 'G':7, 'K':8} #Конвертация букв в цифры
    #Такое разветвление (в отличие от других фигур) по двум причинам: Уникальные движения пешками (одни "вверх", другие - "вниз"), Уникальный набор замен пешек
    if figure == 'P':
        VragAlph = 'prheq'
        VozmXods = {}
        k = 1
        #Выявляем возможные ходы...
        if (Pole[X-1])[Y] == '-':
            VozmXods[k] = [X-1,konvert[Y]]
            k += 1
        if (Pole[X-1])[Y+1] in VragAlph:
            VozmXods[k] = [X-1,konvert[Y+1]]
            k += 1
        if (Pole[X-1])[Y-1] in VragAlph:
            VozmXods[k] = [X-1,konvert[Y-1]]
            k += 1
        if X == 7 and ((Pole[X-1])[Y] == '-') and ((Pole[X-2])[Y] == '-'):
            VozmXods[k] = [X-2,konvert[Y]]
        if k == 1:
            print('Данной фигурой невозможно походить, выберите другую!')
            return
        #И даём выбор игроку...
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
        #Замена пешки, если она доковыляла до другого края
        if x == 1:
            Korrekt = False
            while Korrekt == False:
                Nf = str(input('Выберите замену пешки (R,H,E,Q) = '))
                if Nf in 'RHEQ':
                    Korrekt = True
            (Pole[x])[y] = Nf
    #"То же самое", что и сверху
    else:
        VragAlph = 'PRHEQ'
        VozmXods = {}
        k = 1
        if (Pole[X+1])[Y] == '-':
            VozmXods[k] = [X+1,konvert[Y]]
            k += 1
        if (Pole[X+1])[Y+1] in VragAlph:
            VozmXods[k] = [X+1,konvert[Y+1]]
            k += 1
        if (Pole[X+1])[Y-1] in VragAlph:
            VozmXods[k] = [X+1,konvert[Y-1]]
            k += 1
        if X == 2 and ((Pole[X+1])[Y] == '-') and ((Pole[X+2])[Y] == '-'):
            VozmXods[k] = [X+2,konvert[Y]]
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
        if x == 8:
            Korrekt = False
            while Korrekt == False:
                Nf = str(input('Выберите замену пешки (r,h,e,q) = '))
                if Nf in 'rheq':
                    Korrekt = True
            (Pole[x])[y] = Nf
