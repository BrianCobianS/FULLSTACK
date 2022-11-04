def changeBat(fileDirectory, wordToFind, wordToChange, incremento):
    with open(fileDirectory,'r') as archivo:
        i=0
        j=0
        pos=[]
        for linea in archivo:
            if linea == wordToFind:
                print("match")
                pos.append(i)
                j=j+1
            i=i+1
        print("posicion del cambio = ", pos)

    contenido = open(fileDirectory).read().splitlines()
    for index in range(len(pos)):
        print(pos[index])
        contenido.insert(pos[index]-incremento,wordToChange)
    f = open(fileDirectory, "w")
    f.writelines("\n".join(contenido))

def erasepauses(archivo):
    contenido = open(archivo).read().splitlines()
    def loop(x):
        for l in range(x):
            x=0
            try:
                contenido.remove("if not exist nopause pause")
                x=x+1
            except Exception as e:
                n=0
            try:
                contenido.remove("PAUSE > NUL")
                x=x+1
            except Exception as e:
                n=0
            try:
                contenido.remove("    pause")
                x=x+1
            except Exception as e:
                n=0
            try:
                contenido.remove("PAUSE")
                x=x+1
            except Exception as e:
                n=0
            try:
                contenido.remove("pause")
                x=x+1
            except Exception as e:
                n=0
            try:
                contenido.remove("   PAUSE")
                x=x+1
            except Exception as e:
                n=0
            try:
                contenido.remove("   pause")
                x=x+1
            except Exception as e:
                n=0
            print(x)
        if x>0:
            loop(1)
        else:
            print("YA NO HAY MAS PAUSES",x)
    loop(1)
    f = open(archivo, "w")
    f.writelines("\n".join(contenido))
    f.close


changeBat('/mnt/c/ace3d/install.bat','MENU\n','AUTO.BAT', 0)
changeBat('/mnt/c/ace3d/1.bat','MENU\n','CLS\n9.BAT', 2)
changeBat('/mnt/c/ace3d/1.bat','menu\n','CLS\n9.BAT', 0)
changeBat('/mnt/c/ace3d/2.bat','   menu\n','   CLS\n   9.BAT', 2)
changeBat('/mnt/c/ace3d/2.bat','menu\n','CLS\n9.BAT', 2)

erasepauses("/mnt/c/ace3d/1.bat")
erasepauses("/mnt/c/ace3d/2.bat")
erasepauses("/mnt/c/ace3d/0.bat")
erasepauses("/mnt/c/ace3d/7.bat")
erasepauses("/mnt/c/ace3d/8.bat")
erasepauses("/mnt/c/ace3d/EAMRMCDZ.bat")
erasepauses("/mnt/c/ace3d/PPINSWIN.bat")
