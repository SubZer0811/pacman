import pygame
import config
import os
ghost_radius = 10
pixel_size = 20
pixel_center = pixel_size/2
coin_colour = (255, 182, 193)
coin_radius = 4


def draw(coord, ghost_colour):
	pygame.draw.circle(config.surface, ghost_colour, (coord[0]*pixel_size+(pixel_center), coord[1]*pixel_size+(pixel_center)), ghost_radius)
	
def cleardraw(coord):
	pygame.draw.rect(config.surface,(0,0,0), pygame.Rect(([pixel_size*i for i in coord]), (pixel_size, pixel_size))) 

def draw_coin(coord):
	pygame.draw.circle(config.surface, coin_colour, (coord[0]*pixel_size+(pixel_center), coord[1]*pixel_size+(pixel_center)), coin_radius)

def draw_text(words, screen, pos, size, colour, font_name, centered=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        if centered:
            pos[0] = pos[0]-text_size[0]//2
            pos[1] = pos[1]-text_size[1]//2
        screen.blit(text, pos)
	
	
def end_window():
	config.surface.fill((0, 0, 0))
	
	image = pygame.image.load(r'game_over.jpg') 
	config.surface.blit(image, (100, 0)) 

	pygame.display.update()

	quit_text = "Press the ESCAPE to quit"
	again_text = "Press SPACE to play with again"
	draw_text(again_text, config.surface, [
					config.WIDTH//2, config.HEIGHT//2+100],  36, (190, 190, 190), 'Comic Sans MS', centered=True)
	draw_text(quit_text, config.surface, [
					config.WIDTH//2, config.HEIGHT//2 + 200],  36, (190, 190, 190), 'Comic Sans MS', centered=True)
	pygame.display.update()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				pygame.quit()
				os.system('python3 main.py')
				exit(0)
			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				exit(0)
			if event.type == pygame.QUIT:
				exit(0)
			pygame.display.update()

