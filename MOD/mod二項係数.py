#mod=10**9+7における二項係数(階乗およびその逆元)の扱い方

#二項係数とその逆元テーブルを作る前処理
fac = [0]*(Max) #階乗のテーブル
finv = [0]*(Max) #階乗の逆元テーブル
inv = [0]*(Max) #逆元テーブル
fac[0]=fac[1]=1
finv[0]=finv[1]=1
inv[1]=1
for i in range(2,Max):
        fac[i] = fac[i-1] * i % mod
        inv[i] = mod - inv[mod%i]*(mod//i)%mod
        finv[i] = finv[i-1]*inv[i]%mod
#O(1)でmod計算した組合せ数を計算
def Comb(n,r):
    if n < r:
        return 0
    if n < 0 or r < 0 :
        return 0
    return fac[n]*(finv[r]*finv[n-r]%mod)%mod
