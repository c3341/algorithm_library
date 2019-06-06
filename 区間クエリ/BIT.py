#BinaryIndexedTree
#i番目の要素の更新、部分和の計算がO(logn)でできる(蟻本p159~)
#a_i,a_i+1,...,a_Nにxを加える,i番目の要素を求めるともみなすことが出来る
class BIT:
    def __init__(self,n):
        self.n = n
        self.data = [0]*(n+1)
        self.el = [0]*(n+1)
    def add(self,i,x):
        self.el[i] += x
        while i <= self.n:
            self.data[i] += x
            i += i & -i
    def sum(self,i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
    def get(self,i,j=None):
        if j is None:
            return self.el[i]
        return self.sum(j)-self.sum(i)

#クラス用いない実装(反転数の項目も参照)
N,Q = map(int,input().split())
data = [0]*(N+1)
def add(k,x):
    while k <= N:
        data[k] += x
        k += k & -k
def get(k):
    s = 0
    while k:
        s += data[k]
        k -= k & -k
    return s

#使用例(概要にある２つ目のデータ構造として使用したとき)
for q in range(Q):
    cmd,*op = map(int,input().split())
    if cmd:
        print(get(op[0]))
    else:
        s,t,x = op
        add(s,x)
        if t < N:
            add(t+1,-x)
