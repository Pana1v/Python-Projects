import random 
import pygame,sys

#setup
pygame.init()
clock=pygame.time.Clock()

#main window

screen_width= 1200
screen_height=600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Ping Pong')
ball_x=13*random.choice((1,-1))
ball_y=14*random.choice((1,-1))
# Rectangles
# 0,0 is on top left (x,y,width,height)
player_speed=0
opponent_speed=20
ball = pygame.Rect(screen_width/2-15,screen_height/2-15,30,30)
player=pygame.Rect(screen_width-20,screen_height/2- 70, 10,140)
opponent = pygame.Rect(10,screen_height/2-70,10,140)
bg_color=pygame.Color('black')
pink=(59, 22, 39)
def ball_restart():
    global ball_x,ball_y
    ball.center=(screen_width/2,screen_height/2)
    ball_x*=random.choice((1,-1))
    ball_y*=random.choice((1,-1))
def player_anim():
    if player.top<=0:
        player.top=0
    if player.bottom>=screen_height:
        player.bottom=screen_height
    player.y+=player_speed
def opponent_ai():
    if opponent.top<ball.y:
        opponent.top+=opponent_speed
    if opponent.bottom>ball.y:
        opponent.bottom-=opponent_speed
    if opponent.top<=0:
        opponent.top=0
    if opponent.bottom>=screen_height:
        opponent.bottom=screen_height
    player.y+=player_speed
def ball_anim():
    global ball_x,ball_y
    ball.x+=ball_x
    ball.y+=ball_y
    if ball.top<=0 or ball.bottom>=screen_height:
        ball_y*=-1
    if ball.left<=0 or ball.right >=screen_width:
        ball_x*=-1
        ball_restart()
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_x*=-1
while True : 
    # Inputs
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:
                player_speed+=14
            if event.key==pygame.K_UP:
                player_speed-=14
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_DOWN:
                player_speed-=14
            if event.key==pygame.K_UP:
                player_speed+=14
    # Updating the window
    ball_anim()
    player_anim()
    opponent_ai()
    screen.fill(bg_color)
    pygame.draw.aaline(screen,pink,(0,screen_height/2),(screen_width,screen_height/2))
    pygame.draw.rect(screen,'grey12',opponent)
    pygame.draw.rect(screen,'red',player)
    
    pygame.draw.aaline(screen,pink,(screen_width/2,0),(screen_width/2,screen_height))
    pygame.draw.ellipse(screen,'yellow',ball)
    pygame.display.flip()
    clock.tick(60)
    # limits how fast the loop runs

#most basic element - display surface
# image needs to be on the surface in order to be visible
# regular surface (You can have as many of them as you want)
# you can add drawings, etc,  RECTANGLES can be put around surfaces.
