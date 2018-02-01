#!/usr/bin/env python

import time
import sys
from psychopy import visual,event,core


# 5. Show the following sequence: blue, red, blue, red, blue, red 
#(with each square appearing for 1 s with a 50 ms blank screen in the middle).
win = visual.Window([400,400],color="black", units='pix')
squareR = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
squareB = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100])

i=0
while i < 3:
	squareR.draw()
	win.flip()
	core.wait(1)
	win.flip()
	core.wait(.05)
	squareB.draw()
	win.flip()
	core.wait(1)
	i = i+1

sys.exit()

