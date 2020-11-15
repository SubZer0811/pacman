import pygame
import sys
import random
maze = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
	[1,9,9,9,9,9,9,9,9,9,9,9,9,1,1,9,9,9,9,9,9,9,9,9,9,9,9,1],
	[1,9,1,1,1,1,9,1,1,1,1,1,9,1,1,9,1,1,1,1,1,9,1,1,1,1,9,1],
	[1,9,1,1,1,1,9,1,1,1,1,1,9,1,1,9,1,1,1,1,1,9,1,1,1,1,9,1],
	[1,9,1,1,1,1,9,1,1,1,1,1,9,1,1,9,1,1,1,1,1,9,1,1,1,1,9,1],
	[1,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,1],
	[1,9,1,1,1,1,9,1,1,9,1,1,1,1,1,1,1,1,9,1,1,9,1,1,1,1,9,1],
	[1,9,1,1,1,1,9,1,1,9,1,1,1,1,1,1,1,1,9,1,1,9,1,1,1,1,9,1],
	[1,9,9,9,9,9,9,1,1,9,9,9,9,1,1,9,9,9,9,1,1,9,9,9,9,9,9,1],
	[1,1,1,1,1,1,9,1,1,1,1,1,9,1,1,9,1,1,1,1,1,9,1,1,1,1,1,1],
	[1,1,1,1,1,1,9,1,1,1,1,1,9,1,1,9,1,1,1,1,1,9,1,1,1,1,1,1],
	[1,1,1,1,1,1,9,1,1,9,9,9,9,9,9,9,9,9,9,1,1,9,1,1,1,1,1,1],
	[1,1,1,1,1,1,9,1,1,9,1,1,1,0,0,1,1,1,9,1,1,9,1,1,1,1,1,1],
	[1,1,1,1,1,1,9,1,1,9,1,0,0,0,0,0,0,1,9,1,1,9,1,1,1,1,1,1],
	[1,1,1,1,1,1,9,9,9,9,1,0,0,0,0,0,0,1,9,9,9,9,1,1,1,1,1,1],
	[1,1,1,1,1,1,9,1,1,9,1,0,0,0,0,0,0,1,9,1,1,9,1,1,1,1,1,1],
	[1,1,1,1,1,1,9,1,1,9,1,1,1,1,1,1,1,1,9,1,1,9,1,1,1,1,1,1],
	[1,1,1,1,1,1,9,1,1,9,9,9,9,9,9,9,9,9,9,1,1,9,1,1,1,1,1,1],
	[1,1,1,1,1,1,9,1,1,9,1,1,1,1,1,1,1,1,9,1,1,9,1,1,1,1,1,1],
	[1,1,1,1,1,1,9,1,1,9,1,1,1,1,1,1,1,1,9,1,1,9,1,1,1,1,1,1],
	[1,9,9,9,9,9,9,9,9,9,9,9,9,1,1,9,9,9,9,9,9,9,9,9,9,9,9,1],
	[1,9,1,1,1,1,9,1,1,1,1,1,9,1,1,9,1,1,1,1,1,9,1,1,1,1,9,1],
	[1,9,1,1,1,1,9,1,1,1,1,1,9,1,1,9,1,1,1,1,1,9,1,1,1,1,9,1],
	[1,9,9,9,1,1,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,1,1,9,9,9,1],
	[1,1,1,9,1,1,9,1,1,9,1,1,1,1,1,1,1,1,9,1,1,9,1,1,9,1,1,1],
	[1,1,1,9,1,1,9,1,1,9,1,1,1,1,1,1,1,1,9,1,1,9,1,1,9,1,1,1],
	[1,9,9,9,9,9,9,1,1,9,9,9,9,1,1,9,9,9,9,1,1,9,9,9,9,9,9,1],
	[1,9,1,1,1,1,1,1,1,1,1,1,9,1,1,9,1,1,1,1,1,1,1,1,1,1,9,1],
	[1,9,1,1,1,1,1,1,1,1,1,1,9,1,1,9,1,1,1,1,1,1,1,1,1,1,9,1],
	[1,9,9,9,9,9,9,9,9,9,9,9,9,0,0,9,9,9,9,9,9,9,9,9,9,9,9,1],
	[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

coin_score=0

class maze_map:

	pixel_size = 20
	pixel_center = pixel_size/2
	wall_colour = (255,0,0)
	coin_colour = (255, 182, 193)
	coin_radius = 4
	player_colour = (255, 255, 0)
	player_radius = 8

	def __init__(self, surface):
		
		self.surface = surface


	def show(self):
		coord = [0, 0]
		for j in maze:
			for i in j:
				if (i == 1):
					pygame.draw.rect(self.surface, self.wall_colour, pygame.Rect((coord), (self.pixel_size, self.pixel_size))) 
				if (i == 9):
					pygame.draw.circle(self.surface, self.coin_colour, (coord[0]+(self.pixel_center), coord[1]+(self.pixel_center)), self.coin_radius)
				coord[0] += self.pixel_size
			coord[1] += self.pixel_size
			coord[0] = 0


class ghost ():
	pixel_size = 20
	pixel_center = pixel_size/2
	coin_colour = (255, 182, 193)
	coin_radius = 4
	def __init__(self,coord,surface):

		
		self.coord=coord
		self.surface=surface
		self.ghost_colour=(0,255,0)
		self.ghost_radius=10
	
	
		
	def draw(self):
		pygame.draw.circle(self.surface, self.ghost_colour, (self.coord[0]*self.pixel_size+(self.pixel_center), self.coord[1]*self.pixel_size+(self.pixel_center)), self.ghost_radius)
	
	def cleardraw(self):
		pygame.draw.rect(self.surface,(0,0,0), pygame.Rect(([self.pixel_size*i for i in self.coord]), (self.pixel_size, self.pixel_size))) 
	
	def draw_coin(self):
		pygame.draw.circle(self.surface, self.coin_colour, (self.coord[0]*self.pixel_size+(self.pixel_center), self.coord[1]*self.pixel_size+(self.pixel_center)), self.coin_radius)
		print("coin")
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
		print("test: ", test)
		key_press = random.randint(0,len(test)-1)
		print(key_press)
		key_press = test[key_press]
		if(maze[tmp_y][tmp_x] == 9):
			self.draw_coin()
			print("call-coin")
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
		
		
			


class player(maze_map):
	
	SIZE = (10, 10)
	color = (255,0,0)
	VELOCITY = 1

	def __init__(self,coord, surface):
		
		self.coord=coord
		self.surface = surface
	
	def cleardraw(self):
		pygame.draw.rect(self.surface,(0,0,0), pygame.Rect(([self.pixel_size*i for i in self.coord]), (self.pixel_size, self.pixel_size))) 

	def draw(self):
		pygame.draw.circle(self.surface, self.player_colour, (self.coord[0]*self.pixel_size+(self.pixel_center), self.coord[1]*self.pixel_size+(self.pixel_center)), self.player_radius)


pygame.init()
surface = pygame.display.set_mode((560,620))

player_1 = player([13, 29], surface)
player_1.draw()

mapobj= maze_map(surface)
mapobj.show()

ghost=ghost([11,13],surface)

pygame.display.flip()

clock = pygame.time.Clock()

while True:
	ghost.move_ghost()
	keys = pygame.key.get_pressed()

	# if event.type == pygame.KEYDOWN:
	tmp_x=player_1.coord[0]
	tmp_y=player_1.coord[1]
	if keys[pygame.K_RIGHT]:
		if(maze[tmp_y][tmp_x+1]==9 or maze[tmp_y][tmp_x+1]==0):
			print("right")
			if(maze[tmp_y][tmp_x+1]==9):
				coin_score+=1
				maze[tmp_y][tmp_x+1]=0
				print("Score:",coin_score)
			player_1.cleardraw()
			player_1.coord[0]+=1
			player_1.draw()
	elif keys[pygame.K_LEFT]:
		if(maze[tmp_y][tmp_x-1]==9 or maze[tmp_y][tmp_x-1]==0):
			print("left")
			if(maze[tmp_y][tmp_x-1]==9):
				coin_score+=1
				maze[tmp_y][tmp_x-1]=0
				print("Score:",coin_score)
			player_1.cleardraw()
			player_1.coord[0]-=1
			player_1.draw()
	elif keys[pygame.K_UP]:
		if(maze[tmp_y-1][tmp_x]==9 or maze[tmp_y-1][tmp_x]==0):
			print("up")
			if(maze[tmp_y-1][tmp_x]==9):
				coin_score+=1
				maze[tmp_y-1][tmp_x]=0
				print("Score:",coin_score)
			player_1.cleardraw()
			player_1.coord[1]-=1
			player_1.draw()
	elif keys[pygame.K_DOWN]:
		if(maze[tmp_y+1][tmp_x]==9 or maze[tmp_y+1][tmp_x]==0):
			print("down")
			if(maze[tmp_y+1][tmp_x]==9):
				coin_score+=1
				maze[tmp_y+1][tmp_x]=0
				print("Score:",coin_score)
			player_1.cleardraw()
			player_1.coord[1]+=1
			player_1.draw()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print("Quit")
			pygame.quit()
			exit()

	clock.tick(8)
	pygame.display.flip()