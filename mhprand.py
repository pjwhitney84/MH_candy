#!/usr/bin/env python
from random import randint,sample

def genDoors():
    doors = ['G','G','G']
    doors[randint(1,3)-1] = 'C'
    return tuple(doors)

def doorChoice():
    return randint(1,3) - 1


if __name__ == "__main__":

    print "Testing setDoors..."
    counter = {}
    for x in xrange(0,19):
        doors = genDoors()
        if doors in counter.keys():
            counter[doors] = counter[doors] + 1
        else:
            counter[doors] = 1

        print doors

    print "\n%s" % counter
    print "Testing setDoors Complete."

    print "Testing doorChoice"
    for x in xrange(0,19):
         print doorChoice()

    print "Testing doorChoice Complete"
