#!/usr/bin/python3

# my eratosthenes algorithm

def primecalc(limit):
    primes = []
    counter = [True]*(limit)  #to take off the counter for 1, which is not prime
    for i in range(2,limit):
        if counter[i]==False:
            continue
        primes.append(i)
        for f in range(i*i,limit,i):
            counter[f]=False            
    return primes
print (primecalc(1000))