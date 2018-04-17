#!/usr/bin/env python
####
####  mhp.py -- A Monty Hall simulation.  First runs through and has the
####  contestant never change their guess after being shown a goat.  Then runs
####  again to show the results if the contestant always changes their choice.
####  Theory states that changing to the other door is always avantageous
####  which should be demonstrated in this simulation.
####  Patrick Whitney March 2017
####
####
import mhprand as rnd
import mhpui as ui
import mhputil as util

####  you're the next contestant on Let's make a deal!!
####
passes = ui.getItCount()

#### Our first pass, we're going to have the user never change their original
#### choice.
###  nc == never change
nc_wins = 0
nc_losses = 0
### ac == always change
ac_wins = 0
ac_losses = 0


ui.notifyStart(passes)
for x in xrange(passes):

    doors = rnd.genDoors()
    cchoice = rnd.doorChoice()
    goat = util.showGoat(doors,cchoice)

    if doors[cchoice] == 'C':
        nc_wins = nc_wins + 1
    else:
        nc_losses = nc_losses + 1

    if doors[util.changeChoice(cchoice,goat)] == 'C':
        ac_wins = ac_wins + 1
    else:
        ac_losses = ac_losses + 1


ui.notifyStop(passes,nc_wins,nc_losses,ac_wins,ac_losses)
