#mod=10**9+7における逆元および分数の扱い方
#逆元テーブル
inv = [0]*(Max)
inv[1]=1
for i in range(2,Max):
        inv[i] = mod - inv[mod%i]*(mod//i)%mod
#modの世界での有理数の持ち方(a = A over B)
a = A*inv[B] % mod

#a^n modの計算
pow(a,n,mod)
#a^(-1)modの計算(フェルマーの小定理)
pow(a,mod-2,mod)

#掛け算、足し算、引き算は一回行うたびにmodを取るのが無難
