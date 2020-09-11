import pygame
grid=[' ']*10
def printgrid():
    print("   |   |");
    print(" "+grid[1] + " | " + grid[2] + " | " + grid[3]);
    print("   |   |");
    print("-----------");
    print("   |   |");
    print(" " + grid[4] + " | " + grid[5] + " | " + grid[6]);
    print("   |   |");
    print("-----------");
    print("   |   |");
    print(" " + grid[7] + " | " + grid[8] + " | " + grid[9]);
    print("   |   |");
    print(" ");
def full():
    for i in range(1,10):
        if grid[i]==' ':
            return False
    return True
def winner(le,bo):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[7] == le and bo[4] == le and bo[1] == le) or (bo[8] == le and bo[5] == le and bo[2] == le) or (bo[9] == le and bo[6] == le and bo[3] == le) or (bo[7] == le and bo[5] == le and bo[3] == le) or(bo[9] == le and bo[5] == le and bo[1] == le))
def player():
    n=int(input())
    if grid[n]==' ':
        grid[n]='X'
    else:
        print('invalid')
        player()
    print("your move")
    printgrid()
def scorecount():
    if winner('X',grid):
        return -1
    elif winner('O',grid):
        return 1
    else:
        return 0
def possiblemoves():
    l=[]
    for i in range(1,10):
        if grid[i]==' ':
            l.append(i)
    return l
d=['O','X']
def minimax(depth,ismax):
    score=scorecount()
    if score==1:
        return score
    if score==-1:
        return score
    if full():
        return 0
    if ismax:
        best=-100
        pm=possiblemoves()
        for i in pm:
            grid[i]=d[0]
            best=max(best,minimax(depth+1,not ismax))
            grid[i]=' '
        return best
    else:
        best=100
        pm=possiblemoves()
        for i in pm:
            grid[i]=d[1]
            best=min(best,minimax(depth+1,not ismax))
            grid[i]=' '
        return best

def findbestmove():
    bestval=-100
    pm=possiblemoves()
    for i in pm:
        grid[i]=d[0]
        moveval=minimax(0,False)
        grid[i]=' '
        if moveval>bestval:
            place=i
            bestval=moveval
    return place
def game():
    while(not full() and not winner('X',grid) and not winner('O',grid)):
        move=findbestmove()
        grid[move]=d[0]
        print("computer move")
        printgrid()
        if winner('O',grid):
            print("you lost")
            break
        if full():
            print("Tie")
            break
        player()
        if winner('X',grid):
            print("you won")
            break
game()