from random import randint
# Make a board
area = []
for field in range(10):
    area.append(["0"] * 10)

# Ships placement
def OneShip(area):
    for i in range(4):
        x =randint(0,9)
        y =randint(0,9)
        print('Pozycja statku 1: ',x,y)
        if area[x][y] == '1' or area[x][y] == '*':
            x = randint(0, 9)
            y = randint(0, 9)
            if area[x][y] == '0':
                area[x][y] = '1'
        else:
            if area[x][y] == '0':
                area[x][y] = '1'

'''
# That make shield around ships AND THAT's WORK!
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
# Shield END
'''
def TwoShip(area):
    orient = randint(0,1)
    x = randint(0,9)
    y = randint(0,9)
    print ('Pozycja statku 2: Pole 1:',x,y,'- Pole 2:',x,y+1)
    if area[x][y] == '0':
        #if area[x][y+1] != '0' or area[x-1][y] !='0':
        #    TwoShip(area)
        #else:
            if orient == 0:
                if y == 9:
                    try:
                        area[x][y] = '2'
                        if area[x][y-1] == '0':
                            area[x][y-1] = '2'
                        else:
                            area[x][y+1] = '2'
                    except:
                        area[x][y] = '2'
                        area[x-1][y] = '2'
                else:
                    area[x][y] = '2'
                    if area[x][y+1] == '0':
                        area[x][y+1] = '2'
                    else:
                        area[x][y - 1] = '2'
            elif orient == 1:
                if x == 9:
                    try:
                        area[x][y] = '2'
                        if area[x-1][y] == '0':
                            area[x-1][y] = '2'
                        else:
                            TwoShip(area)
                    except:
                        if y <9:
                            area[x][y] = '2'
                            area[x][y+1] = '2'
                elif x == 0:
                    area[x][y] = '2'
                    if area[x+1][y] == '0':
                        area[x+1][y] = '2'
                    else:
                        TwoShip(area)
                else:
                    area[x][y] = '2'
                    if area[x-1][y] == '0':
                        area[x-1][y] = '2'
                    elif area [x+1][y] == '0':
                        area[x+1][y] == '2'
                    else:
                        TwoShip(area)
    else:
        print('Powino się powtórzyć rozstawienie')
        TwoShip(area)

def ThreeShip(area):
    orient3 = randint(0, 1)
    x = randint(0, 9)
    y = randint(0, 9)
    print('Pozycja statku 3: Pole start: ',x,y)
    if orient3 == 0 and x == 9:
        try:
            area[x][y] = '3'
            area[x + 1][y] = '3'
            area[x + 2][y] = '3'
        except:
            area[x][y] = '3'
            area[x][y + 1] = '3'
            area[x][y + 2] = '3'
    elif orient3 == 0 and y == 9:
        area[x][y] = '3'
        area[x][y-1] = '3'
        area[x][y-2] = '3'

    # if area[x][y] == '1' or area[x][y] == '*':

    else:
        area[x][y] = '3'
        area[x - 1][y] = '3'
        area[x-2][y] = '3'

def FourShip(area):
    orient4 = randint(0,1)
    x = randint(0, 9)
    y = randint(0, 9)
    print('Pozycja statku 4: Pole start: ', x, y)
    if area[x][y] == '0':
        if orient4 == 0:
            if y == 9:
                try:
                    area[x][y] = '4'
                    if area[x][y - 3] == '0':
                        area[x][y - 1] = '4'
                        area[x][y - 2] = '4'
                        area[x][y - 3] = '4'
                    else:
                        if x < 7:
                            if area[x + 3][y] == '0':
                                area[x + 1][y] = '4'
                                area[x + 2][y] = '4'
                                area[x + 3][y] = '4'
                            else:
                                if x > 2:
                                    if area[x - 3][y] == '0':
                                        area[x - 1][y] = '4'
                                        area[x - 2][y] = '4'
                                        area[x - 3][y] = '4'
                                    else:
                                        FourShip(area)
                        else:
                            FourShip(area)
                except:
                    FourShip(area)
            elif y == 0:
                try:
                    area[x][y] = '4'
                    if area[x][y + 3] == '0':
                        area[x][y + 1] = '4'
                        area[x][y + 2] = '4'
                        area[x][y + 3] = '4'
                    else:
                        if x < 7:
                            if area[x + 3][y] == '0':
                                area[x + 1][y] = '4'
                                area[x + 2][y] = '4'
                                area[x + 3][y] = '4'
                            else:
                                if x > 2:
                                    if area[x - 3][y] == '0':
                                        area[x - 1][y] = '4'
                                        area[x - 2][y] = '4'
                                        area[x - 3][y] = '4'
                                    else:
                                        FourShip(area)
                        else:
                            FourShip(area)
                except:
                    FourShip(area)
            else:
                if y > 2 and y < 7:
                    if area[x][y + 3] == '0':
                        area[x][y] = '4'
                        area[x][y + 1] = '4'
                        area[x][y + 2] = '4'
                        area[x][y + 3] = '4'
                    else:
                        if area[x][y - 3] == '0':
                            area[x][y] = '4'
                            area[x][y - 1] = '4'
                            area[x][y - 2] = '4'
                            area[x][y - 3] = '4'
                else:
                    if x > 2 and x < 7:
                        try:
                            if area[x + 3][y] == '0':
                                area[x][y] = '4'
                                area[x + 1][y] = '4'
                                area[x + 2][y] = '4'
                                area[x + 3][y] = '4'
                            else:
                                if area[x - 3][y] == '0':
                                    area[x][y] = '4'
                                    area[x - 1][y] = '4'
                                    area[x - 2][y] = '4'
                                    area[x - 3][y] = '4'
                                else:
                                    FourShip(area)
                        except:
                            FourShip(area)
                    else:
                        FourShip(area)
        elif orient4 == 1:
            if x == 0:
                try:
                    if area[x + 3][y] == '0':
                        area[x][y] = '4'
                        area[x + 1][y] = '4'
                        area[x + 2][y] = '4'
                        area[x + 3][y] = '4'
                    else:
                        if y < 7:
                            if area[x][y + 3] == '0':
                                area[x][y] = '4'
                                area[x][y + 1] = '4'
                                area[x][y + 2] = '4'
                                area[x][y + 3] = '4'
                            else:
                                FourShip(area)
                        elif y > 6 and y < 10:
                            if area[x - 3][y] == '0':
                                area[x][y] = '0'
                                area[x - 1][y] = '0'
                                area[x - 2][y] = '0'
                                area[x - 3][y] = '0'
                            else:
                                FourShip(area)
                        else:
                            FourShip(area)
                except:
                    FourShip(area)
            elif x == 9:
                try:
                    if area[x - 3][y] == '0':
                        area[x][y] = '4'
                        area[x - 1][y] = '4'
                        area[x - 2][y] = '4'
                        area[x - 3][y] = '4'
                    else:
                        if y < 7:
                            if area[x][y + 3] == '0':
                                area[x][y] = '4'
                                area[x][y + 1] = '4'
                                area[x][y + 2] = '4'
                                area[x][y + 3] = '4'
                            else:
                                FourShip(area)
                        elif y > 6 and y < 10:
                            try:
                                if area[x - 3][y] == '0':
                                    area[x][y] = '4'
                                    area[x - 1][y] = '4'
                                    area[x - 2][y] = '4'
                                    area[x - 3][y] = '4'
                                else:
                                    FourShip(area)
                            except:
                                FourShip(area)
                except:
                    FourShip(area)
            else:
                if x > 2 and x < 7:
                    if area[x + 3][y] == '0':
                        area[x][y] = '4'
                        area[x + 1][y] = '4'
                        area[x + 2][y] = '4'
                        area[x + 3][y] = '4'
                    else:
                        if y > 2 and y < 7:
                            try:
                                if area[x - 3][y] == '0':
                                    area[x][y] = '4'
                                    area[x - 1][y] = '4'
                                    area[x - 2][y] = '4'
                                    area[x - 3][y] = '4'
                                elif area[x][y + 3] == '0':
                                    area[x][y] = '4'
                                    area[x][y + 1] = '4'
                                    area[x][y + 2] = '4'
                                    area[x][y + 3] = '4'
                                elif area[x][y - 3] == '0':
                                    area[x][y] = '4'
                                    area[x][y - 1] = '4'
                                    area[x][y - 2] = '4'
                                    area[x][y - 3] = '4'
                                else:
                                    FourShip(area)
                            except:
                                FourShip(area)
                        else:
                            try:
                                if area[x - 3][y] == '0':
                                    area[x][y] = '4'
                                    area[x - 1][y] = '4'
                                    area[x - 2][y] = '4'
                                    area[x - 3][y] = '4'
                            except:
                                FourShip(area)



# Rest
def ocean(area):
    print("--------------------")
    for mila in area:
        print(" ".join(mila))
    print("--------------------")

FourShip(area)
#ThreeShip(area)
TwoShip(area)
OneShip(area)
ocean(area)















