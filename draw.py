import pygame
import config

ghost_radius = 10
pixel_size = 20
pixel_center = pixel_size/2
coin_colour = (255, 182, 193)
coin_radius = 4


def draw(coord, ghost_colour):
	print("draw: ",coord)
	pygame.draw.circle(config.surface, ghost_colour, (coord[0]*pixel_size+(pixel_center), coord[1]*pixel_size+(pixel_center)), ghost_radius)
	
def cleardraw(coord):
	pygame.draw.rect(config.surface,(0,0,0), pygame.Rect(([pixel_size*i for i in coord]), (pixel_size, pixel_size))) 

def draw_coin(coord):
	pygame.draw.circle(config.surface, coin_colour, (coord[0]*pixel_size+(pixel_center), coord[1]*pixel_size+(pixel_center)), coin_radius)