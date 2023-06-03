#this script was generated with assistence from GPT4
import pygame
import numpy as np

# Pygame setup
WIDTH, HEIGHT = 800, 800
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def draw_mandelbrot(xmin,xmax,ymin,ymax,width,height,max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return (r1,r2,np.array([[mandelbrot(complex(r, i),max_iter) for r in r1] for i in r2]))

def draw(surface, pixels, colormap):
    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            iteration = pixels[i,j]
            color = colormap[iteration % len(colormap)]
            surface.set_at((i, j), pygame.Color(*color, 255))

xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
max_iter = 256

# Define some colors for the Mandelbrot set
colormap = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 255, 255)]

# Draw the Mandelbrot set
x,y,array = draw_mandelbrot(xmin,xmax,ymin,ymax,WIDTH,HEIGHT,max_iter)
mandelbrot_surface = pygame.Surface((WIDTH, HEIGHT))
draw(mandelbrot_surface, array, colormap)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.blit(mandelbrot_surface, (0, 0))
    pygame.display.flip()
