#!/usr/bin/env python

import time
import sys
from psychopy import visual,event,core


# 9. Make a square stop rotating when you press 's' 
# and then start rotating again when you press 'r'
win = visual.Window([400,400],color="black", units='pix')
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])



x = 2
def turn(x):
	while x > 1 :
		i = 0
		while i < 361 :
			square.ori += 1
			square.draw()
			win.flip()
			core.wait(1/360)
			i +=1
			if event.getKeys('s') :
				x = 0
				break

turn(2)
if event.waitKeys('r') :
	turn(2)







