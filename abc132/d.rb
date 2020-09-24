N,K=gets.chomp.split(" ").map(&:to_i)
L=N-K
MOD=10**9+7
def ppow(x, n)
    return 1 if n == 0
    return ppow(x**2 % MOD, n / 2) if (n % 2) == 0
    return ppow(x**2 % MOD, n / 2) * x if (n % 2) == 1
end  
def kaijou(a, b)
  	return 1 if a==0
    (b..a).inject(1) {|i,j| i*j % MOD }
end
  
(1..K).each do |i|
    l=kaijou(K-1,K-i+1) * ppow(kaijou(i-1,1), MOD-2)%MOD
    r=kaijou(L+1,L+2-i) * ppow(kaijou(i,1), MOD-2)%MOD
    puts l*r%MOD
end
