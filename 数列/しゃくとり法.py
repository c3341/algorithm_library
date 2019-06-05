"""
(しゃくとり法のテンプレート)
right = 0
for left in range(n):
    while(right < n and (rightを１個進めたときに条件を満たす)):
    #実際にrightを1進める
    #(ex.sum += a[right])
    right +=1
    #breakした状態でrightは条件を満たす最大の数なのでなにかする[l,r)
  (ex. ans += right -left)
  if right == left:
   right +=1
  else:
    (ex. sum -= a[left])
"""

#連続する部分列で積がK以下となるもののうち最大の長さをしゃくとり法で求めてみる
N,K = map(int,input().split())
a = []
for i in range(N):
    ai = int(input())
    if ai == 0:
        print(N)
        exit()
    else:
        a.append(ai)
res,right = 0,0
mul = 1
for left in range(N):
    while(right<N and mul*a[right]<=K):
        mul *= a[right]
        right += 1
    res = max(res,right-left)
    if right == left:
        right += 1
    else:
        mul //= a[left]
print(res)
