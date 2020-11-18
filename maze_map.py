import pygame

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