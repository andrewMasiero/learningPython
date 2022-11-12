'''
Homegrown timing tools for function calls.
Does total time, best-of time, and best-of-totals time
'''

import time
import sys
timer = time.perf_counter


def total(reps, func, *pargs, **kargs):
    '''
    total time to run func() reps times.
    Returns (total time, last result)
    '''
    repslist = list(range(reps))
    start = timer()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = timer() - start

    # print(f'Total: {elapsed}')
    return (elapsed, ret)


def bestof(reps, func, *pargs, **kargs):
    '''
    Quickest func() among reps runs.
    Returns (best time, last result)
    '''
    best = 2 ** 32
    for i in range(reps):
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        if elapsed < best:
            best = elapsed
    # print(f'Best of: {best}')
    return (best, ret)


def bestoftotal(reps1, reps2, func, *pargs, **kargs):
    # timer.bestoftotal(50, 1000, str.upper, spam)
    '''
    Best of total:
    (best of reps1 runs of (total of reps2 runs of func))
    '''
    b = bestof(reps1, total, reps2, func, *pargs, **kargs)
    # print(f'Best of total: {b}')
    return b
