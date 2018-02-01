#!/usr/bin/env python

import time
import sys
from psychopy import visual,event,core


# 3. Show a red square for 1 s, then switch it to blue and show it for 1 s
win = visual.Window([400,400],color="black", units='pix')
squareR = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
squareR.draw()
win.flip() # make anything drawn visible
core.wait(1)
squareB = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100])
squareB.draw()
win.flip()
core.wait(1)

sys.exit()

