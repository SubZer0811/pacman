import pygame
import sys
import random
import threading
import math
import time
import multiprocessing
from maze_map import *
from player import *
from draw import *
import config
from ghost import *

thread_status = [0, 0, 0, 0]

pygame.init()
pygame.display.set_caption('PACMAN')
pygame.font.init()

config.WIDTH = 560
config.HEIGHT = 700
surface = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
config.surface = surface

image = pygame.image.load(r'start_screen.png') 

surface.blit(image, (1, 1)) 

start = "Press SPACE to start the game!"
draw_text(start, config.surface, [
					config.WIDTH//2, 660],  50, (255, 255, 255), 'Comic Sans MS', centered=True)

pygame.display.update()

flag = 0
while True:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
			flag = 1
			break
	if flag:
		break
		pygame.display.update()

mapobj = maze_map(surface)
mapobj.show()

player_1 = player([13, 29], surface)

ghost1 = ghost([11, 13], surface, 0, color="red")
ghost2 = ghost([15, 13], surface, 1, color="blue")
ghost3 = ghost([14, 13], surface, 2, color="yellow")

draw((ghost1.coord), ghost1.ghost_colour)
draw((ghost2.coord), ghost2.ghost_colour)
draw((ghost3.coord), ghost3.ghost_colour)

pygame.display.flip()
clock = pygame.time.Clock()

GAME_FONT = pygame.font.SysFont('Comic Sans MS', 24)


with multiprocessing.Manager() as manager:

	snd = manager.dict()
	snd1 = manager.dict()
	snd2 = manager.dict()
	snd3 = manager.dict()

	snd['t_stat'] = thread_status
	snd['player_coord'] = player_1.player_coord
	snd['maze'] = maze

	snd1['draw'] = ([-1, -1], (255, 255, 255))
	snd1['clear_draw'] = (-1, -1)
	snd1['draw_coin1'] = (-1, -1)
	snd1['draw_coin2'] = (-1, -1)

	snd2['draw'] = ([-1, -1], (255, 255, 255))
	snd2['clear_draw'] = (-1, -1)
	snd2['draw_coin1'] = (-1, -1)
	snd2['draw_coin2'] = (-1, -1)

	snd3['draw'] = ([-1, -1], (255, 255, 255))
	snd3['clear_draw'] = (-1, -1)
	snd3['draw_coin1'] = (-1, -1)
	snd3['draw_coin2'] = (-1, -1)

	p1 = multiprocessing.Process(target=ghost1.move_ghost, args=(snd, snd1))
	p2 = multiprocessing.Process(target=ghost2.move_ghost, args=(snd, snd2))
	p3 = multiprocessing.Process(target=ghost3.move_ghost, args=(snd, snd3))

	p1.start()
	p2.start()
	p3.start()

	while True:

		keys = pygame.key.get_pressed()

		tmp_x = player_1.player_coord[0]
		tmp_y = player_1.player_coord[1]

		if keys[pygame.K_RIGHT]:
			if(maze[tmp_y][tmp_x+1] == 9 or maze[tmp_y][tmp_x+1] == 0):
				maze[tmp_y][tmp_x] = 0
				if(maze[tmp_y][tmp_x+1] == 9):		# check coin
					player_1.coin_score += 1			# increment score
					maze[tmp_y][tmp_x+1] = 0			# update map with no coin

				player_1.player_coord[0] += 1
				maze[player_1.player_coord[1]][player_1.player_coord[0]] = 7

		elif keys[pygame.K_LEFT]:
			if(maze[tmp_y][tmp_x-1] == 9 or maze[tmp_y][tmp_x-1] == 0):
				maze[tmp_y][tmp_x] = 0
				if(maze[tmp_y][tmp_x-1] == 9):
					player_1.coin_score += 1
					maze[tmp_y][tmp_x-1] = 0

				player_1.player_coord[0] -= 1
				maze[player_1.player_coord[1]][player_1.player_coord[0]] = 7
		elif keys[pygame.K_UP]:
			if(maze[tmp_y-1][tmp_x] == 9 or maze[tmp_y-1][tmp_x] == 0):
				maze[tmp_y][tmp_x] = 0
				if(maze[tmp_y-1][tmp_x] == 9):
					player_1.coin_score += 1
					maze[tmp_y-1][tmp_x] = 0

				player_1.player_coord[1] -= 1
				maze[player_1.player_coord[1]][player_1.player_coord[0]] = 7
		elif keys[pygame.K_DOWN]:
			if(maze[tmp_y+1][tmp_x] == 9 or maze[tmp_y+1][tmp_x] == 0):
				maze[tmp_y][tmp_x] = 0
				if(maze[tmp_y+1][tmp_x] == 9):
					player_1.coin_score += 1
					maze[tmp_y+1][tmp_x] = 0

				player_1.player_coord[1] += 1
				maze[player_1.player_coord[1]][player_1.player_coord[0]] = 7
		for event in pygame.event.get():
			if event.type == pygame.QUIT:		
				pygame.quit()
				exit()

		pygame.draw.rect(surface, (0, 0, 0), pygame.Rect((0, 621), (560, 80)))
		text = GAME_FONT.render("LIVES: " + str(player_1.lives) + 50 *
								' '+"SCORE: " + str(player_1.coin_score), True, (255, 0, 255))
		surface.blit(text, (100, 650))

		snd["player_coord"] = player_1.player_coord
		snd["maze"] = maze
		mapobj.show()
		
		
		while True:
			if(sum(snd['t_stat']) >= 3):
				if(snd1['draw'][0][0] != -1):
					draw(snd1['draw'][0], snd1['draw'][1])
				if(snd2['draw'][0][0] != -1):
					draw(snd2['draw'][0], snd2['draw'][1])
				if(snd3['draw'][0][0] != -1):
					draw(snd3['draw'][0], snd3['draw'][1])
				break
			# pygame.time.wait(100)
		if(snd1['draw'][0] == player_1.player_coord 
		or snd2['draw'][0] == player_1.player_coord 
		or snd3['draw'][0] == player_1.player_coord):
		
			if(player_1.lives - 1 > 0):
				player_1.lives -= 1
				maze[player_1.player_coord[1]][player_1.player_coord[0]] = 0
				player_1.player_coord[0] = 13
				player_1.player_coord[1] = 29
				maze[29][13] = 7
				pygame.time.wait(1000)

				continue
			else:
				snd["t_stat"] = [3 for i in range(4)]
				p1.join()
				p2.join()
				p3.join()
				del ghost1
				del ghost2
				del ghost3
				replay=end_window()


		snd1['draw'] = ([-1, -1], (255, 255, 255))
		snd1['clear_draw'] = (-1, -1)
		snd1['draw_coin1'] = (-1, -1)
		snd1['draw_coin2'] = (-1, -1)

		snd2['draw'] = ([-1, -1], (255, 255, 255))
		snd2['clear_draw'] = (-1, -1)
		snd2['draw_coin1'] = (-1, -1)
		snd2['draw_coin2'] = (-1, -1)

		snd3['draw'] = ([-1, -1], (255, 255, 255))
		snd3['clear_draw'] = (-1, -1)
		snd3['draw_coin1'] = (-1, -1)
		snd3['draw_coin2'] = (-1, -1)

		

		pygame.display.flip()
		clock.tick(10)
		snd["t_stat"] = [0 for i in range(4)]
