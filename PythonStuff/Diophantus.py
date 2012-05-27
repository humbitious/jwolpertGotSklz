#loop through 6, 9, 20 piece mcnugget set and get a set of the possible combos
#of course, this is a bit silly above 44, given that as a diophantine equation, it is simply a sequence of all the integers

def nuggets(low,high,small,medium,large):
    if low < 0:
        print "can't go below zero"
    elif high > 400:
            print "can't go too high or you'll never see the end of this...stay below 400"
            #I should put more checks in here for small, medium, large
    else:
        nuggetSet = ()
        for s in range(low,high,small):
            #print l
            nuggetSet = nuggetSet+((s+small),) #get all the iterations of only small
            for m in range(low,high,medium):   #while in the counter for the current value of s
                #print m
                nuggetSet = nuggetSet+((m+medium),)  #get the next value of 0+m+0
                nuggetSet = nuggetSet+(((s+small)+(m+medium)),)   #get the next value of s+m+0
                for l in range(low,high,large):   #while in the counter for the current value of m
                    #print s
                    nuggetSet = nuggetSet+((l+large),)   #get the next value of 0+0+l 
                    nuggetSet = nuggetSet + (((s+small)+(l+large)),)  #get the next value of s+0+l
                    nuggetSet = nuggetSet + (((m+medium)+(l+large)),)  #get the next value of 0+m+l
                    nuggetSet = nuggetSet + (((s+small)+(m+medium)+(l+large)),) #get the next value of s+m+l
        nuggetFinal = sorted(nuggetSet)  #not necessary, but handy for other things
        nuggetUltimate = list(set(nuggetFinal)) #remove all the messy duplicate values caused by this method of looping...very cool that python set can do this...casting the set to a list and removing duplicates automatically 
        print nuggetSet
        print nuggetUltimate
nuggets(0,60,6,9,20)    

