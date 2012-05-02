#!/usr/bin/python3

# my eratosthenes algorithm

def primecalc(limit):
    primes = []  #create the holding array - could have used set - to hold the primes
    counter = [True]*(limit)  #create an array of booleans set to True...this works by matching i in loop to array position
    for i in range(2,limit):
        if counter[i]==False:
            continue
        primes.append(i)
        for f in range(i*i,limit,i):  #this will find each successive multiple of i and set that position to false
            counter[f]=False
print (primecalc (1000))