import pygame

pygame.init()


clock = pygame.time.Clock()
white = (255,255,255)
light_yellow = (255,255,0)
light_red = (255,0,0)
light_green = (0,255,0)
yellow = (200,200,0)
black = (0,0,0)
red = (155,0,0)
green = (0,155,0)
blue = (0,0,255)
boardheight = 800
boardwidth = 800
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

#.....................loading images.....................
BP = pygame.image.load('BP.png')
BK = pygame.image.load('BK.png')
BQ = pygame.image.load('BQ.png')
BB = pygame.image.load('BB.png')
BN = pygame.image.load('BN.png')
BR = pygame.image.load('BR.png')
    
WP = pygame.image.load('WP.png')
WR = pygame.image.load('WR.png')
WK = pygame.image.load('WK.png')
WQ = pygame.image.load('WQ.png')
WN = pygame.image.load('WN.png')
WB = pygame.image.load('WB.png')

imgdict = {
        "bk" : BK,
        "bpb" : BP,
        "bq" : BQ,
        "bb" : BB,
        "bn" : BN,
        "br" : BR,
        "wk" : WK,
        "wpw" : WP,
        "wq" : WQ,
        "wb" : WB,
        "wn" : WN,
        "wr" : WR,
    }

#.....................assigning positions & nature.................
posdict = {
    "pos_BK" : [400,700,"b","k"],
    "pos_BQ" : [300,700,"b","q"],
    "pos_BP_1" : [0,600,"b","pb"],
    "pos_BP_2" : [100,600,"b","pb"],
    "pos_BP_3" : [200,600,"b","pb"],
    "pos_BP_4" : [300,600,"b","pb"],
    "pos_BP_5" : [400,600,"b","pb"],
    "pos_BP_6" : [500,600,"b","pb"],
    "pos_BP_7" : [600,600,"b","pb"],
    "pos_BP_8" : [700,600,"b","pb"],
    "pos_BB_1" : [200,700,"b","b"],
    "pos_BB_2" : [500,700,"b","b"],
    "pos_BN_1" : [100,700,"b","n"],
    "pos_BN_2" : [600,700,"b","n"],
    "pos_BR_1" : [0,700,"b","r"],
    "pos_BR_2" : [700,700,"b","r"],
    "pos_WK" : [400,0,"w","k"],
    "pos_WQ" : [300,0,"w","q"],
    "pos_WP_1" : [0,100,"w","pw"],
    "pos_WP_2" : [100,100,"w","pw"],
    "pos_WP_3" : [200,100,"w","pw"],
    "pos_WP_4" : [300,100,"w","pw"],
    "pos_WP_5" : [400,100,"w","pw"],
    "pos_WP_6" : [500,100,"w","pw"],
    "pos_WP_7" : [600,100,"w","pw"],
    "pos_WP_8" : [700,100,"w","pw"],
    "pos_WB_1" : [200,0,"w","b"],
    "pos_WB_2" : [500,0,"w","b"],
    "pos_WN_1" : [100,0,"w","n"],
    "pos_WN_2" : [600,0,"w","n"],
    "pos_WR_1" : [0,0,"w","r"],
    "pos_WR_2" : [700,0,"w","r"],
}



gameDisplay = pygame.display.set_mode((boardwidth,boardheight))
gameDisplay.fill(white)



def board():
    for x in range(0,800,200):
        for y in range(0,800,200):
            pygame.draw.rect(gameDisplay, blue, (x,y,100,100))

    for x in range(100,800,200):
        for y in range(100,800,200):
            pygame.draw.rect(gameDisplay, blue, (x,y,100,100))

    for x in range(0,800,200):
        for y in range(100,800,200):
            pygame.draw.rect(gameDisplay, white, (x,y,100,100))

    for x in range(100,800,200):
        for y in range(0,800,200):
            pygame.draw.rect(gameDisplay, white, (x,y,100,100))

##.....................................................selecting a piece..........................................
value_list = [".",".",".","."]
input_list = []
def selected_tile(x,y):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global team_selected, team,input_list,value_list

    
    if x + 100> cur[0] > x and y + 100 > cur[1] > y:
        if click[0] == 1 and len(input_list) == 0:
            for value in posdict:
                if x == posdict[value][0] and y == posdict[value][1]:
                    team = posdict[value][2]
                    name = posdict[value][3]
                    pygame.draw.rect(gameDisplay, red,(x,y,100,100))
                    if len(input_list) < 2:
                        input_list.append(x)
                        input_list.append(y)
                        input_list.append(team)
                        input_list.append(name)
                        print(x,y,team,name)   #for showing which coordinates you have selected for your piece to be
                        value_list = input_list.copy()
##                        input_list.clear()
        
        if click[0] == 1 and len(input_list) == 0:  
            pygame.draw.rect(gameDisplay, red,(x,y,100,100))
            team = "."
            name = "."
            if len(input_list) < 2:
                input_list.append(x)
                input_list.append(y)
                input_list.append(team)
                input_list.append(name)
                print(x,y,team,name)   #for showing which coordinates you have selected for your piece to be
                value_list = input_list.copy()

        input_list.clear()
    return value_list[0],value_list[1],value_list[2],value_list[3]
            
            
##........................................................................................knight.......................................................................

def knight(x,y):
    available_tiles = [[x+100,y-200],
                       [x-100,y-200],
                       [x+100,y+200],
                       [x-100,y+200],
                       [x-200,y-100],
                       [x-200,y+100],
                       [x+200,y-100],
                       [x+200,y+100]]
    
    for value in posdict:
        if x == posdict[value][0] and y == posdict[value][1]:
            teamm = posdict[value][2]


    for value in posdict:
        for i in available_tiles:
            if i[0] == posdict[value][0] and i[1] == posdict[value][1] and teamm == posdict[value][2]:
                print("yay")
                available_tiles.remove([i[0],i[1]])

    return available_tiles

def selection(tiles):
    val = []
    inp = []
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    for i in tiles:
        pygame.draw.rect(gameDisplay, red,(i[0],i[1],100,100),10)
        if i[0] + 100> cur[0] > i[0] and i[1] + 100 > cur[1] > i[1] and click[2] == 1:
            print(i[0],i[1])
            val.append(i[0])
            val.append(i[1])
            if len(val) > 1:
                inp = val.copy()
            val.clear()
    return inp


def pawnb(x,y):
    val = []
    inp = []
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    available_tiles = [[x,y-100]]
    if y == 600:
        available_tiles.append([x,y-200])
        for value in posdict:
            if x == posdict[value][0] and y-100 == posdict[value][1]:
                available_tiles.remove([x,y-200])
    for value in posdict:
        if x+100 == posdict[value][0] and y-100 == posdict[value][1] and posdict[value][2]!="b":
            available_tiles.append([x+100,y-100])
    for value in posdict:
        if x-100 == posdict[value][0] and y-100 == posdict[value][1] and posdict[value][2]!="b":
            available_tiles.append([x-100,y-100])
    for value in posdict:
        if x == posdict[value][0] and y-100 == posdict[value][1]:
            available_tiles.remove([x,y-100])

    for value in posdict:
        if x == posdict[value][0] and y == posdict[value][1]:
            teamm = posdict[value][2]


    for value in posdict:
        for i in available_tiles:
            if i[0] == posdict[value][0] and i[1] == posdict[value][1] and teamm == posdict[value][2]:
                print("yay")
                available_tiles.remove([i[0],i[1]])
        
    return available_tiles

def pawnw(x,y):
    val = []
    inp = []
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    available_tiles = [[x,y+100]]
    if y == 100:
        available_tiles.append([x,y+200])
        for value in posdict:
            if x == posdict[value][0] and y+100 == posdict[value][1]:
                available_tiles.remove([x,y+200])
    for value in posdict:
        if x+100 == posdict[value][0] and y+100 == posdict[value][1] and posdict[value][2]!="w":
            available_tiles.append([x+100,y+100])
    for value in posdict:
        if x-100 == posdict[value][0] and y+100 == posdict[value][1] and posdict[value][2]!="w":
            available_tiles.append([x-100,y+100])
    for value in posdict:
        if x == posdict[value][0] and y+100 == posdict[value][1]:
            available_tiles.remove([x,y+100])

    for value in posdict:
        if x == posdict[value][0] and y == posdict[value][1]:
            teamm = posdict[value][2]


    for value in posdict:
        for i in available_tiles:
            if i[0] == posdict[value][0] and i[1] == posdict[value][1] and teamm == posdict[value][2]:
                print("yay")
                available_tiles.remove([i[0],i[1]])

    return available_tiles


def queen(x,y):
    get = []
    get1 = []
    least_tr = 800
    least_tl = 800
    least_br = 800
    least_bl = 800
    least_right = 800
    least_left = 800
    least_up = 800
    least_down = 800
    available_tiles = []

    #.............................for main Diagonal.........................
    for i in range(-700,800,100):
        for value in posdict:
            if x-i == posdict[value][0] and y-i == posdict[value][1]:
                get.append([x-i,y-i])

    for i in get:
        if i[0]<x and i[1]<y and abs(i[0]-x) < least_tl:
            least_tl =  abs(i[0]-x)
    for i in get:
        if i[0]>x and i[1]>y and abs(i[0]-x) < least_br:
            least_br =  abs(i[0]-x)
            
    for m in range(-least_tl,least_br+100,100):   
        available_tiles.append([x+m,y+m]) 


                
    #.............................for other diagonal.........................
    for i in range(-700,800,100):
        for value in posdict:
            if x+i == posdict[value][0] and y-i == posdict[value][1]:
                get.append([x+i,y-i])
                
    for i in get:
        if i[0]<x and i[1]>y and abs(i[0]-x) < least_bl:
            least_bl =  abs(i[0]-x)
    for i in get:
        if i[0]>x and i[1]<y and abs(i[0]-x) < least_tr:
            least_tr =  abs(i[0]-x)
            
    for m in range(-least_bl,least_tr+100,100):   
        available_tiles.append([x+m,y-m])

    #.........................for vertical positions.............
    for j in range (0,800,100):
        for value in posdict:
            if x == posdict[value][0] and j == posdict[value][1]:
                get1.append([x,j])

    for i in get1:
        if i[1]>y and abs(i[1]-y) < least_down:
            least_down = abs(i[1]-y)
    for i in get1:
        if i[1]<y and abs(i[1]-y) < least_up:
            least_up = abs(i[1]-y)

    for m in range(y-least_up,y+least_down+100,100):
        available_tiles.append([x,m])

    #........................for horizontal positions.............
    for i in range (0,800,100):
        for value in posdict:
            if i == posdict[value][0] and y == posdict[value][1]:
                get1.append([i,y])

    for i in get1:
        if i[0]>x and abs(i[0]-x) < least_right:
            least_right = abs(i[0]-x)
    for i in get1:
        if i[0]<x and abs(i[0]-x) < least_left:
            least_left = abs(i[0]-x)

    for m in range(x-least_left,x+least_right+100,100):
        available_tiles.append([m,y]) 
    available_tiles.remove([x,y])
    available_tiles.remove([x,y])
    available_tiles.remove([x,y])
    available_tiles.remove([x,y])


    for value in posdict:
        if x == posdict[value][0] and y == posdict[value][1]:
            teamm = posdict[value][2]


    for value in posdict:
        for i in available_tiles:
            if i[0] == posdict[value][0] and i[1] == posdict[value][1] and teamm == posdict[value][2]:
                print("yay")
                available_tiles.remove([i[0],i[1]])

    return available_tiles


    
def rook(x,y):
    get = []
    least_right = 800
    least_left = 800
    least_up = 800
    least_down = 800
    available_tiles = []

    #.........................for vertical positions.............
    for j in range (0,800,100):
        for value in posdict:
            if x == posdict[value][0] and j == posdict[value][1]:
                get.append([x,j])

    for i in get:
        if i[1]>y and abs(i[1]-y) < least_down:
            least_down = abs(i[1]-y)
    for i in get:
        if i[1]<y and abs(i[1]-y) < least_up:
            least_up = abs(i[1]-y)

    for m in range(y-least_up,y+least_down+100,100):
        available_tiles.append([x,m])

    #........................for horizontal positions.............
    for i in range (0,800,100):
        for value in posdict:
            if i == posdict[value][0] and y == posdict[value][1]:
                get.append([i,y])

    for i in get:
        if i[0]>x and abs(i[0]-x) < least_right:
            least_right = abs(i[0]-x)
    for i in get:
        if i[0]<x and abs(i[0]-x) < least_left:
            least_left = abs(i[0]-x)

    for m in range(x-least_left,x+least_right+100,100):
        available_tiles.append([m,y])

    available_tiles.remove([x,y])
    available_tiles.remove([x,y])


    for value in posdict:
        if x == posdict[value][0] and y == posdict[value][1]:
            teamm = posdict[value][2]


    for value in posdict:
        for i in available_tiles:
            if i[0] == posdict[value][0] and i[1] == posdict[value][1] and teamm == posdict[value][2]:
                print("yay")
                available_tiles.remove([i[0],i[1]])

    return available_tiles

def bishop(x,y):
    get = []
    least_tr = 800
    least_tl = 800
    least_br = 800
    least_bl = 800
    available_tiles = []

    #.............................for main Diagonal.........................
    for i in range(-700,800,100):
        for value in posdict:
            if x-i == posdict[value][0] and y-i == posdict[value][1]:
                get.append([x-i,y-i])

    for i in get:
        if i[0]<x and i[1]<y and abs(i[0]-x) < least_tl:
            least_tl =  abs(i[0]-x)
    for i in get:
        if i[0]>x and i[1]>y and abs(i[0]-x) < least_br:
            least_br =  abs(i[0]-x)
            
    for m in range(-least_tl,least_br+100,100):   
        available_tiles.append([x+m,y+m]) 


                
    #.............................for other diagonal.........................
    for i in range(-700,800,100):
        for value in posdict:
            if x+i == posdict[value][0] and y-i == posdict[value][1]:
                get.append([x+i,y-i])
                
    for i in get:
        if i[0]<x and i[1]>y and abs(i[0]-x) < least_bl:
            least_bl =  abs(i[0]-x)
    for i in get:
        if i[0]>x and i[1]<y and abs(i[0]-x) < least_tr:
            least_tr =  abs(i[0]-x)
            
    for m in range(-least_bl,least_tr+100,100):   
        available_tiles.append([x+m,y-m])
    available_tiles.remove([x,y])
    available_tiles.remove([x,y])


    for value in posdict:
        if x == posdict[value][0] and y == posdict[value][1]:
            teamm = posdict[value][2]


    for value in posdict:
        for i in available_tiles:
            if i[0] == posdict[value][0] and i[1] == posdict[value][1] and teamm == posdict[value][2]:
                available_tiles.remove([i[0],i[1]])

    return available_tiles


def king(x,y):
    available_tiles = [[x+100,y],
                       [x-100,y],
                       [x+100,y+100],
                       [x-100,y+100],
                       [x+100,y-100],
                       [x-100,y-100],
                       [x,y-100],
                       [x,y+100]]
                
    for value in posdict:
        if x == posdict[value][0] and y == posdict[value][1]:
            teamm = posdict[value][2]


    for value in posdict:
        for i in available_tiles:
            if i[0] == posdict[value][0] and i[1] == posdict[value][1] and teamm == posdict[value][2]:
                available_tiles.remove([i[0],i[1]])

    return available_tiles
    
def delete(x,y,c,a,b):
    team = [c]
    team1 = []
    
    for val in posdict:
        if a == posdict[val][0] and b == posdict[val][1]:
            team1.append(posdict[val][2])

    if team1 != team:
        print("aaaaa")
        for val in posdict:
            if a == posdict[val][0] and b == posdict[val][1]:
                posdict[val][0] = 800
                posdict[val][1] = 800
        for value in posdict:
            if x == posdict[value][0] and y == posdict[value][1]:
                posdict[value][0] = a
                posdict[value][1] = b

def pawnConversion():
    pawn_destination = True
    out = []
    while pawn_destination:
        gameDisplay.fill(white)
        message_to_screen("Select the Piece", black, -100, size = "large")
        message_to_screen("N - Knight", black, 0, size = "medium")
        message_to_screen("Q - Queen", black, 50, size = "medium")
        message_to_screen("R - Rook", black, 100, size = "medium")
        message_to_screen("B - Bishop", black, 150, size = "medium")
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    out.append("q")
                if event.key == pygame.K_r:
                    out.append("r")
                if event.key == pygame.K_b:
                    out.append("b")
                if event.key == pygame.K_n:
                    out.append("n")
        if len(out)>=1:            
            pawn_destination = False
    return out[0]
    
def turn(team):
    ret = []
    if team == "b":
        ret.clear()
        ret.append("w")

    if team == "w":
        ret.clear()
        ret.append("b")

    return ret[0]

def castling_b(b):
    team = ["b","w"]
    name = ["k","q","r","b","p","n"]
    var = True
    var1 = True
    for value in posdict:
        for i in team:
            for j in name:
                if posdict[value] == [600,700,i,j]:
                    var = False
                if posdict[value] == [500,700,i,j]:
                    var = False
                if posdict[value] == [200,700,i,j]:
                    var1 = False
                if posdict[value] == [300,700,i,j]:
                    var1 = False
    if var:
        b.append([600,700])
    if var1:
        b.append([200,700])

def castling_w(b):
    team = ["b","w"]
    name = ["k","q","r","b","p","n"]
    var = True
    var1 = True
    for value in posdict:
        for i in team:
            for j in name:
                if posdict[value] == [600,0,i,j]:
                    var = False
                if posdict[value] == [500,0,i,j]:
                    var = False
                if posdict[value] == [200,0,i,j]:
                    var1 = False
                if posdict[value] == [300,0,i,j]:
                    var1 = False
    if var:
        b.append([600,0])
    if var1:
        b.append([200,0])

def piece(img,x,y):
    gameDisplay.blit(img,(x,y))

def text_objects(text, color,size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)
    
    return textSurface, textSurface.get_rect()

def message_to_screen(msg, color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (boardwidth / 2), (boardheight / 2)+y_displace
    gameDisplay.blit(textSurf, textRect)

def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size="small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = ((buttonx+(buttonwidth/2)), buttony+(buttonheight/2))
    gameDisplay.blit(textSurf, textRect)

def game_controls():

    gcont = True

    while gcont:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                    
        gameDisplay.fill(white)
        message_to_screen("Controls",
                          green,
                          -100,
                          size="large")
        message_to_screen("Select a piece: Left-click",
                          black,
                          -30,
                          size="small")
        message_to_screen("Select a position: Right-click",
                          black,
                          10,
                          size="small")
        message_to_screen("Pause: P",
                          black,
                          70,
                          size="small")

        button("play", 150,500,100,50, green,light_green,action="play")
##        button("Main Menu", 350,500,100,50, yellow, light_yellow,action="main")
        button("quit", 550,500,100,50,red , light_red,action="quit")
        
        pygame.display.update()
        clock.tick(15)

def game_intro():

    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
##                if event.key == pygame.K_c:
##                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                    
        gameDisplay.fill(white)
        message_to_screen("Welcome to Chess!",
                          green,
                          -100,
                          size="large")
        message_to_screen("Get an opponent",
                          black,
                          -30,
                          size="small")
        message_to_screen("Play your best move",
                          black,
                          10,
                          size="small")
        message_to_screen("Let's see who is the real KING of this Chess-Field",
                          black,
                          70,
                          size="small")



        button("play", 150,500,100,50, green,light_green,action="play")
        button("controls", 350,500,100,50, yellow, light_yellow,action="controls")
        button("quit", 550,500,100,50,red , light_red,action="quit")
        
        pygame.display.update()
        clock.tick(15)

def button (text, x, y, width, height, inactive_color, active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()

            if action == "controls":
                game_controls()

            if action == "play":
                gameLoop()

            if action == "main":
                game_intro()
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))

    text_to_button(text,black,x,y,width,height)

def gameLoop():
    t = "b"
    castling_B = True
    castling_W = True
    gameOver = False
    gameExit = False
    if t == "b":
        phurr = "White"
    else:
        phurr = "Black"

    while not gameExit:



        while gameOver == True:
            gameDisplay.fill(white)
            
            message_to_screen("Team "+phurr+" Wins!!",
                              red,
                              -50,
                              size="medium")
            
            message_to_screen("Thanks For playing!!!",
                              black,
                              50,
                              size="small")
            
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()


        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
        board()        
        piece(BK,posdict.get("pos_BK")[0],posdict.get("pos_BK")[1])
        piece(BQ,posdict.get("pos_BQ")[0],posdict.get("pos_BQ")[1])
        piece(BB,posdict.get("pos_BB_1")[0],posdict.get("pos_BB_1")[1])
        piece(BB,posdict.get("pos_BB_2")[0],posdict.get("pos_BB_2")[1])
        piece(BR,posdict.get("pos_BR_1")[0],posdict.get("pos_BR_1")[1])
        piece(BR,posdict.get("pos_BR_2")[0],posdict.get("pos_BR_2")[1])
        piece(BN,posdict.get("pos_BN_1")[0],posdict.get("pos_BN_1")[1])
        piece(BN,posdict.get("pos_BN_2")[0],posdict.get("pos_BN_2")[1])
        
        piece(imgdict.get(posdict.get("pos_BP_1")[2]+posdict.get("pos_BP_1")[3]),posdict.get("pos_BP_1")[0],posdict.get("pos_BP_1")[1])
        piece(imgdict.get(posdict.get("pos_BP_2")[2]+posdict.get("pos_BP_2")[3]),posdict.get("pos_BP_2")[0],posdict.get("pos_BP_2")[1])
        piece(imgdict.get(posdict.get("pos_BP_3")[2]+posdict.get("pos_BP_3")[3]),posdict.get("pos_BP_3")[0],posdict.get("pos_BP_3")[1])
        piece(imgdict.get(posdict.get("pos_BP_4")[2]+posdict.get("pos_BP_4")[3]),posdict.get("pos_BP_4")[0],posdict.get("pos_BP_4")[1])
        piece(imgdict.get(posdict.get("pos_BP_5")[2]+posdict.get("pos_BP_5")[3]),posdict.get("pos_BP_5")[0],posdict.get("pos_BP_5")[1])
        piece(imgdict.get(posdict.get("pos_BP_6")[2]+posdict.get("pos_BP_6")[3]),posdict.get("pos_BP_6")[0],posdict.get("pos_BP_6")[1])
        piece(imgdict.get(posdict.get("pos_BP_7")[2]+posdict.get("pos_BP_7")[3]),posdict.get("pos_BP_7")[0],posdict.get("pos_BP_7")[1])
        piece(imgdict.get(posdict.get("pos_BP_8")[2]+posdict.get("pos_BP_8")[3]),posdict.get("pos_BP_8")[0],posdict.get("pos_BP_8")[1])
        
        piece(WK,posdict.get("pos_WK")[0],posdict.get("pos_WK")[1])
        piece(WQ,posdict.get("pos_WQ")[0],posdict.get("pos_WQ")[1])
        piece(WB,posdict.get("pos_WB_1")[0],posdict.get("pos_WB_1")[1])
        piece(WB,posdict.get("pos_WB_2")[0],posdict.get("pos_WB_2")[1])
        piece(WR,posdict.get("pos_WR_1")[0],posdict.get("pos_WR_1")[1])
        piece(WR,posdict.get("pos_WR_2")[0],posdict.get("pos_WR_2")[1])
        piece(WN,posdict.get("pos_WN_1")[0],posdict.get("pos_WN_1")[1])
        piece(WN,posdict.get("pos_WN_2")[0],posdict.get("pos_WN_2")[1])
        
        piece(imgdict.get(posdict.get("pos_WP_1")[2]+posdict.get("pos_WP_1")[3]),posdict.get("pos_WP_1")[0],posdict.get("pos_WP_1")[1])
        piece(imgdict.get(posdict.get("pos_WP_2")[2]+posdict.get("pos_WP_2")[3]),posdict.get("pos_WP_2")[0],posdict.get("pos_WP_2")[1])
        piece(imgdict.get(posdict.get("pos_WP_3")[2]+posdict.get("pos_WP_3")[3]),posdict.get("pos_WP_3")[0],posdict.get("pos_WP_3")[1])
        piece(imgdict.get(posdict.get("pos_WP_4")[2]+posdict.get("pos_WP_4")[3]),posdict.get("pos_WP_4")[0],posdict.get("pos_WP_4")[1])
        piece(imgdict.get(posdict.get("pos_WP_5")[2]+posdict.get("pos_WP_5")[3]),posdict.get("pos_WP_5")[0],posdict.get("pos_WP_5")[1])
        piece(imgdict.get(posdict.get("pos_WP_6")[2]+posdict.get("pos_WP_6")[3]),posdict.get("pos_WP_6")[0],posdict.get("pos_WP_6")[1])
        piece(imgdict.get(posdict.get("pos_WP_7")[2]+posdict.get("pos_WP_7")[3]),posdict.get("pos_WP_7")[0],posdict.get("pos_WP_7")[1])
        piece(imgdict.get(posdict.get("pos_WP_8")[2]+posdict.get("pos_WP_8")[3]),posdict.get("pos_WP_8")[0],posdict.get("pos_WP_8")[1])
        

        #............................................................................................selecting a piece
        for x in range (0,900,100):
            for y in range (0,900,100):
                sel_x,sel_y,sel_team,sel_name = selected_tile(x,y)
                
        if sel_team == t:
            if sel_name == "n" :
                b = knight(sel_x,sel_y)
                a = selection(b)
                check_list = []
                print(a)
                if len(a)>1:
                    for value in posdict:
                        if a[0] == posdict[value][0] and a[1] == posdict[value][1]:
                            if posdict[value][3] == "k":
                                gameOver = True
                    delete(sel_x,sel_y,sel_team,a[0],a[1])
                    t = turn(t)
                    check_list = knight(a[0],a[1])
                    print(check_list)
                    for value in posdict:
                        if posdict[value][3] == "k" :
                            x = posdict[value][0]
                            y = posdict[value][1]
                        for i in check_list:
                            if i[0] == x and i[1] == y:
                                gameDisplay.fill(white)
                                message_to_screen("check for "+phurr, light_red, -50, size = "large")
                                pygame.display.update()
                                clock.tick(9)
                    check_list.clear()

            
            if sel_name == "k":
                b = king(sel_x,sel_y)
                if castling_B and sel_team == "b":
                    castling_b(b)
                if castling_W and sel_team == "w":
                    castling_w(b)
                a = selection(b)
                print(a)
                if len(a)>1:
                    for value in posdict:
                        if a[0] == posdict[value][0] and a[1] == posdict[value][1]:
                            if posdict[value][3] == "k":
                                gameOver = True
                    if castling_B and a[0] == 600 and a[1] == 700:
                        delete(700,700,sel_team,500,700)
                    if castling_W and a[0] == 600 and a[1] == 0:
                        delete(700,0,sel_team,500,0)
                    if castling_B and a[0] == 200 and a[1] == 700:
                        delete(0,700,sel_team,300,700)
                    if castling_W and a[0] == 200 and a[1] == 0:
                        delete(0,0,sel_team,300,0)
                    delete(sel_x,sel_y,sel_team,a[0],a[1])
                        
                    if sel_team == "b" and castling_B:
                        castling_B = False
                    elif sel_team == "w":
                        castling_W = False
                    t = turn(t)
                    check_list = king(a[0],a[1])
                    print(check_list)
                    for value in posdict:
                        if posdict[value][3] == "k" :
                            x = posdict[value][0]
                            y = posdict[value][1]
                        for i in check_list:
                            if i[0] == x and i[1] == y:
                                gameDisplay.fill(white)
                                message_to_screen("check for "+phurr, light_red, -50, size = "large")
                                pygame.display.update()
                                clock.tick(9)
                    check_list.clear()
            if sel_name == "q":
                b = queen(sel_x,sel_y)
                a = selection(b)
                print(a)
                if len(a)>1:
                    for value in posdict:
                        if a[0] == posdict[value][0] and a[1] == posdict[value][1]:
                            if posdict[value][3] == "k":
                                gameOver = True
                    delete(sel_x,sel_y,sel_team,a[0],a[1])
                    t = turn(t)
                    check_list = queen(a[0],a[1])
                    print(check_list)
                    for value in posdict:
                        if posdict[value][3] == "k" :
                            x = posdict[value][0]
                            y = posdict[value][1]
                        for i in check_list:
                            if i[0] == x and i[1] == y:
                                gameDisplay.fill(white)
                                message_to_screen("check for "+phurr, light_red, -50, size = "large")
                                pygame.display.update()
                                clock.tick(9)
                    check_list.clear()
            if sel_name == "pb":
                b = pawnb(sel_x,sel_y)
                a = selection(b)
                print(a)
                if len(a)>1:
                    for value in posdict:
                        if a[0] == posdict[value][0] and a[1] == posdict[value][1]:
                            if posdict[value][3] == "k":
                                gameOver = True
                    delete(sel_x,sel_y,sel_team,a[0],a[1])
                    if not gameOver:
                        for value in posdict:
                            if a[0] == posdict[value][0] and a[1] == 0:
                                c = pawnConversion()
                                posdict[value][3] = c
                            
                    t = turn(t)
                    check_list = pawnb(a[0],a[1])
                    print(check_list)
                    for value in posdict:
                        if posdict[value][3] == "k" :
                            x = posdict[value][0]
                            y = posdict[value][1]
                        for i in check_list:
                            if i[0] == x and i[1] == y:
                                gameDisplay.fill(white)
                                message_to_screen("check for "+phurr, light_red, -50, size = "large")
                                pygame.display.update()
                                clock.tick(9)
                    check_list.clear()
            if sel_name == "pw":
                b = pawnw(sel_x,sel_y)
                a = selection(b)
                print(a)
                if len(a)>1:
                    for value in posdict:
                        if a[0] == posdict[value][0] and a[1] == posdict[value][1]:
                            if posdict[value][3] == "k":
                                gameOver = True
                    delete(sel_x,sel_y,sel_team,a[0],a[1])

                    for value in posdict:
                        if a[0] == posdict[value][0] and a[1] == 700:
                            c = pawnConversion()
                            posdict[value][3] = c
                            
                    t = turn(t)
                    check_list = pawnw(a[0],a[1])
                    print(check_list)
                    for value in posdict:
                        if posdict[value][3] == "k" :
                            x = posdict[value][0]
                            y = posdict[value][1]
                        for i in check_list:
                            if i[0] == x and i[1] == y:
                                gameDisplay.fill(white)
                                message_to_screen("check for "+phurr, light_red, -50, size = "large")
                                pygame.display.update()
                                clock.tick(9)
                    check_list.clear()
            if sel_name == "r":
                b = rook(sel_x,sel_y)
                a = selection(b)
                print(a)
                if len(a)>1:
                    for value in posdict:
                        if a[0] == posdict[value][0] and a[1] == posdict[value][1]:
                            if posdict[value][3] == "k":
                                gameOver = True
                    delete(sel_x,sel_y,sel_team,a[0],a[1])
                    if sel_team == "b":
                        castling_B = False
                    elif sel_team == "w":
                        castling_W = False
                    t = turn(t)
                    check_list = rook(a[0],a[1])
                    print(check_list)
                    for value in posdict:
                        if posdict[value][3] == "k" :
                            x = posdict[value][0]
                            y = posdict[value][1]
                        for i in check_list:
                            if i[0] == x and i[1] == y:
                                gameDisplay.fill(white)
                                message_to_screen("check for "+phurr, light_red, -50, size = "large")
                                pygame.display.update()
                                clock.tick(9)
                    check_list.clear()
            if sel_name == "b":
                b = bishop(sel_x,sel_y)
                a = selection(b)
                print(a)
                if len(a)>1:
                    for value in posdict:
                        if a[0] == posdict[value][0] and a[1] == posdict[value][1]:
                            if posdict[value][3] == "k":
                                gameOver = True
                    delete(sel_x,sel_y,sel_team,a[0],a[1])
                    t = turn(t)
                    check_list = bishop(a[0],a[1])
                    print(check_list)
                    for value in posdict:
                        if posdict[value][3] == "k" :
                            x = posdict[value][0]
                            y = posdict[value][1]
                        for i in check_list:
                            if i[0] == x and i[1] == y:
                                gameDisplay.fill(white)
                                message_to_screen("check for "+phurr, light_red, -50, size = "large")
                                pygame.display.update()
                                clock.tick(9)
                    check_list.clear()

                    
        pygame.display.update()
        clock.tick(10)


    pygame.display.update()
    

game_intro()    
gameLoop()


