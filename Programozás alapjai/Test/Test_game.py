import random

def random10x10MatrixGenerator():
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
        pair = (a, b)
        if pair in bombs:
            pass
        elif pair == (9, 0):
            pass
        else:
            bombs.append(pair)
            i += 1

    for i in bombs:
        a = i[0]
        b = i[1]
        matrix[a][b] = 1

    return matrix

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

def playSpaceUpdater(cortable):
    matrix = playSpaceGenerator()
    basecor = [9, 0]
    for newcor in cortable:
        matrix[basecor[0]][basecor[1]] = "◻"
        matrix[newcor[0]][newcor[1]] = "☺"
        basecor = newcor
    return matrix



playspace = playSpaceGenerator()
matrix = random10x10MatrixGenerator()

matrixDrawer(playspace)
#matrixDrawer(matrix)

cor = [9, 0]
cortable = []

while True:
    while True:
        move = input("Move: ")
        if move == "w":
            x = cor[0] - 1
            y = cor[1]
            if checker(x, y) == True:
                break
            else:
                print("Nem léphet ki a pálya szélén!")
                continue
        elif move == "a":
            x = cor[0]
            y = cor[1] - 1
            if checker(x, y) == True:
                break
            else:
                print("Nem léphet ki a pálya szélén!")
                continue
        elif move == "s":
            x = cor[0] + 1
            y = cor[1]
            if checker(x, y) == True:
                break
            else:
                print("Nem léphet ki a pálya szélén!")
                continue
        elif move == "d":
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
    matrixDrawer(playSpaceUpdater(cortable))


