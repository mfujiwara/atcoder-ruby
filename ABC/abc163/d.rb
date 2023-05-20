N,K=gets.chomp.split(" ").map(&:to_i)
MOD=10**9+7
ret=0
(K..(N+1)).each do |k|
    min_sum = k*(k-1)/2
    max_sum = k*(N-k+N+1)/2
    ret += max_sum - min_sum + 1
    ret %= MOD
end
puts ret 
