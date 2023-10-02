def build_grid(coords):
    grid = [["12|","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |"],
            ["11|","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |"],
            ["10|","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |"],
            ["9 |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |"],
            ["8 |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |"],
            ["7 |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |"],
            ["6 |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |"],
            ["5 |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |"],
            ["4 |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |"],
            ["3 |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |"],
            ["2 |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |"],
            ["1 |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |","  |"],
            ["  |","1 |","2 |","3 |","4 |","5 |","6 |","7 |","8 |","9 |","10|","11|","12|"],
    ]

    print(*grid,sep="\n")

    for i in range(0,len(coords),2):
        grid[coords[i]][coords[i+1]]="* |"

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
    loc = []
    x = int(data[0])
    y = int(data[1])
    coords.append(x)
    coords.append(y)
    print("start, x="+str(x)+". y="+str(y))
    for i in range(len(data)):
        if (0<x<13) and (0<y<13):
            if data[i] == "N":
                y+=1
                coords.append(x)
                coords.append(y)
                #print("Coords are "+str(x)+","+str(y)+" when i is "+str(i))
            if data[i] == "S":
                y-=1
                coords.append(x)
                coords.append(y)
                #print("Coords are "+str(x)+","+str(y)+" when i is "+str(i))
            if data[i] == "E":
                x+=1
                coords.append(x)
                coords.append(y)
                #print("Coords are "+str(x)+","+str(y)+" when i is "+str(i))
            if data[i] == "W":
                x-=1
                coords.append(x)
                coords.append(y)
                #print("Coords are "+str(x)+","+str(y)+" when i is "+str(i))
        else:
            print("Error in file")
            break
    build_grid(coords)

while True:
    Input()