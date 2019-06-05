#Nの素因数分解をする計算量はO(√N)
pdic = defaultdict(int)
x = N
y = 2
while y*y<=x:
    while x%y == 0:
        pdic[y] +=1
        x //=y
    y += 1
if x > 1:
    pdic[x] += 1
