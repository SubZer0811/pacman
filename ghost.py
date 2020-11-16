from maze import *
import random

class ghost (maze_map):

	def __init__(self,coord,surface):
		self.coord=coord
		self.surface=surface
		self.ghost_colour = (0,255,0)
		self.ghost_radius = 10
		
	def draw(self):
		pygame.draw.circle(self.surface, self.ghost1_colour, (self.coord[0]*self.pixel_size+(self.pixel_center), self.coord[1]*self.pixel_size+(self.pixel_center)), self.ghost1_radius)
	
	def cleardraw(self):
		pygame.draw.rect(self.surface,(0,0,0), pygame.Rect(([self.pixel_size*i for i in self.coord]), (self.pixel_size, self.pixel_size))) 
	
	def draw_coin(self):
		pygame.draw.circle(self.surface, self.coin_colour, (self.coord[0]*self.pixel_size+(self.pixel_center), self.coord[1]*self.pixel_size+(self.pixel_center)), self.coin_radius)
		
	def move_ghost(self):
    		
		self.cleardraw()
		tmp_x = self.coord[0]
		tmp_y = self.coord[1]

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

		key_press = test[random.randint(0,len(test)-1)]
		
		if(maze[tmp_y][tmp_x] == 9):
			self.draw_coin()
			
		if(key_press == 0):
			if(maze[tmp_y][tmp_x+1] != 1):
				print("ghost-right")
				self.coord[0]+=1
			self.draw()
		elif(key_press == 1):
			if(maze[tmp_y][tmp_x-1]!=1):
				print("ghost-left")
				self.coord[0]-=1
			self.draw()
		elif(key_press == 2):
			if(maze[tmp_y-1][tmp_x]!=1):
				print("ghost-up")
				self.coord[1]-=1
			self.draw()
		elif(key_press == 3):
			if(maze[tmp_y+1][tmp_x]!=1):
				print("ghost-down")
				self.coord[1]+=1
			self.draw()