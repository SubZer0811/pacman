import pygame



class maze_map:

	def __init__(self, surface):
		
		pixel_size = 20
		pixel_center = pixel_size/2

		maze = open("walls.txt", "r")
		self.color = (255,0,0)
		self.coin_colour = (255, 255, 0)
		self.coin_radius = 6
		line = maze.readline()
		coord = [0, 0]
		while line:
			for i in line:
				# print(i)
				if (i == '1'):
					pygame.draw.rect(surface, self.color, pygame.Rect((coord), (pixel_size, pixel_size))) 
					# print(coord)
				if (i == 'C'):
					pygame.draw.circle(surface, self.coin_colour, (coord[0]+(pixel_center), coord[1]+(pixel_center)), self.coin_radius)
				coord[0] += pixel_size
			coord[1] += pixel_size
			coord[0] = 0
			line = maze.readline()



if __name__ == "__main__":
	

	pygame.init()
	surface = pygame.display.set_mode((560,620))

	test = maze_map(surface)
	pygame.display.flip()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()