#!/usr/bin/python3

# my eratosthenes algorithm
#progressively eliminate the multiples of the integers starting with 2 up to the limit set in the function call.  Produce a list of the remaining figures.  Use the properties of array as the integer index for efficiency.

def primecalc(limit):
    primes = []
    counter = [True]*(limit)  #initialize an array set to true...then in the loop start removing "trues" where the index of the array is a multiple of the current i 
    for i in range(2,limit):  #to take off the counter for 1, which is not prime
        if counter[i]==False:
            continue
        primes.append(i)
        for f in range(i*i,limit,i):
            counter[f]=False            
    return primes
print (primecalc(1000))