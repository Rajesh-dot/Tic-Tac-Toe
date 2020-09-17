import pygame
from pygame.locals import *
import time

CLOCK = pygame.time.Clock()

pygame.init()
pygame.display.set_caption("Tic-Tac-Toe")
run=True
width=400
height=400
WHITE = (255, 255, 255)
line_color = (64, 224, 208)
win=pygame.display.set_mode((width,height+100),0,32)


grid=[' ']*10



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


    
    

def draw_grid():
    win.fill(WHITE)
    pygame.draw.line(win, line_color, (width / 3, 0), (width / 3, height), 7) 
    pygame.draw.line(win, line_color, (width / 3 * 2, 0), (width / 3 * 2, height), 7) 
    pygame.draw.line(win, line_color, (0, height / 3), (width, height / 3), 7) 
    pygame.draw.line(win, line_color, (0, height / 3 * 2), (width, height / 3 * 2), 7) 
    draw_status('Welcome') 
    pygame.display.update()


#draw_grid()



x_img=pygame.image.load('x.png')
o_img=pygame.image.load('o.png')
x_img = pygame.transform.scale(x_img, (80, 80)) 
o_img = pygame.transform.scale(o_img, (80, 80))



#XO='x'
def drawXO(row, col,XO):
    #global XO 
    if row == 1: 
        posx = 30    
    if row == 2: 
        posx = width / 3 + 30
    if row == 3: 
        posx = width / 3 * 2 + 30
    if col == 1: 
        posy = 30
    if col == 2: 
        posy = height / 3 + 30
    if col == 3: 
        posy = height / 3 * 2 + 30 
    #board[row-1][col-1] = XO 
    if(XO == 'X'): 
        win.blit(x_img, (posy, posx)) 
        XO = 'O'
    else: 
        win.blit(o_img, (posy, posx)) 
        XO = 'X'
    pygame.display.update() 



#drawXO(1,2,'x')


def draw_status(message):
    
    if winner('X',grid): 
        message = "Hurray You Won!"
    if winner('O',grid): 
        message = "You Lost!"
    if full(): 
        message = "Game Draw !"

    font = pygame.font.Font(None, 30) 

    text = font.render(message, 1, (255, 255, 255)) 

    win.fill ((0, 0, 0), (0, 400, 500, 100)) 
    text_rect = text.get_rect(center =(width / 2, 500-50)) 
    win.blit(text, text_rect) 
    pygame.display.update() 





def user_click(): 
    x, y = pygame.mouse.get_pos() 
    if(x<width / 3): 
        col = 1
    elif (x<width / 3 * 2): 
        col = 2
    elif(x<width): 
        col = 3
    else: 
        col = None
    if(y<height / 3): 
        row = 1
    elif (y<height / 3 * 2): 
        row = 2
    elif(y<height): 
        row = 3
    else: 
        row = None
    if(row and col is not None): #and grid[(row-1)*3+col]==' '
        if grid[(row-1)*3+col]==' ':
            drawXO(row, col,'X')
            return row,col
        else:
            return 0,0
    else:
        return -1,-1
    #check_win() 

    
def reset_game():
    global grid
    time.sleep(1)
    grid=[' ']*10
    draw_grid()
    draw_status("Restarted")
    

draw_grid()

move_dic={1:(1,1),2:(1,2),3:(1,3),4:(2,1),5:(2,2),6:(2,3),7:(3,1),8:(3,2),9:(3,3)}

while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if full():
            draw_status("Kareddy")
            reset_game()
            #print("tie")
        elif winner('X',grid):
            draw_status("You Won!")
            reset_game()
        elif winner('O',grid):
            draw_status("You lost")
            reset_game()
            #print(grid)
        else:
            if event.type is MOUSEBUTTONDOWN:
                x,y=user_click()
                if x!=0 and x!=-1:
                    draw_status("Kareddy")
                    pos=(x-1)*3+y
                    grid[pos]='X'
                    draw_status("Kareddy")
                    if not full():
                        move=findbestmove()
                        grid[move]='O'
                        #print(move)
                        row,col=move_dic[move]
                        draw_status("Kareddy")
                        drawXO(row, col,'O')
                elif x==0:
                    draw_status("Already Selected")
            
pygame.quit()