def build_grid():
    grid = [["  " for i in range(13)] for j in range(13)]
    for i in range(12,0,-1):
        grid[i-1][0]=str(i)
    for i in range(0,12):
        grid[12][i] = str(i-1)

    print(grid,sep="\n")


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
    x = int(data[0])
    y = int(data[1])
    print("start, x="+str(x)+". y="+str(y))
    for i in range(len(data)):
        if (0<x<13) and (0<y<13):
            if data[i] == "N":
                y +=1
                print("Coords are "+str(x)+","+str(y)+" when i is "+str(i))
            if data[i] == "S":
                y -=1
                print("Coords are "+str(x)+","+str(y)+" when i is "+str(i))
            if data[i] == "E":
                x +=1
                print("Coords are "+str(x)+","+str(y)+" when i is "+str(i))
            if data[i] == "W":
                x -=1
                print("Coords are "+str(x)+","+str(y)+" when i is "+str(i))
        else:
            print("Error in file")
            break

build_grid()

#while True:
    #Input()