import time
import random
from multiprocessing import Process


# This does all of our prime factorization on a give number 'n'
def calculatePrimeFactors(n):
    primfac = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
        primfac.append(n)
    return primfac


def executeProc():
    for i in range(1000):
        rand = random.randint(20000, 100000000)
        calculatePrimeFactors(rand)


def main():
    print('201413271 김석우')
    print("Starting number crunching with multiprocessing")
    t0 = time.time()

    procs = []

    for i in range(10):
        proc = Process(target=executeProc, args=())
        procs.append(proc)
        proc.start()

    # we use .join() method in order to wait for
    # execution to finish for all of our processes

    for proc in procs:
        proc.join()

    t1 = time.time()
    totalTime = t1 - t0

    print("Execution Time: {}".format(totalTime))


if __name__ == '__main__':
    main()
