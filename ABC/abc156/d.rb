N,A,B=gets.chomp.split(" ").map(&:to_i)
MOD=10**9+7
def ppow(x, n)
    return 1 if n == 0
    return ppow(x**2 % MOD, n / 2) if (n % 2) == 0
    return ppow(x**2 % MOD, n / 2) * x if (n % 2) == 1
end

def kaijou(a, b)
    (b..a).inject(1) {|i,j| i*j % MOD }
end

ret = ppow(2, N)
ret -= 1
ret -= (kaijou(N, N-A+1) * ppow(kaijou(A, 1), MOD-2)) % MOD
ret -= (kaijou(N, N-B+1) * ppow(kaijou(B, 1), MOD-2)) % MOD
ret += MOD*2
puts ret % MOD
