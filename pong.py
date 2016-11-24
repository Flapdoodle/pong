import pygame
import random

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
pygame.mixer.init()

song = 'C:/Users/Austin Abate/Downloads/Gamesongs/Track1.wav'
pygame.mixer.music.load(song)
pygame.mixer.music.play(-1)

global displayWidth, displayHeight, FPS, screen

displayWidth = 1000
displayHeight = 500

paddleWidth = 15
paddleHeight = 60

ballWidth = 15
ballHeight = 15


white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

FPS = 60
clock = pygame.time.Clock()

pygame.display.set_caption('Austins Game')
screen = pygame.display.set_mode([displayWidth, displayHeight])
background = pygame.Surface(screen.get_size())
background.fill((black))
background = background.convert()
screen.blit(background, (0,0))

def mainloop():
    global xStart1, xStart2, yStart1, yStart2, ballStartX, ballStartY, ballSpeed, score1, score2, dx, dy
    dx = -8 #x speed
    dy = 3 #y speed
    StartDirX = random.randint(1,2)
    if StartDirX == 1:
        dx *= (-1)
    elif StartDirX == 2:
        dx *= (-1)
    StartDirY = random.randint(1,2)
    if StartDirX == 1:
        dy *= (-1)
    elif StartDirX == 2:
        dy *= (-1)
    score1 = 0
    score2 = 0
    xStart1 = 0
    xStart2 = displayWidth - paddleWidth
    yStart1 = displayHeight/2
    yStart2 = displayHeight/2
    yStartChange = 5
    ballStartX = displayWidth/2
    ballStartY = displayHeight/2
    ballSpeed = 5
    mainloop = True
    
    while mainloop == True:
        keys = pygame.key.get_pressed()
        screen.fill(black)
        Paddle1 = pygame.draw.rect(screen, white, ([xStart1,yStart1,paddleWidth,paddleHeight]))
        Paddle2 = pygame.draw.rect(screen, white, ([xStart2,yStart2,paddleWidth,paddleHeight]))
        ball = pygame.draw.rect(screen, white, ([ballStartX,ballStartY,ballWidth,ballHeight]))
        ballStartX = ballStartX + dx
        ballStartY = ballStartY + dy
        if ballStartY + ballHeight >= displayHeight:
            dy *= (-1)
        if ballStartY <= 0:
            dy *= (-1)
        if Paddle1.colliderect(ball):
            dx *= (-1)
            ballStartX = 0 + paddleWidth + 1
        if Paddle2.colliderect(ball):
            dx *= (-1)
            ballStartX = displayWidth - paddleWidth - ballWidth - 1
        if ballStartX < 0:
            score2 = score2 + 1
            ballStartX = displayWidth/2
        if ballStartX > displayWidth - ballWidth:
            score1 = score1 + 1
            ballStartX = displayWidth/2
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        if keys[pygame.K_w]:
            yStart1 -= yStartChange
                    
        if keys[pygame.K_s]:
            yStart1 += yStartChange
                    
        if keys[pygame.K_UP]:
            yStart2 -= yStartChange
                    
        if keys[pygame.K_DOWN]:
            yStart2 += yStartChange

        if yStart1 + paddleHeight >= displayHeight:
            yStart1 = displayHeight - paddleHeight
        if yStart2 + paddleHeight >= displayHeight:
            yStart2 = displayHeight - paddleHeight
        if not yStart1 >= 0:
            yStart1 = 0
        if not yStart2 >= 0:
            yStart2 = 0

        text = "Score: " + str(score1) + " to " + str(score2)
        pygame.display.set_caption(text)
        clock.tick(FPS)
        pygame.display.flip()
        
mainloop()
pygame.quit()
