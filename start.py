import pygame
import OpenGL
import os
import time
pygame.init()
width=1080
height=1080
black=(0,0,0)
white=(100,100,100)
color=(34,139,34)
surface=pygame.display.set_mode((width,height))
pygame.display.set_caption('GAME')
timer=pygame.time.Clock()
image=pygame.image.load('racecar.png')

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
	x=(width*0.50)    #1080*0.45
	y=(height*0.45)
	del_x=0
	del_y=0
	while not flag:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				flag=True
			if event.type == pygame.KEYDOWN:
				if event.key ==pygame.K_LEFT:
					del_x=-6
				elif event.key == pygame.K_RIGHT:
					del_x=6
				elif event.key ==pygame.K_UP:
					del_y=-6
				elif event.key ==pygame.K_DOWN:
					del_y=6
			if event.type == pygame.KEYUP:
				if event.key ==pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key ==pygame.K_UP or event.key ==pygame.K_DOWN :
					del_x=0
					del_y=0

		x=x+del_x
		y=y+del_y
		surface.fill(color)
		car(x,y)
		if x<0 or y<0 or x > width-75 or y > height-450:
			end_game()

		
		pygame.display.update()
		timer.tick(60)

start()
pygame.quit()
quit()












