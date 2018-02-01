#!/usr/bin/env python

import time
import sys
from psychopy import visual,event,core


# 5. Show a red square for 1 s then change its orientation by 45-deg
# To change the orientation by a certain degree-value use square.setOri(value) where `value` is the new orientation.
win = visual.Window([400,400],color="black", units='pix')
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
squareB = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100])



x = 2
while x > 1 :
	i = 0
	b = 360
	while i < 361 :
		square.ori += 1
		square.draw()
		win.flip()
		core.wait(1/360)
		i +=1

		squareB.ori -= 1
		squareB.draw()
		win.flip()
		core.wait(1/360)
		b -=1
		if event.getKeys('s') :
			x = 0
			break





sys.exit()

