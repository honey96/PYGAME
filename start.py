import pygame
import OpenGL
import os
import time
import random
pygame.init()
width=800
height=600
black=(0,0,0)
white=(100,100,100)
color=(34,139,34)
red=(255,0,0)
surface=pygame.display.set_mode((width,height))
pygame.display.set_caption('GAME')
timer=pygame.time.Clock()
image=pygame.image.load('racecar.png')

def score(count):
	font = pygame.font.SysFont(None, 25)
	text = font.render("Score: "+str(count), True,black)
	surface.blit(text,(0,0))


def obstacle(obs_x,obs_y,color,obs_w,obs_h):
	pygame.draw.rect(surface,color,[obs_x,obs_y,obs_w,obs_h])



def car(x,y):
	surface.blit(image,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((width/2),(height/2))
    surface.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    start()

def end_game():
	message_display("GAME OVER")

def start():
	flag=False	
	x=(width*0.45)    #1080*0.45
	y=(height*0.8)
	del_x=0
	obs_x=random.randrange(0,width)
	obs_y = -600
	obs_speed = 4
	obs_w = 100
	obs_h = 100
	score_count=0	
	while not flag:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				flag=True
			if event.type == pygame.KEYDOWN:
				if event.key ==pygame.K_LEFT:
					del_x=-5
				elif event.key == pygame.K_RIGHT:
					del_x=5
				
			if event.type == pygame.KEYUP:
				if event.key ==pygame.K_LEFT or event.key == pygame.K_RIGHT:
					del_x=0
					

		x=x+del_x
		surface.fill(color)
		obstacle(obs_x,obs_y,red,obs_w,obs_h)
		obs_y=obs_y+obs_speed

		car(x,y)
		score(score_count)


		if x<0 or  x > width-73:
			end_game()

		if obs_y > height:
			obs_y = 0 - obs_h
			obs_x =random.randrange(0,width)
			score_count+=1
			obs_speed+=1
			obs_w+= (score_count*1.2)


		if y < obs_y+obs_h:
			print('crossover')
			if x > obs_x and x < obs_x + obs_w or x+ 73 >obs_x and x+ 73< obs_x + obs_w:
				print('x crossover')
				end_game()

		
		pygame.display.update()
		timer.tick(60)

start()
pygame.quit()
quit()












