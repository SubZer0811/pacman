import pygame
import sys
import random
from maze import *
from player import *
from ghost import *

coin_score=0

pygame.init()
surface = pygame.display.set_mode((560,620))

player_1 = player([13, 29], surface)
player_1.draw()

mapobj= maze_map(surface)
mapobj.show()

ghost1=ghost([11,13],surface)

pygame.display.flip()

clock = pygame.time.Clock()

while True:
	ghost1.move_ghost()
	keys = pygame.key.get_pressed()

	tmp_x = player_1.player_coord[0]
	tmp_y = player_1.player_coord[1]
	if keys[pygame.K_RIGHT]:
		if(maze[tmp_y][tmp_x+1]==9 or maze[tmp_y][tmp_x+1]==0):
			print("right")
			if(maze[tmp_y][tmp_x+1]==9):
				coin_score+=1
				maze[tmp_y][tmp_x+1]=0
				print("Score:",coin_score)
			player_1.cleardraw()
			player_1.player_coord[0]+=1
			player_1.draw()
	elif keys[pygame.K_LEFT]:
		if(maze[tmp_y][tmp_x-1]==9 or maze[tmp_y][tmp_x-1]==0):
			print("left")
			if(maze[tmp_y][tmp_x-1]==9):
				coin_score+=1
				maze[tmp_y][tmp_x-1]=0
				print("Score:",coin_score)
			player_1.cleardraw()
			player_1.player_coord[0]-=1
			player_1.draw()
	elif keys[pygame.K_UP]:
		if(maze[tmp_y-1][tmp_x]==9 or maze[tmp_y-1][tmp_x]==0):
			print("up")
			if(maze[tmp_y-1][tmp_x]==9):
				coin_score+=1
				maze[tmp_y-1][tmp_x]=0
				print("Score:",coin_score)
			player_1.cleardraw()
			player_1.player_coord[1]-=1
			player_1.draw()
	elif keys[pygame.K_DOWN]:
		if(maze[tmp_y+1][tmp_x]==9 or maze[tmp_y+1][tmp_x]==0):
			print("down")
			if(maze[tmp_y+1][tmp_x]==9):
				coin_score+=1
				maze[tmp_y+1][tmp_x]=0
				print("Score:",coin_score)
			player_1.cleardraw()
			player_1.player_coord[1]+=1
			player_1.draw()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print("Quit")
			pygame.quit()
			exit()

	clock.tick(8)
	pygame.display.flip()