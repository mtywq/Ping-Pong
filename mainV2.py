from pygame import *
from random import randint
import time as tm
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
plsyer1_csore = 0
plsyer2_csore = 0
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
        if keys_pressed[K_e] and self.rect.y < 500:
            self.rect.y += self.speed
        if keys_pressed[K_d] and self.rect.y > 0:
            self.rect.y -= self.speed

class Playerr(GameSprite):
    def walking(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_o] and self.rect.y < 500:
            self.rect.y += self.speed
        if keys_pressed[K_k] and self.rect.y > 0:
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
            self.speed_y = -self.speed_y#; self.speed_y *= 1.01; self.speed_x *= 1.01
        if self.rect.y <= 575:
            self.speed_y = -self.speed_y#; self.speed_y *= 1.01; self.speed_x *= 1.01
#window~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
win_h = 800; win_w = 600
wind = display.set_mode((win_h,win_w))
display.set_caption("Ping-Pong")
bg = transform.scale(image.load("bg.png"), (win_h, win_w))
clock = time.Clock()
#sounds~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
mixer.init()
mixer.music.load(open("music.ogg"))
#collision_sound = mixer.Sound("collision.mp3")
#lose_sound = mixer.Sound('lose.mp3')
mixer.music.play()
def sound_play(a,b):
    mixer.init()
    mixer.music.load(a)
    mixer.music.play()
    tm.sleep(b)
    mixer.music.stop()
    mixer.quit()
    mixer.init()
    mixer.music.load(open("music.ogg"))
    mixer.music.play() 
#font~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
font.init()
defaultFont = font.SysFont("Arial", 64)
#sprites~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
player1 = Player(25,100, "platform.png",10,50,250)
player2 = Playerr(25,100, "platform.png",10,750,250)
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
        #point1 = defaultFont.render("PLAYER 1 GETS POINT!",1,(randint(0,255),randint(0,255),randint(0,255)))
        #point2= defaultFont.render("PLAYER 2 GETS POINT!",1,(randint(0,255),randint(0,255),randint(0,255)))
        lose1 = defaultFont.render("PLAYER 1 WINS!",1,(randint(0,255),randint(0,255),randint(0,255)))
        lose2 = defaultFont.render("PLAYER 2  WINS!",1,(randint(0,255),randint(0,255),randint(0,255)))
        players_score = defaultFont.render(f"{plsyer1_csore}:{plsyer2_csore}", 1,(randint(0,255),randint(0,255),randint(0,255)))
        wind.blit(players_score,(360,25))
        player1.show(); player1.walking()
        player2.show(); player2.walking()
        sphere.show(); sphere.move()
        if player1.rect.colliderect(sphere):
            sphere.speed_x *= -1;#; sphere.speed_y *= 1.01; sphere.speed_x *= 1.01
        if player2.rect.colliderect(sphere):
            sphere.speed_x *= -1#; sphere.speed_y *= 1.01; sphere.speed_x *= 1.01
        if sphere.rect.x <= 0: 
            #wind.blit(point1,(100,260))
            plsyer2_csore += 1; sphere.kill(); time.delay(1200)
            sphere =  Ball(25,25,"ball.png",2,400,300)
        if sphere.rect.x >= 800:
            #wind.blit(point2,(100,260))
            plsyer1_csore += 1; sphere.kill(); time.delay(1200)
            sphere =  Ball(25,25,"ball.png",2,400,300)
        if plsyer1_csore == 5:
            wind.blit(lose1,(210,260)); finish = True
        if plsyer2_csore == 5:
            wind.blit(lose2,(210,260)); finish = True
    else:
        finish = False
        sound_play("lose.mp3", 3)
        plsyer1_csore = 0; plsyer2_csore = 0
        sphere.kill(); sphere =  Ball(25,25,"ball.png",2,400,300)     

    display.update(); clock.tick(60)
