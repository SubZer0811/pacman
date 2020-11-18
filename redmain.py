import pygame
import sys
import random
import threading
import math
import time
import multiprocessing
from maze_map import *
from player import *
# from enemy import *

thread_status = [0, 0, 0, 0]

pygame.init()
pygame.font.init()
surface = pygame.display.set_mode((560,700))


class ghost (maze_map):
	
	def __init__(self,coord,surface,tid,mode="chase",color="red"):
		self.coord=coord
		self.surface=surface
		self.ghost_colour = (0,255,0)
		if(color=="pink"):
			self.ghost_colour=(255,105,180)
		self.ghost_radius = 10
		self.mode=mode
		self.color=color
		self.speedcnt=0
		self.dir=-1
		self.tid = tid

		# self.proc = multiprocessing.Process(target=self.move_ghost, daemon=True)
		# self.thread = threading.Thread(target=self.move_ghost, daemon=True)
		
	def draw(self):
		# global surface
		pygame.draw.circle(surface, self.ghost_colour, (self.coord[0]*self.pixel_size+(self.pixel_center), self.coord[1]*self.pixel_size+(self.pixel_center)), self.ghost_radius)
	
	def cleardraw(self):
		# global surface
		pygame.draw.rect(surface,(0,0,0), pygame.Rect(([self.pixel_size*i for i in self.coord]), (self.pixel_size, self.pixel_size))) 
	
	def draw_coin(self):
		# global surface
		pygame.draw.circle(surface, self.coin_colour, (self.coord[0]*self.pixel_size+(self.pixel_center), self.coord[1]*self.pixel_size+(self.pixel_center)), self.coin_radius)
	
	def move_ghost(self, rcv):
		global surface
		pygame.draw.circle(surface, (0,53,255), (100, 100), 75)
		# global thread_status, player_1
		while True:
			print(self.tid, "proc: ", self.coord)
			pygame.time.wait(100)
			# print(self.tid, ": ", rcv['t_stat'][self.tid])
			t_stat=rcv['t_stat']
			
			# print(self.tid, " ghost: ", self.coord)
			
			if(t_stat[self.tid] == 0):

				self.cleardraw()
				maze=rcv["maze"]
				if(self.speedcnt==0):

					tmp_x = int(self.coord[0])
					tmp_y = int(self.coord[1])

					if(self.color=="red"):
						key_press = self.next_tile(rcv)
					else:
						way_mat = [0, 0, 0, 0]			# left, right, up, down
						if(maze[tmp_y][tmp_x+1] != 1):
							way_mat[0] = 1
						if(maze[tmp_y][tmp_x-1] != 1):
							way_mat[1] = 1
						if(maze[tmp_y-1][tmp_x] != 1):
							way_mat[2] = 1
						if(maze[tmp_y+1][tmp_x] != 1):
							way_mat[3] = 1

						test = []
						for i in range(len(way_mat)):
							if(way_mat[i]):
								test.append(i)
						ind=self.next_tile(rcv)
						key_press = test[ind]
						
					if(maze[tmp_y][tmp_x] == 9):
						self.draw_coin()
						
					if(key_press == 0):
						if(maze[tmp_y][tmp_x+1] != 1):
							# print("ghost-right")
							self.coord[0]+=0.5
							self.dir=0
					elif(key_press == 1):
						if(maze[tmp_y][tmp_x-1]!=1):
							# print("ghost-left")
							self.coord[0]-=0.5
							self.dir=1
					elif(key_press == 2):
						if(maze[tmp_y-1][tmp_x]!=1):
							# print("ghost-up")
							self.coord[1]-=0.5
							self.dir=2
					elif(key_press == 3):
						if(maze[tmp_y+1][tmp_x]!=1):
							# print("ghost-down")
							self.coord[1]+=0.5
							self.dir=3
					
					print(key_press)
					
					self.draw()
					self.speedcnt=1
				else:
					self.cleardraw()
					tf_x = self.coord[0]
					tf_y = self.coord[1]
					tmp_x = int(self.coord[0])
					tmp_y = int(self.coord[1])
					self.coord[0]=tmp_x
					self.coord[1]=tmp_y
					if(maze[tmp_y][tmp_x] == 9):
					 	self.draw_coin()
					if(self.dir==0):
						tf_x+=0.5
						tmp_x+=1
					elif(self.dir==1):
						tf_x-=0.5
						tmp_x+=1
					elif(self.dir==2):
						tf_y-=0.5
						tmp_y+=1
					elif(self.dir==3):
						tf_y+=0.5
						tmp_y+=1

					self.coord[0]=tmp_x
					self.coord[1]=tmp_y
					if(maze[tmp_y][tmp_x] == 9):
						self.draw_coin()
					self.coord[0]=tf_x
					self.coord[1]=tf_y
					self.draw()

					self.speedcnt=0
				t_stat[self.tid] = 1
				rcv["t_stat"]=t_stat
			# pygame.display.update(pygame.Rect((0, 0), (560, 700)))
	
	def next_tile(self,rcv):
		if(self.color=="red"):
			if(self.mode=="chase"):

				# tmp_x=int(self.coord[0])
				# tmp_y=int(self.coord[1])
				
				# play_x=player_1.player_coord[0]
				# play_y=player_1.player_coord[1]
				time = pygame.time.get_ticks()
				s=self.BFS(self.coord,rcv["player_coord"])
				print(pygame.time.get_ticks() - time)
				if(self.coord[0]<s[0]):
					return 0
				elif(self.coord[0]>s[0]):
					return 1
				elif(self.coord[1]<s[1]):
					return 3
				elif(self.coord[1]>s[1]):
					return 2
		if(self.color=="pink"):
			if(self.mode=="chase"):
				#ghostpos
				tmp_x=int(self.coord[0])
				tmp_y=int(self.coord[1])
				play_x=rcv["player_coord"][0]
				play_y=rcv["player_coord"][1]
				# print((play_x, play_y))
				test = []
				if(maze[tmp_y][tmp_x+1] != 1):
					test.append((play_x-tmp_x-1)**2+(play_y-tmp_y)**2)
				if(maze[tmp_y][tmp_x-1] != 1):
					test.append((play_x-tmp_x+1)**2+(play_y-tmp_y)**2)
				if(maze[tmp_y-1][tmp_x] != 1):
					test.append((play_x-tmp_x)**2+(play_y-tmp_y+1)**2)
				if(maze[tmp_y+1][tmp_x] != 1):
					test.append((play_x-tmp_x)**2+(play_y-tmp_y-1)**2)

				return test.index(min(test))

	def BFS(self, start, target):
		start=[int(i) for i in start]
		queue = [start]
		path = []
		visited = []
		while queue:
			current = queue[0]
			queue.remove(queue[0])
			visited.append(current)
			if current == target:
				break
			else:
				neighbours = [[0, -1], [1, 0], [0, 1], [-1, 0]]
				for neighbour in neighbours:
					if neighbour[0]+current[0] >= 0 and neighbour[0] + current[0] < len(maze[0]):
						if neighbour[1]+current[1] >= 0 and neighbour[1] + current[1] < len(maze):
							next_cell = [neighbour[0] + current[0], neighbour[1] + current[1]]
							if next_cell not in visited:
								if maze[next_cell[1]][next_cell[0]] != 1:
									queue.append(next_cell)
									path.append({"Current": current, "Next": next_cell})
		shortest = [target]
		while target != start:
			for step in path:
				if step["Next"] == target:
					target = step["Current"]
					shortest.insert(0, step["Current"])
		return(shortest[1])


mapobj= maze_map(surface)
mapobj.show()

player_1 = player([1, 2], surface)
player_1.draw()

ghost1=ghost([11,13],surface,0)
ghost2=ghost([15,13],surface,1,color="pink")
ghost1.draw()
ghost2.draw()

pygame.display.flip()
clock = pygame.time.Clock()

GAME_FONT = pygame.font.SysFont('Comic Sans MS', 24)

with multiprocessing.Manager() as manager: 
	
	snd = manager.dict()

	snd['t_stat'] = thread_status
	snd['player_coord'] = player_1.player_coord
	snd['maze'] = maze

	p1 = multiprocessing.Process(target=ghost1.move_ghost, args=(snd,)) 
	p2 = multiprocessing.Process(target=ghost2.move_ghost, args=(snd,))

	p1.start()
	p2.start()
	# ghost1.proc.start()
	# ghost2.proc.start()

	while True:
		
		snd["t_stat"]=[0 for i in range(4)]

		keys = pygame.key.get_pressed()

		tmp_x = player_1.player_coord[0]
		tmp_y = player_1.player_coord[1]

		if(ghost1.coord == player_1.player_coord or ghost2.coord == player_1.player_coord):
			print("dead")
			if(player_1.lives - 1 > 0):
				player_1.lives -= 1
				player_1.player_coord[0] = 13; player_1.player_coord[1] = 29
				player_1.draw()
				pygame.time.wait(1000)
				continue
			else:
				exit(0)

		if keys[pygame.K_RIGHT]:
			if(maze[tmp_y][tmp_x+1] == 9 or maze[tmp_y][tmp_x+1] == 0):
				# print("right")
				if(maze[tmp_y][tmp_x+1]==9):
					player_1.coin_score+=1
					maze[tmp_y][tmp_x+1]=0
					# print("Score:",player_1.coin_score)
				player_1.cleardraw()
				player_1.player_coord[0]+=1
				player_1.draw()
		elif keys[pygame.K_LEFT]:
			if(maze[tmp_y][tmp_x-1]==9 or maze[tmp_y][tmp_x-1]==0):
				# print("left")
				if(maze[tmp_y][tmp_x-1]==9):
					player_1.coin_score+=1
					maze[tmp_y][tmp_x-1]=0
					# print("Score:",_.coin_score)
				player_1.cleardraw()
				player_1.player_coord[0]-=1
				player_1.draw()
		elif keys[pygame.K_UP]:
			if(maze[tmp_y-1][tmp_x]==9 or maze[tmp_y-1][tmp_x]==0):
				# print("up")
				if(maze[tmp_y-1][tmp_x]==9):
					player_1.coin_score+=1
					maze[tmp_y-1][tmp_x]=0
					# print("Score:",player_1.coin_score)
				player_1.cleardraw()
				player_1.player_coord[1]-=1
				player_1.draw()
		elif keys[pygame.K_DOWN]:
			if(maze[tmp_y+1][tmp_x]==9 or maze[tmp_y+1][tmp_x]==0):
				# print("down")
				if(maze[tmp_y+1][tmp_x]==9):
					player_1.coin_score+=1
					maze[tmp_y+1][tmp_x]=0
					# print("Score:",player_1.coin_score)
				player_1.cleardraw()
				player_1.player_coord[1]+=1
				player_1.draw()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				print("Quit")
				pygame.quit()
				exit()

		pygame.draw.rect(surface, (0, 0, 0), pygame.Rect((0, 621), (560, 80))) 
		text = GAME_FONT.render("LIVES: "+ str(player_1.lives) +50*' '+"SCORE: " + str(player_1.coin_score), True, (255, 0, 255))
		surface.blit(text, (100, 650))
		
		snd["player_coord"]=player_1.player_coord
		snd["maze"]=maze

		while True:
			# print("main thread: {}" .format(snd['t_stat']))
			# print("sum = ", sum(snd['t_stat']))
			print("main: ", ghost1.coord)
			if(sum(snd['t_stat']) == 2):
				# print(thread_status)
				# print("asdf")
				break
			pygame.time.wait(100)
		
		clock.tick(10)
		
		pygame.display.flip()