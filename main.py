import pygame
import sys
import random
import threading
import math
thread_status = [0, 0, 0, 0]

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


class maze_map:

	pixel_size = 20
	pixel_center = pixel_size/2
	wall_colour = (255,0,0)
	
	coin_colour = (255, 182, 193)
	coin_radius = 4
	
	############################## Player properties ##############################
	player_colour = (255, 255, 0)
	player_radius = 8
	player_coord = []

	############################## Ghost properties ##############################
	

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
			

class player(maze_map):
	
	SIZE = (10, 10)
	color = (255,0,0)
	VELOCITY = 1
	lives = 3

	def __init__(self, player_coord, surface):
		self.player_coord=player_coord
		self.surface = surface
		self.coin_score=0
	def cleardraw(self):
		pygame.draw.rect(self.surface,(0,0,0), pygame.Rect(([self.pixel_size*i for i in self.player_coord]), (self.pixel_size, self.pixel_size))) 

	def draw(self):
		pygame.draw.circle(self.surface, self.player_colour, (self.player_coord[0]*self.pixel_size+(self.pixel_center), self.player_coord[1]*self.pixel_size+(self.pixel_center)), self.player_radius)

class ghost (maze_map):

	def __init__(self,coord,surface,mode="chase",color="red"):
		self.coord=coord
		self.surface=surface
		self.ghost_colour = (0,255,0)
		self.ghost_radius = 10
		self.mode=mode
		self.color=color
		self.speedcnt=0
		self.dir=-1

		self.thread = threading.Thread(target=self.move_ghost, daemon=True)
		
	def draw(self):
		pygame.draw.circle(self.surface, self.ghost_colour, (self.coord[0]*self.pixel_size+(self.pixel_center), self.coord[1]*self.pixel_size+(self.pixel_center)), self.ghost_radius)
	
	def cleardraw(self):
		pygame.draw.rect(self.surface,(0,0,0), pygame.Rect(([self.pixel_size*i for i in self.coord]), (self.pixel_size, self.pixel_size))) 
	
	def draw_coin(self):
		pygame.draw.circle(self.surface, self.coin_colour, (self.coord[0]*self.pixel_size+(self.pixel_center), self.coord[1]*self.pixel_size+(self.pixel_center)), self.coin_radius)
		
	def move_ghost(self):
    	
		# ghost_lock = threading.Lock()
		global thread_status,player_1
		while True:
			
			# print("ghost1 thread: {}" .format(thread_status))
			# play_x=player_1.player_coord[0]
			# play_y=player_1.player_coord[1]
			if(thread_status[0] == 0):
				self.cleardraw()
				if(self.speedcnt==0):
			
					
				
					tmp_x = int(self.coord[0])
					tmp_y = int(self.coord[1])

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
					ind=self.next_tile()
					#key_press = test[random.randint(0,len(test)-1)]
					key_press = test[ind]
					
					if(maze[tmp_y][tmp_x] == 9):
						self.draw_coin()
						
					if(key_press == 0):
						if(maze[tmp_y][tmp_x+1] != 1):
							print("ghost-right")
							self.coord[0]+=0.5
							self.dir=0
						self.draw()
					elif(key_press == 1):
						if(maze[tmp_y][tmp_x-1]!=1):
							print("ghost-left")
							self.coord[0]-=0.5
							self.dir=1
						self.draw()
					elif(key_press == 2):
						if(maze[tmp_y-1][tmp_x]!=1):
							print("ghost-up")
							self.coord[1]-=0.5
							self.dir=2
						self.draw()
					elif(key_press == 3):
						if(maze[tmp_y+1][tmp_x]!=1):
							print("ghost-down")
							self.coord[1]+=0.5
							self.dir=3
						self.draw()
						
					
					self.speedcnt=1
				else:
					tmp_x = int(self.coord[0])
					tmp_y = int(self.coord[1])

					if(maze[tmp_y][tmp_x] == 9):
						self.draw_coin()
					
					if(self.dir==0):
						self.coord[0]+=0.5
						
					elif(self.dir==1):
						self.coord[0]-=0.5
					elif(self.dir==2):
						self.coord[1]-=0.5
					elif(self.dir==3):
						self.coord[1]+=0.5
					
					if(maze[tmp_y][tmp_x] == 9):
						self.draw_coin()
					self.draw()

					self.speedcnt=0
				thread_status[0] = 1
			# pygame.time.wait(1000)
			# ghost_lock.release()
				# pygame.time.wait(100)
	
	def next_tile(self):
		if(self.color=="red"):
			if(self.mode=="chase"):
				#ghostpos
				tmp_x=int(self.coord[0])
				tmp_y=int(self.coord[1])
				global player_1
				play_x=player_1.player_coord[0]
				play_y=player_1.player_coord[1]
				print((play_x, play_y))
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
ghost1.thread.start()

# main_lock = threading.Lock()

while True:
	# print(pygame.time.get_ticks())
	# main_lock.acquire(blocking=True)
	thread_status = [0, 0, 0, 0]
	# main_lock.release()
	keys = pygame.key.get_pressed()

	tmp_x = player_1.player_coord[0]
	tmp_y = player_1.player_coord[1]

	if(ghost1.coord == player_1.player_coord):
		print("dead")
		if(player_1.lives - 1 > 0):
			player_1.lives -= 1
			player_1.player_coord[0] = 13; player_1.player_coord[1] = 29
			player_1.draw()
			pygame.time.wait(1000)
			continue
		else:
			ghost1.thread.join()
			exit(0)

	if keys[pygame.K_RIGHT]:
		if(maze[tmp_y][tmp_x+1]==9 or maze[tmp_y][tmp_x+1]==0):
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
	
	while True:
		# print("main thread: {}" .format(thread_status))
		if(sum(thread_status) == 1):
			# print("asdf")
			break
		# pygame.time.wait(1000)
	
	clock.tick(8)
	
	pygame.display.flip()