#!/usr/bin/env python

import time
import sys
from psychopy import visual,event,core


# 4. Make the square appear for 1.5 secs, then show a blank screen for 1 sec, 
# then flash the square 3 times for 30 ms each.
win = visual.Window([400,400],color="black", units='pix')
squareB = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100])
squareB.draw()
win.flip() # make anything drawn visible
core.wait(1.5)
win.flip()
core.wait(1)

i=0
while i < 3:
	squareB.draw()
	win.flip()
	core.wait(.03)
	win.flip()
	core.wait(.03)
	i = i+1

sys.exit()


# Show the following sequence: blue, red, blue, red, blue, red (with each square appearing for 1 s with a 50 ms blank screen in the middle).

# Show a red square for 1 s then change its orientation by 45-deg