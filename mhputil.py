def showGoat(doors,cchoice):
    for x in xrange(0,len(doors)):
        if (x != cchoice) and (doors[x] == 'G'):
            return x

def changeChoice(choice,goat):
    for x in range(0,3):
        if (x != choice) and (x != goat):
            return x


if __name__ == '__main__':

    print "Testing showGoat"


    for cah in xrange(0,3):
        noprizedoor = ['G','G','G']
        tempd = noprizedoor
        tempd[cah] = 'C'
        mydoor = (tempd)
        for choice in xrange(0,3):

            print "cah = %s\t choice = %s" % (cah,choice)
            goat = showGoat(mydoor,choice)
            print "mydoor %s\tgi %s\tdoorv %s\n" % (mydoor,goat,mydoor[goat])

    print "Testing showGoat Complete"

    print "Testing changeChoice"

    for choice in xrange(0,3):
        for goat in xrange(0,3):
            if (choice == goat):
                pass
            else:
                print "choice %s\tgoat %s\tnewchoice %s" % (choice,goat,changeChoice(choice,goat))
