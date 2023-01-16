import pygame
import random
from algorithms.bubblesort import bubblesort
from components import is_sorted
from algorithms.bogosort import bogosort
from algorithms.selectionsort import selectionsort

BOGOSORT = "bogosort"
BUBBLESORT = "bubblesort"
SELECTIONSORT = "selectionsort"


sorted = False
RED = (255,0,0)
minNum = 10
maxNum = 60
lengthOfList = 100
numlist = [random.randint(minNum,maxNum) for x in range(lengthOfList)]
index = 0
unsorted_index = 0


list_sorted = False

import sys
 
import pygame
from pygame.locals import *
 
pygame.init()
 
fps = 1000
fpsClock = pygame.time.Clock()
 
width, height = 800, 650
screen = pygame.display.set_mode((width, height))
 
SIZE = 15
startX = (width/2)-(lengthOfList*2)
y = 25
margin = 5

def drawList(listi):
    for ind,num in enumerate(listi):
        p1 = (startX+(margin*ind),y)
        p2 = (startX+(margin*ind),y+(num*SIZE/2))
        if ind != index:
            pygame.draw.line(screen,(255,255,255),p1,p2,width=4)
        else:
            pygame.draw.line(screen,RED,p1,p2,width=4)


algorithm = BUBBLESORT
# Game loop.
while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Draw.
    
    if not sorted:
        if algorithm == "bogosort":
            numlist = bogosort(numlist)
            if is_sorted(numlist):
                sorted = True

        elif algorithm == "bubblesort":
            if index > len(numlist)-2:
                if not is_sorted(numlist):
                    index = 0
                else:
                    sorted = True
            if not sorted:
                numlist = bubblesort(numlist,index)
                index += 1

        elif algorithm == "selectionsort":
            index,numlist = selectionsort(numlist)
            if is_sorted(numlist):
                sorted = True
            

    else:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                pygame.quit()
                sys.exit()


    
    drawList(numlist)

    pygame.display.flip()
    fpsClock.tick(fps)
