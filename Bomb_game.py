import random
import keyboard
import time

def bombgenetartor():
    matrix = [[0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0]]
    i = 0
    bombs = []
    while i < 10:
        a = random.randint(0,9)
        b = random.randint(0, 9)
        pair = [a, b]
        if pair in bombs:
            pass
        elif pair == [9, 0]:
            pass
        else:
            bombs.append(pair)
            i += 1

    for i in bombs:
        a = i[0]
        b = i[1]
        matrix[a][b] = 1

    return bombs

def matrixDrawer(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end="  ")
        print()

def playSpaceGenerator():
    bl = "⏹"
    sm = "☺"
    playSpace = [[bl, bl, bl, bl, bl, bl, bl, bl, bl, bl],
                 [bl, bl, bl, bl, bl, bl, bl, bl, bl, bl],
                 [bl, bl, bl, bl, bl, bl, bl, bl, bl, bl],
                 [bl, bl, bl, bl, bl, bl, bl, bl, bl, bl],
                 [bl, bl, bl, bl, bl, bl, bl, bl, bl, bl],
                 [bl, bl, bl, bl, bl, bl, bl, bl, bl, bl],
                 [bl, bl, bl, bl, bl, bl, bl, bl, bl, bl],
                 [bl, bl, bl, bl, bl, bl, bl, bl, bl, bl],
                 [bl, bl, bl, bl, bl, bl, bl, bl, bl, bl],
                 [sm, bl, bl, bl, bl, bl, bl, bl, bl, bl]]

    return playSpace

def checker(x, y):
    if x >= 0 and x <= 9 and y >= 0 and y <= 9:
        return True
    else:
        return False

def playSpaceUpdater(cortable, bombslist):
    matrix = playSpaceGenerator()
    basecor = [9, 0]
    bombstat = False


    for newcor in cortable:
        matrix[basecor[0]][basecor[1]] = "◻"
        matrix[newcor[0]][newcor[1]] = "☺"
        basecor = newcor


    for bomb in bombslist:
        if bomb == cortable[-1]:
            matrix[cortable[-1][0]][cortable[-1][1]] = "⎈"
            bombstat = True

    return matrix, bombstat

def stepCounter(cortable):
    stepscord = []
    for cord in cortable:
        if cord in stepscord:
            pass
        else:
            stepscord.append(cord)

    return len(stepscord)-1



playspace = playSpaceGenerator()
bombslist = bombgenetartor()

matrixDrawer(playspace)

cor = [9, 0]
cortable = []

while True:
    while True:
        key = keyboard.read_event(suppress=True).name

        time.sleep(0.2)

        if key == "up":
            x = cor[0] - 1
            y = cor[1]
            if checker(x, y) == True:
                break
            else:
                print("Nem léphet ki a pálya szélén!")
                continue
        elif key == "left":
            x = cor[0]
            y = cor[1] - 1
            if checker(x, y) == True:
                break
            else:
                print("Nem léphet ki a pálya szélén!")
                continue
        elif key == "down":
            x = cor[0] + 1
            y = cor[1]
            if checker(x, y) == True:
                break
            else:
                print("Nem léphet ki a pálya szélén!")
                continue
        elif key == "right":
            x = cor[0]
            y = cor[1] + 1
            if checker(x, y) == True:
                break
            else:
                print("Nem léphet ki a pálya szélén!")
                continue
        else:
            continue

    cor = [x, y]
    cortable.append(cor)
    playspace, bomb = playSpaceUpdater(cortable, bombslist)
    print(" ")
    matrixDrawer(playspace)

    if bomb == True:
        time.sleep(2)
        print("Vége a játéknak")
        print("Bombára léptél!")
        print(f"Elért pontszám: {stepCounter(cortable)}")
        break
    else:
        continue