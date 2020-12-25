require 'prime'
N=gets.to_i
PRIMES={}
(1..N).each do |n|
  Prime.prime_division(n).each do |nn, e|
    PRIMES[nn]||=0
    PRIMES[nn]+=e
  end
end
# 75 = 3 * 5 * 5
ret=0
PRIMES.values.each do |a|
  ret+=1 if a>=74
end
PRIMES.values.combination(2) do |a,b|
  ret+=1 if a>=2 && b>=24
  ret+=1 if a>=4 && b>=14
  ret+=1 if a>=14 && b>=4
  ret+=1 if a>=24 && b>=2
end
PRIMES.values.combination(3) do |a,b,c|
  ret+=1 if a>=2 && b>=4 && c>=4
  ret+=1 if a>=4 && b>=2 && c>=4
  ret+=1 if a>=4 && b>=4 && c>=2
end
puts ret
