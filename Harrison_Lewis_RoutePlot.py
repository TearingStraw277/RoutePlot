def build_grid(coords):
    grid = [["12|","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |"],#0
            ["__|","__|","__|","__|","__|","__|","__|","__|","__|","__|","__|","__|","__|"],#1
            ["11|","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |"],#2
            ["__|","__|","__|","__|","__|","__|","__|","__|","__|","__|","__|","__|","__|"],#3
            ["10|","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |"],#4
            ["__|","__|","__|","__|","__|","__|","__|","__|","__|","__|","__|","__|","__|"],#5
            ["9 |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |"],#6
            ["__|","__|","__|","__|","__|","__|","__|","__|","__|","__|","__|","__|","__|"],#7
            ["8 |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |"],#8
            ["__|","__|","__|","__|","__|","__|","__|","__|","__|","__|","__|","__|","__|"],#9
            ["7 |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |"],#10
            ["__|","__|","__|","__|","__|","__|","__|","__|","__|","__|","__|","__|","__|"],#11
            ["6 |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |"],#12
            ["__|","__|","__|","__|","__|","__|","__|","__|","__|","__|","__|","__|","__|"],#13
            ["5 |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |"],#14
            ["__|","__|","__|","__|","__|","__|","__|","__|","__|","__|","__|","__|","__|"],#15
            ["4 |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |"],#16
            ["__|","__|","__|","__|","__|","__|","__|","__|","__|","__|","__|","__|","__|"],#17
            ["3 |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |"],#18
            ["__|","__|","__|","__|","__|","__|","__|","__|","__|","__|","__|","__|","__|"],#19
            ["2 |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |"],#20
            ["__|","__|","__|","__|","__|","__|","__|","__|","__|","__|","__|","__|","__|"],#21
            ["1 |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |"],#22
            ["__|","__|","__|","__|","__|","__|","__|","__|","__|","__|","__|","__|","__|"],#23
            ["  |","1 |","2 |","3 |","4 |","5 |","6 |","7 |","8 |","9 |","10|","11|","12|"]#24
    ]
    #need to loop through building grid

    coords_copy = coords.copy()
    for i in range(0,len(coords_copy),2):
        if coords_copy[i]==12:
            coords_copy[i]=0
        elif coords_copy[i]==11:
            coords_copy[i]=2
        elif  coords_copy[i]==10:
            coords_copy[i]=4
        elif coords_copy[i]==9:
            coords_copy[i]=6
        elif coords_copy[i]==7:
            coords_copy[i]=10
        elif coords_copy[i]==6:
            coords_copy[i]=12
        elif coords_copy[i]==5:
            coords_copy[i]=14
        elif coords_copy[i]==4:
            coords_copy[i]=16
        elif coords_copy[i]==3:
            coords_copy[i]=18
        elif coords_copy[i]==2:
            coords_copy[i]=20
        elif coords_copy[i]==1:
            coords_copy[i]=22

    for i in range(0,len(coords_copy)-1,2):
        grid[coords_copy[i]][coords_copy[i+1]] = "* |"

    for row in grid:
        print(*row)

    print("Coordinates")
    for i in range(0,len(coords)-1):
        print(f"({coords[i+1]},{coords[i]})")

def get_data(file):
    with open('Route00'+file+'.txt','rt') as lines:
        data = []
        for line in lines:
            line = line.strip()
            data.append(line)
    path(data)

def Input():
    User_Input=str(input("Enter which route you wish to use or STOP to end program: "))
    if User_Input.upper() == "STOP":
        print("The program will now end.")
        exit()
    elif User_Input == "1" or User_Input == "2" or User_Input == "3":
        get_data(User_Input)
    else:
        print("Please enter a 1, 2 or 3 to choose a route or type STOP to end program")

def path(data):
    coords = []
    x = int(data[0])
    y = int(data[1])
    coords.append(y)
    coords.append(x)
    for i in range(len(data)):
        if (0<x<13) and (0<y<13):
            if data[i] == "N":
                y+=1
                coords.append(y)
                coords.append(x)
            if data[i] == "S":
                y-=1
                coords.append(y)
                coords.append(x)
            if data[i] == "E":
                x+=1
                coords.append(y)
                coords.append(x)
            if data[i] == "W":
                x-=1
                coords.append(y)
                coords.append(x)
        else:
            print("Error in file")
            Input()
    build_grid(coords)

while True:
    Input()