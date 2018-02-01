#!/usr/bin/env python

import time
import sys
from psychopy import visual,event,core


# 7. 
win = visual.Window([400,400],color="black", units='pix')
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])


x = 1
while x < 4: 
	i = 0
	while i < 361 :
		square.ori += 1
		square.draw()
		win.flip()
		core.wait(1/360)
		i +=1




sys.exit()

