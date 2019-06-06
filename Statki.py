from random import randint
#Ships placement
area = []

for field in range(10):
    area.append(["0"] * 10)

# ship check his placement!
def OneShip(area):
    for i in range(4):
        x =randint(0,9)
        y =randint(0,9)
        print('Pozycja statku 1: ',x,y)
        if area[x][y] == '1' or area[x][y] == '*':
            x = randint(0, 9)
            y = randint(0, 9)
            area[x][y] = '1'
        else:
            area[x][y] = '1'
'''
# That should be another def:
        if x > 0 and x < 9:
            if y == 0:
                area[x - 1][y] = '*'
                area[x - 1][y + 1] = '*'
                area[x][y + 1] = '*'
                area[x + 1][y] = '*'
                area[x + 1][y + 1] = '*'
            elif y == 9:
                area[x - 1][y - 1] = '*'
                area[x - 1][y] = '*'
                area[x][y - 1] = '*'
                area[x + 1][y - 1] = '*'
                area[x + 1][y] = '*'
            else:
                area[x-1][y-1] = '*'
                area[x-1][y] = '*'
                area[x-1][y+1] = '*'
                area[x][y-1] = '*'
                area[x][y+1] = '*'
                area[x+1][y-1] = '*'
                area[x+1][y] = '*'
                area[x+1][y+1] = '*'
        elif x == 9:
            if y == 9:
                area[x - 1][y - 1] = '*'
                area[x - 1][y] = '*'
                area[x][y-1] = '*'
            elif y == 0:
                area[x - 1][y] = '*'
                area[x - 1][y + 1] = '*'
                area[x][y+1] = '*'
            else:
                area[x - 1][y - 1] = '*'
                area[x - 1][y] = '*'
                area[x - 1][y + 1] = '*'
                area[x][y-1] = '*'
                area[x][y+1] = '*'
        elif x == 0:
            if y == 0:
                area[x][y+1] = '*'
                area[x+1][y] = '*'
                area[x+1][y+1] = '*'
            elif y == 9:
                area[x][y - 1] = '*'
                area[x + 1][y] = '*'
                area[x + 1][y - 1] = '*'
            else:
                area[x][y - 1] = '*'
                area[x][y + 1] = '*'
                area[x + 1][y - 1] = '*'
                area[x + 1][y] = '*'
                area[x + 1][y + 1] = '*'
'''
#Shield V2
'''
if x > 0 and x < 9:
            if y == 0:
                area[x - 1][y] = '*'
                area[x - 1][y + 1] = '*'
                area[x][y + 1] = '*'
                area[x + 1][y] = '*'
                area[x + 1][y + 1] = '*'
            elif y == 9:
                area[x - 1][y - 1] = '*'
                area[x - 1][y] = '*'
                area[x][y - 1] = '*'
                area[x + 1][y - 1] = '*'
                area[x + 1][y] = '*'
            else:
                area[x-1][y-1] = '*'
                area[x-1][y] = '*'
                area[x-1][y+1] = '*'
                area[x][y-1] = '*'
                area[x][y+1] = '*'
                area[x+1][y-1] = '*'
                area[x+1][y] = '*'
                area[x+1][y+1] = '*'
        elif x == 9:
            if y == 9:
                area[x - 1][y - 1] = '*'
                area[x - 1][y] = '*'
                area[x][y-1] = '*'
            elif y == 0:
                area[x - 1][y] = '*'
                area[x - 1][y + 1] = '*'
                area[x][y+1] = '*'
            else:
                area[x - 1][y - 1] = '*'
                area[x - 1][y] = '*'
                area[x - 1][y + 1] = '*'
                area[x][y-1] = '*'
                area[x][y+1] = '*'
        elif x == 0:
            if y == 0:
                area[x][y+1] = '*'
                area[x+1][y] = '*'
                area[x+1][y+1] = '*'
            elif y == 9:
                area[x][y - 1] = '*'
                area[x + 1][y] = '*'
                area[x + 1][y - 1] = '*'
            else:
                area[x][y - 1] = '*'
                area[x][y + 1] = '*'
                area[x + 1][y - 1] = '*'
                area[x + 1][y] = '*'
                area[x + 1][y + 1] = '*'
'''

def Shield(area):
    print("Shield Activited\n")
    for i in range(9):
        for j in range(9):
            if area[i][j] != '0':
                print('FIND SHIP CAPTAIN\n',i,j)
                if i == 0:
                    if j == 0:
                        area[i][j+1] = '*'
                        area[i+1][j] = '*'
                        area[i+1][j+1] = '*'
                    elif j == 9:
                        area[i][j-1] = '*'
                        area[i+1][j] = '*'
                        area[i+1][j-1] = '*'
                    else:
                        area[i][j-1] = '*'
                        area[i][j+1] = '*'
                        area[i+1][j-1] = '*'
                        area[i+1][j] = '*'
                        area[i+1][j+1] = '*'



            else:
                print('Nothing there Captain\n',i,j)


    print("Shield desactivited\n")


# Rest
def ocean(area):
    print("--------------------")
    for mila in area:
        print(" ".join(mila))
    print("--------------------")

#ocean(area)
OneShip(area)
Shield(area)
ocean(area)















