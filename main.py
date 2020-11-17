import pygame
import sys
import random
from maze import *
from player import *
from ghost import *

coin_score=0

pygame.init()
pygame.font.init()
surface = pygame.display.set_mode((560,700))

mapobj= maze_map(surface)
mapobj.show()

player_1 = player([13, 29], surface)
player_1.draw()

ghost1=ghost([11,13],surface)

pygame.display.flip()
clock = pygame.time.Clock()

GAME_FONT = pygame.font.SysFont('Comic Sans MS', 24)
# ghost1.move_ghost()

thread_status = [0, 0, 0, 0]

while True:
	# print(pygame.time.get_ticks())
	thread_status = [0, 0, 0, 0]
	keys = pygame.key.get_pressed()

	tmp_x = player_1.player_coord[0]
	tmp_y = player_1.player_coord[1]

	if(ghost1.coord == player_1.player_coord):
		print("dead")
		if(player_1.lives - 1 > 0):
			player_1.lives -= 1
			player_1.player_coord[0] = 13; player_1.player_coord[1] = 29
			pygame.time.wait(1000)
			continue
		else:
			ghost1.thread.join()
			exit(0)

	if keys[pygame.K_RIGHT]:
		if(maze[tmp_y][tmp_x+1]==9 or maze[tmp_y][tmp_x+1]==0):
			# print("right")
			if(maze[tmp_y][tmp_x+1]==9):
				coin_score+=1
				maze[tmp_y][tmp_x+1]=0
				# print("Score:",coin_score)
			player_1.cleardraw()
			player_1.player_coord[0]+=1
			player_1.draw()
	elif keys[pygame.K_LEFT]:
		if(maze[tmp_y][tmp_x-1]==9 or maze[tmp_y][tmp_x-1]==0):
			# print("left")
			if(maze[tmp_y][tmp_x-1]==9):
				coin_score+=1
				maze[tmp_y][tmp_x-1]=0
				# print("Score:",coin_score)
			player_1.cleardraw()
			player_1.player_coord[0]-=1
			player_1.draw()
	elif keys[pygame.K_UP]:
		if(maze[tmp_y-1][tmp_x]==9 or maze[tmp_y-1][tmp_x]==0):
			# print("up")
			if(maze[tmp_y-1][tmp_x]==9):
				coin_score+=1
				maze[tmp_y-1][tmp_x]=0
				# print("Score:",coin_score)
			player_1.cleardraw()
			player_1.player_coord[1]-=1
			player_1.draw()
	elif keys[pygame.K_DOWN]:
		if(maze[tmp_y+1][tmp_x]==9 or maze[tmp_y+1][tmp_x]==0):
			# print("down")
			if(maze[tmp_y+1][tmp_x]==9):
				coin_score+=1
				maze[tmp_y+1][tmp_x]=0
				# print("Score:",coin_score)
			player_1.cleardraw()
			player_1.player_coord[1]+=1
			player_1.draw()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print("Quit")
			pygame.quit()
			exit()

	pygame.draw.rect(surface, (0, 0, 0), pygame.Rect((0, 621), (560, 80))) 
	text = GAME_FONT.render("LIVES: "+ str(player_1.lives) +50*' '+"SCORE: " + str(coin_score), True, (255, 0, 255))
	surface.blit(text, (100, 650))
	
	while True:
		if(sum(thread_status) == 1):
    		break

	clock.tick(8)
	
	pygame.display.flip()