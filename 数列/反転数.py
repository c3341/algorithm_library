#数列aの大小関係が添字と逆になっている組の総数を計算(蟻本p159~)
#計算量は単純に求めるとO(N^2)で、BITだとO(NlogN)
N = int(input())
A = list(map(int,input().split()))
ans = 0
"""
#愚直
for i in range(N):
    for j in range(i+1,N):
        if A[i] > A[j]:
            ans +=1
print(ans)
"""
#BIT
date = [0]*(N+1)
def add(k,x):
    while k <= N:
        date[k] += x
        k += k & -k
def get(k):
    s = 0
    while k:
        s += date[k]
        k -= k & -k
    return s

for i,a in enumerate(A):
    ans += i-get(a)
    add(a,1)
print(ans)
