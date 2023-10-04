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
    #need to loop through building grid and improve look?

    for i in range(0,len(coords),2):
        if coords[i]==12:
            coords[i]-=12
        elif coords[i]==11:
            coords[i]-=10
        elif coords[i]==10:
            coords[i]-=8
        elif coords[i]==9:
            coords[i]-=6
        elif coords[i]==8:
            coords[i]-=4
        elif coords[i]==7:
            coords[i]-=2
        elif coords[i]==6:
            coords[i]-=0
        elif coords[i]==5:
            coords[i]+=2
        elif coords[i]==4:
            coords[i]+=4
        elif coords[i]==3:
            coords[i]+=6
        elif coords[i]==2:
            coords[i]+=8
        elif coords[i]==1:
            coords[i]+=10

    for i in range(0,len(coords)-1,2):
        grid[coords[i]][coords[i+1]] = "* |"
    print(*grid,sep="\n")
    print("Coordinates")
    for i in range(0,len(coords)-1):
        print(f"({coords[i+1]},{coords[i]+12})")
    #Need to fix coords variable


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
    print("start, x="+str(x)+". y="+str(y))
    for i in range(len(data)):
        if (0<x<13) and (0<y<13):
            if data[i] == "N":
                y+=1
                coords.append(y)
                coords.append(x)
                #print("Coords are "+str(x)+","+str(y)+" when i is "+str(i))
            if data[i] == "S":
                y-=1
                coords.append(y)
                coords.append(x)
                #print("Coords are "+str(x)+","+str(y)+" when i is "+str(i))
            if data[i] == "E":
                x+=1
                coords.append(y)
                coords.append(x)
                #print("Coords are "+str(x)+","+str(y)+" when i is "+str(i))
            if data[i] == "W":
                x-=1
                coords.append(y)
                coords.append(x)
                #print("Coords are "+str(x)+","+str(y)+" when i is "+str(i))
        else:
            print("Error in file")
            Input()
    build_grid(coords)

while True:
    Input()