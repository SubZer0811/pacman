import pygame

class player:

	SIZE = (10, 10)
	color = (255,0,0)
	VELOCITY = 1

	def __init__(self, x, y, surface):
		
		self.x = x
		self.y = y
		self.surface = surface


	def draw(self):
		pygame.draw.rect(surface, self.color, pygame.Rect((self.x, self.y), self.SIZE)) 

	def play(self):

		while True:
			


if __name__ == "__main__":
	
	pygame.init()

	surface = pygame.display.set_mode((400,300))
	
	player_1 = player(100, 100, surface)
	player_1.draw()
	pygame.display.flip()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()




# # Drawing Rectangle 
# pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60)) 