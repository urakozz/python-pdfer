__author__ = 'yury'
import time

def primes_sieve(limit):
    limitn = limit+1
    not_prime = [False] * limitn
    primes = []

    for i in xrange(2, limitn):
        if not_prime[i]:
            continue
        for f in xrange(i*2, limitn, i):
            not_prime[f] = True

        primes.append(i)

    return primes

if __name__ == '__main__':
    # n = raw_input("input limit:\n> ")
    # n = int(n)
    t = time.time()
    primes = primes_sieve(9000000)
    print "primes found: %d" % primes.__len__()
    # print "last 3 is: %s" % primes[-3:]
    print "time is %0.04F" % (time.time() - t)