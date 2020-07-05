require 'prime'
N=gets.to_i
MOD=10**9+7
PRIMES = {}
(2..N).each do |i|
    Prime.prime_division(i).each do |n, e|
        PRIMES[n] ||= 0
        PRIMES[n] += e
    end
end
ret = 1
PRIMES.each do |k,v|
    ret *= (v+1)
    ret %= MOD
end
puts ret
