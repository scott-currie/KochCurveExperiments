import math
import pygame
from pygame.locals import *
import sys

FPS = 1
#Starting length of triangle side
SIDE = 600
#Recursion depth
ORDER_DEPTH = 2
#list of tuples representing trios of coordinate pairs
triangles = []

first_triangle = ((SIDE / 2,0), (SIDE,math.tan(math.radians(60)) * (SIDE / 2)), (0,math.tan(math.radians(60)) * (SIDE / 2)))
triangles.append(first_triangle)

print(first_triangle)

pygame.init()
window = pygame.display.set_mode((SIDE + 100, SIDE + 100))
fps_time = pygame.time.Clock()


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	pass_count = 0
	for triangle in triangles:
		while len(triangles) < ORDER_DEPTH:
			x1 = triangles[pass_count][0][0]
			y1 = triangles[pass_count][0][1]
			x2 = triangles[pass_count][1][0]
			y2 = triangles[pass_count][1][1]
			x3 = triangles[pass_count][2][0]
			y3 = triangles[pass_count][2][1]

			cx = (x1 + x2 + x3) / 3
			cy = (y1 + y2 + y3) / 3

			d = math.sqrt((math.pow((cx - x1), 2)) + (math.pow((cy - y1), 2)))

			x4 = x1
			y4 = cy + d	

			x5 = .333 * x2
			y5 = y2

			x6 = .666 * x2
			y6 = y2
			
			triangles.insert(len(triangles), ((x4,y4),(x5,y5),(x6,y6)))
			


			pass_count += 1
			pygame.draw.line(window, (0,0,255), (cx, cy), (x5, y5))
	
	print('Number of triangles = ' + str(len(triangles)))
	for triangle in triangles:
		print(triangle)
		pygame.draw.lines(window, (255,0,0), True, triangle)

	pygame.display.update()
	fps_time.tick(FPS)

