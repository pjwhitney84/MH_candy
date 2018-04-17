#!/usr/bin/env python
### proposeInteractive -- ask user if they would like to run the simulation
### interactively.
def proposeInteractive():
    msg = "Would you like to run the simulation interactively? (Y or N)\n"

    while True:
        try:
            answer = raw_input(msg)
        except:
            pass

        if ( not ( (answer == 'Y') or
                   (answer == 'y') or
                   (answer == 'N') or
                   (answer == 'n') )):
            print "Please enter 'Y' for 'Yes' or 'N' for 'No'..."
        else:
            if (answer == 'Y' or answer == 'y'):
                return True
            else:
                return False

### getItCount -- Prompt user for nuber of iterations to run in each simulation.
def getItCount():
    itCount = 0
    while True:

            prmt = "Number of times to run test (1-500000): "
            try:
                itCount = int(raw_input(prmt))
            except ValueError:
                pass

            if  ( (not isinstance(itCount, int)) or
                  (itCount < 1) or
                  (itCount > 500000) ):
                print "Invalid input, plese try again..."
            else:
                return itCount

### notifyStart -- print msg to notify user of the start of the
### simulation.
def notifyStart(passes):
    print "Starting simulation: %s iterations" % passes

def notifyStop(passes,ncwins,ncloss,acwins,acloss):
    print "Simulation complete"
    print "After %s iterations:" % passes
    print "\t... if we NEVER change our choice"
    print "\t\tWins: %s" % ncwins
    print "\t\tLosses: %s" % ncloss
    print "\t\tWin ratio: %.2f%%\n" % (float(ncwins*100)/passes)
    print "\t... if we ALWAYS change our choice"
    print "\t\tWins: %s: " % acwins
    print "\t\tLosses: %s" % acloss
    print "\t\tWin ratio: %.2f%%\n" % (float(acwins*100)/passes)

if __name__ == "__main__":
    print "Did you want to run Interactively: %s" % str(proposeInteractive())
    print "you entered: %i" % getItCount()
    notifyStart(100)
    notifyStop(100,33,66,66,33)
