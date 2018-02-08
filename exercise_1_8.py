#!/usr/bin/env python

import time
import sys
from psychopy import visual,event,core


# 8.
win = visual.Window([400,400],color="black", units='pix')
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])

while True:
   square.draw()
   square.ori += 5
   win.flip()
   if event.getKeys(['s']):
       break


sys.exit()

