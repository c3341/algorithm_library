import sys
import os
f = open("C:/Users/kazuki/Documents/python/import.txt","r")
sys.stdin = f
# -*- coding: utf-8 -*-
from itertools import*
from math import*
from collections import*
from heapq import*
from bisect import bisect_left,bisect_right
from copy import deepcopy
inf = float("inf")
mod = 10**9+7
from functools import reduce
import sys
sys.setrecursionlimit(10**7)
N,Q = map(int,input().split())
N0 = 2**(N-1).bit_length()
data = [None]*(2*N0)

def update(l,r,v):
    L = l+N0;R = r+N0
    while L<R:
        if R&1:
            R -= 1
            data[R-1] = v
        if L&1:
            data[L-1] = v
            L += 1
        L >>= 1; R >>= 1
def _query(k):
    k += N0-1
    s = (-1,2**31-1)
    while k >= 0:
        if data[k]:
            s = max(s,data[k])
        k = (k-1)//2
    return s
def query(k):
    return _query(k)[1]
for i in range(Q):
    cmd,*t = map(int,input().split())

    if cmd:
        print(query(t[0]))
    else:
        l,r,v = t
        update(l,r+1,(i,v))
