#!/usr/bin/env python

import time
import sys
from psychopy import visual,event,core


# 10. Display a blue square and increase its width (making it a rectangle)
# by 10 pixels whenever the user presses the left-arrow key. 
# Decrease the width by 10 pixels when the user presses the right-arrow key
win = visual.Window([400,400],color="black", units='pix')
square = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100])
square.draw()
win.flip()

while True :
	resp = event.waitKeys()
	if 'left' in resp :
		square.size *= [1.1, 1]
	if 'right' in resp :
		square.size *= [0.9, 1]

	square.draw()
	win.flip()

	if 'x' in resp :
		sys.exit()










