#a_iの値を更新、a_i,..,a_r-1の最小値をそれぞれO(logN)で求められる
N,Q = map(int,input().split())
N0 = 2**(N-1).bit_length()
data = [2**31-1]*(2*N0)

def update(k,x):
    k += N0-1
    data[k] = x
    while k >= 0:
        k = (k-1)//2
        data[k]=min(data[2*k+1],data[2*k+2])
def query(l,r):
    L = l + N0
    R = r + N0
    s = 2**31-1
    while L<R:
        if R&1:
            R -=1
            s = min(s,data[R-1])

        if L&1:
            s = min(s,data[L-1])
            L += 1
        L>>=1;R>>=1
    return s

#使い方(AOJ-RangeMinimumQuery)
for q in range(Q):
    com,x,y = map(int,input().split())
    if com:
        print(query(x,y+1))
    else:
        update(x,y)
