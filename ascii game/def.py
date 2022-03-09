def move():
    mv = input("What side of light do you want to go? (north, east, south, west)")
    if mv == "north":
        return (0,-1)
    elif mv == "east":
        return (+1,0)
    elif mv == "south":
        return (0,+1)
    elif mv == "west":
        return (-1,0)
    else: print("Wrong Command")
    
def wallbang(xb,yb,xc,yc):
    if xc == 1 or yc == 1 or xc == xb or yc == yb:
        print("You have hit the wall")   
        return(False)
    else:
        return(True)

def render(xchar, ychar):
    os.system('cls' if os.name == 'nt' else 'clear')
    for y in range(1,8):
        for x in range(1,16):
            if y == ychar and x == xchar:
                print("웃", end="")
            elif y == 1 or y == 7:
                print("$", end ="")
            elif x == 1 or x == 15:
                print("$", end ="")
            else: print(" ", end="")
        print('') 
