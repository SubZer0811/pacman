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

thread_status = [0, 0, 0, 0]

pygame.init()
pygame.font.init()
surface = pygame.display.set_mode((560,700))
config.surface = surface

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
	
	def move_ghost(self, rcv, ret):
		global surface
		pygame.draw.circle(surface, (0,53,255), (100, 100), 75)
		
		while True:
			print(self.coord)
			pygame.time.wait(100)
		
			t_stat=rcv['t_stat']

			# print("before: ", ret['draw'])
			# ret['draw'] = (self.coord, self.ghost_colour)
			# print("after: ", ret['draw'])
			
			if(t_stat[self.tid] == 0):

				# self.cleardraw()
				# print("save meeeeeee",self.tid,"   ",type(ret["clear_draw"]))
				# print("before in ghost1: ", ret['clear_draw'])
				# ret["clear_draw"] = (0,0)
				# l[0]=(100,100)
				# ret['clear_draw'] = l
				# trcv = rcv['clear_draw']
				# trcv = trcv.append(self.coord)
				# rcv['clear_draw'] = trcv
				# print("after in ghost1: ", ret['clear_draw'])
				
				maze=rcv["maze"]
				if(self.speedcnt==0):

					tmp_x = int(self.coord[0])
					tmp_y = int(self.coord[1])

					ret['clear_draw']=tuple(self.coord)

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
						# self.draw_coin()
						
						ret["draw_coin1"]=(tmp_x, tmp_y)
						
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
					
					# self.draw()
					
					ret["draw"]=(self.coord,self.ghost_colour)
					self.speedcnt=1
				else:
					# self.cleardraw()
					ret['clear_draw']=tuple(self.coord)

					tf_x = self.coord[0]
					tf_y = self.coord[1]
					tmp_x = int(self.coord[0])
					tmp_y = int(self.coord[1])
					self.coord[0]=tmp_x
					self.coord[1]=tmp_y
					if(maze[tmp_y][tmp_x] == 9):
					 	# self.draw_coin()
						ret["draw_coin1"]=(tmp_x, tmp_y)
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
						# self.draw_coin()
						ret["draw_coin2"]=(tmp_x, tmp_y)
					self.coord[0]=tf_x
					self.coord[1]=tf_y
					# self.draw()
					ret["draw"]=(self.coord,self.ghost_colour)
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

draw((ghost1.coord), ghost1.ghost_colour)
draw(ghost2.coord, ghost2.ghost_colour)
# ghost1.draw()
# ghost2.draw()

pygame.display.flip()
clock = pygame.time.Clock()

GAME_FONT = pygame.font.SysFont('Comic Sans MS', 24)

with multiprocessing.Manager() as manager: 
	
	snd = manager.dict()
	snd1 = manager.dict()
	snd2 = manager.dict()

	snd['t_stat'] = thread_status
	snd['player_coord'] = player_1.player_coord
	snd['maze'] = maze
	
	snd1['draw'] = ([-1,-1], (255, 255, 255))
	snd1['clear_draw'] = (-1,-1)
	snd1['draw_coin1'] = (-1,-1)
	snd1['draw_coin2'] = (-1,-1)

	snd2['draw'] = ([-1,-1], (255, 255, 255))
	snd2['clear_draw'] = (-1,-1)
	snd2['draw_coin1'] = (-1,-1)
	snd2['draw_coin2'] = (-1,-1)
	

	p1 = multiprocessing.Process(target=ghost1.move_ghost, args=(snd,snd1))
	p2 = multiprocessing.Process(target=ghost2.move_ghost, args=(snd,snd2))

	p1.start()
	p2.start()
	# ghost1.proc.start()
	# ghost2.proc.start()

	while True:
		

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
			if(sum(snd['t_stat']) == 2):

				print(snd1['clear_draw'])
				print(snd1['draw_coin1'])
				print(snd1['draw_coin2'])
				print(snd1['draw'])
				
				if(snd1['clear_draw'][0] != -1):
					cleardraw(snd1['clear_draw'])
				if(snd2['clear_draw'][0] != -1):
					cleardraw(snd2['clear_draw'])
				
					
				for i in ["draw_coin1", "draw_coin2"]:
					if(snd1[i][0] != -1):
						draw_coin(snd1[i])
					if(snd2[i][0] != -1):
						draw_coin(snd2[i])

						
				if(snd1['draw'][0][0] != -1):
					draw(snd1['draw'][0], snd1['draw'][1])
				if(snd2['draw'][0][0] != -1):
					draw(snd2['draw'][0], snd2['draw'][1])


				snd1['draw'] = ([-1,-1], (255, 255, 255))
				snd1['clear_draw'] = (-1,-1)
				snd1['draw_coin1'] = (-1,-1)
				snd1['draw_coin2'] = (-1,-1)

				snd2['draw'] = ([-1,-1], (255, 255, 255))
				snd2['clear_draw'] = (-1,-1)
				snd2['draw_coin1'] = (-1,-1)
				snd2['draw_coin2'] = (-1,-1)
				
				break
			pygame.time.wait(100)
		
		clock.tick(10)
		
		pygame.display.flip()
		snd["t_stat"]=[0 for i in range(4)]