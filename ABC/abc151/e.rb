MOD=10**9+7
N,K=gets.chomp.split(" ").map(&:to_i)
array=gets.chomp.split(" ").map(&:to_i).sort
if K==1
  puts 0
  exit
end

KAIJOU=[1,1]
INVERSE=[1,1]
KAIJOU_INVERSE=[1,1]
(2..(N-1)).each do |i|
  KAIJOU[i] = KAIJOU[i-1] * i % MOD
  INVERSE[i] = MOD - INVERSE[MOD % i] * (MOD / i) % MOD
  KAIJOU_INVERSE[i] = KAIJOU_INVERSE[i-1] * INVERSE[i] % MOD
end
ret=0
(N-K+1).times do |i|
  t = KAIJOU[N-1-i] * KAIJOU_INVERSE[N-K-i] * KAIJOU_INVERSE[K-1] % MOD
  ret += t*array[N-1-i]
  ret -= t*array[i]
  ret%=MOD
end
puts ret
