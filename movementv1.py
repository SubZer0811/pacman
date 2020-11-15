import pygame

class player:

	SIZE = (10, 10)
	color = (255,0,0)
	VELOCITY = 10

	def __init__(self, x, y, surface):
		
		self.x = x
		self.y = y
		self.surface = surface
	
	def cleardraw(self):
		pygame.draw.rect(surface,(0,0,0),pygame.Rect((self.x, self.y), self.SIZE))

	def draw(self):

		pygame.draw.rect(surface, self.color, pygame.Rect((self.x, self.y), self.SIZE))


pygame.init()

surface = pygame.display.set_mode((400,300))

player_1 = player(100, 100, surface)
player_1.draw()
pygame.display.flip()
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print("Quit")
			pygame.quit()
			exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				print("right")
				player_1.cleardraw()
				player_1.x+=player_1.VELOCITY
				player_1.draw()
			if event.key == pygame.K_LEFT:
				print("left")
				player_1.cleardraw()
				player_1.x-=player_1.VELOCITY
				player_1.draw()
			if event.key == pygame.K_UP:
				print("up")
				player_1.cleardraw()
				player_1.x+=player_1.VELOCITY
				player_1.draw()
			if event.key == pygame.K_DOWN:
				print("down")
				player_1.cleardraw()
				player_1.x+=player_1.VELOCITY
				player_1.draw()
	pygame.display.flip()