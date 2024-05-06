from pygame import *
from random import randint
from time import sleep
#vars~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
startx = randint(1,2)
starty = randint(1,2)
if startx == 1:
    speed_x = 2.5
else: 
    speed_x = -2.5
if starty == 1:
    speed_y = 2.5
else: 
    speed_y = -2.5
#classes~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class GameSprite(sprite.Sprite):
    def __init__(self,sizex, sizey, pImage,sped,xcor,ycor):
        super().__init__()
        self.xSize = sizex
        self.ySize = sizey
        self.image = transform.scale(image.load(pImage),(self.xSize,self.ySize))
        self.speed = sped
        self.rect = self.image.get_rect()
        self.rect.x = xcor
        self.rect.y = ycor
    def show(self):
        wind.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def walking(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_q] and self.rect.y < 500:
            self.rect.y += self.speed
        if keys_pressed[K_a] and self.rect.y > 0:
            self.rect.y -= self.speed

class Playerr(GameSprite):
    def walking(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_d] and self.rect.y < 500:
            self.rect.y += self.speed
        if keys_pressed[K_e] and self.rect.y > 0:
            self.rect.y -= self.speed

class Ball(GameSprite):
    global startx
    global starty
    if startx == 1:
        speed_x = 2.5
    else: 
        speed_x = -2.5
    if starty == 1:
        speed_y = 2.5
    else: 
        speed_y = -2.5
    def move(self):
        self.rect.x += self.speed_x
        self.rect.y -= self.speed_y
        if self.rect.y >= 0:
            self.speed_y = -self.speed_y
            #collide_sound.play()
        if self.rect.y <= 575:
            self.speed_y = -self.speed_y
            #collide_sound.play()
#window~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
win_h = 800; win_w = 600
wind = display.set_mode((win_h,win_w))
display.set_caption("Ping-Pong")
bg = transform.scale(image.load("bg.png"), (win_h, win_w))
clock = time.Clock()
#sounds~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
mixer.init()
mixer.music.load(open("music.ogg"))
#collide_sound = mixer.Sound("collide.ogg") - тут ошибка
#lose_sound = mixer.Sound("lose.ogg") - и тут тоже 
mixer.music.play()
#font~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
font.init()
defaultFont = font.SysFont("Arial", 64)
#sprites~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
player1 = Player(25,100, "platform.png",7,50,400)
player2 = Playerr(25,100, "platform.png",7,750,400)
players = sprite.Group(); players.add(player1); players.add(player2)
sphere =  Ball(25,25,"ball.png",2,400,300)
#cycle~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
game = True; finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True: 
        wind.blit(bg,(0,0))
        lose1 = defaultFont.render("PLAYER 1 WIN",1,(randint(0,255),randint(0,255),randint(0,255)))
        lose2 = defaultFont.render("PLAYER 2 WIN",1,(randint(0,255),randint(0,255),randint(0,255)))
        player1.show(); player1.walking()
        player2.show(); player2.walking()
        sphere.show(); sphere.move()
        if player1.rect.colliderect(sphere):
            sphere.speed_x *= -1
            #collide_sound.play()
        if player2.rect.colliderect(sphere):
            sphere.speed_x *= -1
            #collide_sound.play()
        if sphere.rect.x <= 0: 
            wind.blit(lose1,(215,270))
            #lose_sound.play()
            finish = True
        if sphere.rect.x >= 800:
            wind.blit(lose2,(215,270))
            #lose_sound.play()
            finish = True      
    else:
        finish = False

    display.update(); clock.tick(60)
