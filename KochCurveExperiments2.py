import math
import pygame
from pygame.locals import *
import sys

FPS = 1
#Starting length of triangle side
SIDE = 600
#Recursion depth
ORDER_DEPTH = 1
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
		while pass_count < ORDER_DEPTH:
			
			#1st triangle
			
			#load x,y coords of parent triangle. x1, y1 is outward pointing vertex,
			#x2,y2 next clockwise point, x3,y3 last clockwise point.
			px1 = triangles[pass_count][0][0]
			py1 = triangles[pass_count][0][1]
			px2 = triangles[pass_count][1][0]
			py2 = triangles[pass_count][1][1]
			px3 = triangles[pass_count][2][0]
			py3 = triangles[pass_count][2][1]

			pass_count += 1

			'''Find center of parent triangle '''
			centx = (px1 + px2 + px3) / 3
			centy = (py1 + py2 + py3) / 3
			
			'''Find length of line segment from center to any vertex in
			 parent triangle'''
			d = math.sqrt((math.pow((centx - px1), 2)) + (math.pow((centy - py1), 2)))

			'''First child triangle'''
			#First point found relative to vertex 1 of parent triangle
			cx1 = px1 + math.cos(math.radians(90)) * d
			cy1 = py1 + math.sin(math.radians(90)) * 2 * d 	

			'''Need to find line segment on the parent triangle that this child
			triangle 'attaches' to. Should be line drawn between vertices 2 and 3 
			on parent triangle.'''
			side_length = math.sqrt((math.pow((px3 - px2), 2)) + (math.pow((py3 - py2), 2)))

			# cx2 = .666 * px2
			# cy2 = py2

			cx2 = px2 + math.cos(math.radians(180)) * (side_length * .333)
			cy2 = py2 + math.sin(math.radians(180)) * (side_length * .333)

			# cx3 = .333 * px2
			# cy3 = py2

			# cx3 = px2 + math.cos(math.radians(120)) * (side_length * .333)
			# cy3 = py2 + math.sin(math.radians(120)) * (side_length * .333)

			cx3 = px3 - math.cos(math.radians(180)) * (side_length * .333)
			cy3 = py3 + math.sin(math.radians(180)) * (side_length * .333)

			triangles.insert(len(triangles), ((cx1,cy1),(cx2, cy2),(cx3,cy3)))

			pygame.draw.line(window, (0,0,255), (centx, centy), (cx1, cy1))
	
			'''Second child triangle'''
			px2 = triangles[pass_count][0][0]
			py2 = triangles[pass_count][0][1]
			px3 = triangles[pass_count][1][0]
			py3 = triangles[pass_count][1][1]
			px1 = triangles[pass_count][2][0]
			py1 = triangles[pass_count][2][1]
			
			#First point found relative to vertex 1 of parent triangle
			cx1 = px1 + math.cos(math.radians(210)) * d
			cy1 = py1 + math.sin(math.radians(210)) * 2 * d 	

			'''Need to find line segment on the parent triangle that this child
			triangle 'attaches' to. Should be line drawn between vertices 2 and 3 
			on parent triangle.'''
			side_length = math.sqrt((math.pow((px3 - px2), 2)) + (math.pow((py3 - py2), 2)))

			# cx2 = .666 * px2
			# cy2 = py2

			cx2 = px2 + math.cos(math.radians(300)) * (side_length * .333)
			cy2 = py2 + math.sin(math.radians(300)) * (side_length * .333)

			# cx3 = .333 * px2
			# cy3 = py2

			# cx3 = px2 + math.cos(math.radians(120)) * (side_length * .333)
			# cy3 = py2 + math.sin(math.radians(120)) * (side_length * .333)

			cx3 = px3 - math.cos(math.radians(300)) * (side_length * .333)
			cy3 = py3 + math.sin(math.radians(300)) * (side_length * .333)

			triangles.insert(len(triangles), ((cx1,cy1),(cx2, cy2),(cx3,cy3)))

			pygame.draw.line(window, (0,0,255), (centx, centy), (cx1, cy1))

	print('Number of triangles = ' + str(len(triangles)))
	for triangle in triangles:
		print(triangle)
		pygame.draw.lines(window, (255,0,0), True, triangle)

	pygame.display.update()
	fps_time.tick(FPS)