import pygame
import random
from maze_map import *

class ghost (maze_map):
	
	def __init__(self,coord,surface,tid,color):
		self.coord=coord
		self.surface=surface
		self.dir=-1
		if(color == "red"):
			self.ghost_colour = (255,0,0)
		elif(color=="pink"):
			self.ghost_colour=(255,105,180)
		elif(color == "yellow"):
			self.dir=2
			self.ghost_colour=(255,255,0)
		self.ghost_radius = 10
		self.mode="chase"
		self.color=color
		self.speedcnt=0	
		self.tid = tid

	def move_ghost(self, rcv, ret):
		
		while True:
			pygame.time.wait(100)
			t_stat=rcv['t_stat']

			if(t_stat[self.tid] == 3):
				return

			if(t_stat[self.tid] == 0):
				maze=rcv["maze"]
				if(self.speedcnt==0):
					tmp_x = int(self.coord[0])
					tmp_y = int(self.coord[1])

					ret['clear_draw']=tuple(self.coord)

					if(self.color=="red"):
						key_press = self.move_red(rcv)
					elif(self.color == 'pink'):
						key_press = self.move_pink(rcv)
					elif(self.color == 'yellow'):
						key_press = self.move_yellow(rcv)

					if(key_press==-1):
						continue
					if(maze[tmp_y][tmp_x] == 9):
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

					ret["draw"]=(self.coord,self.ghost_colour)
					self.speedcnt=1
				else:
					ret['clear_draw']=tuple(self.coord)

					tf_x = self.coord[0]
					tf_y = self.coord[1]
					tmp_x = int(self.coord[0])
					tmp_y = int(self.coord[1])
					self.coord[0]=tmp_x
					self.coord[1]=tmp_y
					if(maze[tmp_y][tmp_x] == 9):
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
						ret["draw_coin2"]=(tmp_x, tmp_y)
					self.coord[0]=tf_x
					self.coord[1]=tf_y
					ret["draw"]=(self.coord,self.ghost_colour)
					self.speedcnt=0
				t_stat[self.tid] = 1
				rcv["t_stat"]=t_stat

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
		if(len(shortest)>1):
			return(shortest[1])
		return -1


	def move_red(self, rcv):

		s = self.BFS(self.coord,rcv["player_coord"])
		if(s == -1):
			return -1
		if(self.coord[0]<s[0]):
			return 0
		elif(self.coord[0]>s[0]):
			return 1
		elif(self.coord[1]<s[1]):
			return 3
		elif(self.coord[1]>s[1]):
			return 2

	def move_pink(self, rcv):

		tmp_x=int(self.coord[0])
		tmp_y=int(self.coord[1])
		play_x=rcv["player_coord"][0]
		play_y=rcv["player_coord"][1]
		test = []
		w=[]
		if(maze[tmp_y][tmp_x+1] != 1):
			test.append((play_x-tmp_x-1)**2+(play_y-tmp_y)**2)
			w.append(0)
		if(maze[tmp_y][tmp_x-1] != 1):
			test.append((play_x-tmp_x+1)**2+(play_y-tmp_y)**2)
			w.append(1)
		if(maze[tmp_y-1][tmp_x] != 1):
			test.append((play_x-tmp_x)**2+(play_y-tmp_y+1)**2)
			w.append(2)
		if(maze[tmp_y+1][tmp_x] != 1):
			test.append((play_x-tmp_x)**2+(play_y-tmp_y-1)**2)
			w.append(3)

		if(play_x==tmp_x and tmp_y==play_y):
			return -1
		return w[test.index(min(test))]

	def move_yellow(self, rcv):

		tmp_x=int(self.coord[0])
		tmp_y=int(self.coord[1])
		test = []		# right, left, up, down
		if(maze[tmp_y][tmp_x+1] != 1):
			test.append(0)
		if(maze[tmp_y][tmp_x-1] != 1):
			test.append(1)
		if(maze[tmp_y-1][tmp_x] != 1):
			test.append(2)
		if(maze[tmp_y+1][tmp_x] != 1):
			test.append(3)

		print("test: ", test)
		if(self.dir in test):
			return self.dir
		return random.choice(test)