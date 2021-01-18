MOD=10**9+7
def ppow(x, n)
  return 1 if n == 0
  return ppow(x**2 % MOD, n / 2) if (n % 2) == 0
  return ppow(x**2 % MOD, n / 2) * x if (n % 2) == 1
end
def kaijou(a, b)
  (b..a).inject(1) {|i,j| i*j % MOD }
end

N,K=gets.chomp.split(" ").map(&:to_i)
if N>K
  puts kaijou(N+K-1,K+1)*ppow(kaijou(N-1,1),MOD-2) %MOD
  exit
end
q,r=K.divmod(N)
if r==0
  puts 1
  exit
end
puts kaijou(N,N-r+1)*ppow(kaijou(r,1), MOD-2) % MOD
