#!/usr/bin/env python3
from maze_map import *
import pygame

class player(maze_map):
	
	SIZE = (10, 10)
	color = (255,0,0)
	lives = 3
	player_colour = (255, 255, 0)
	player_radius = 8

	def __init__(self, player_coord, surface):
		self.player_coord=player_coord
		self.surface = surface
		self.coin_score=0

	def cleardraw(self):
		pygame.draw.rect(self.surface,(0,0,0), pygame.Rect(([self.pixel_size*i for i in self.player_coord]), (self.pixel_size, self.pixel_size))) 

	def draw(self):
		pygame.draw.circle(self.surface, self.player_colour, (self.player_coord[0]*self.pixel_size+(self.pixel_center), self.player_coord[1]*self.pixel_size+(self.pixel_center)), self.player_radius)