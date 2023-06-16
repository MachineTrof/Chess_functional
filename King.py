def XodKing(figure,X,Y,Pole):
    konvert = {1:'A', 2:'B', 3:'C', 4:'D', 5:'I', 6:'F', 7:'G', 8:'K'} #Конвертация цифр в буквы
    Konvert = {'A':1, 'B':2, 'C':3, 'D':4, 'I':5, 'F':6, 'G':7, 'K':8} #Конвертация букв в цифры
    if figure == 'K':
        VragAlph = 'prheq-'
    else:
        VragAlph = 'PRHEQ-' 
    VozmXods = {}
    k = 1
    try:
        if (Pole[X+1])[Y+1] in VragAlph:
            VozmXods[k] = [X+1,konvert[Y+1]]
            k += 1
    except:
        pass
    try:
        if (Pole[X+1])[Y-1] in VragAlph:
            VozmXods[k] = [X+1,konvert[Y-1]]
            k += 1
    except:
        pass
    try:
        if (Pole[X+1])[Y] in VragAlph:
            VozmXods[k] = [X+1,konvert[Y]]
            k += 1
    except:
        pass
    try:
        if (Pole[X])[Y+1] in VragAlph:
            VozmXods[k] = [X,konvert[Y+1]]
            k += 1
    except:
        pass
    try:
        if (Pole[X])[Y-1] in VragAlph:
            VozmXods[k] = [X,konvert[Y-1]]
            k += 1
    except:
        pass
    try:
        if (Pole[X-1])[Y+1] in VragAlph:
            VozmXods[k] = [X-1,konvert[Y+1]]
            k += 1
    except:
        pass
    try:
        if (Pole[X+1])[Y-1] in VragAlph:
            VozmXods[k] = [X+1,konvert[Y-1]]
            k += 1
    except:
        pass
    try:
        if (Pole[X-1])[Y] in VragAlph:
            VozmXods[k] = [X-1,konvert[Y]]
            k += 1
    except:
        pass #Если выйдем за поле, то не должны пострадать все варианты. Потому сделали для каждого возможного хода try-except
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
