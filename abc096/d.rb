require 'prime'
primes = Prime.take(225).filter{|n| n%5==1 }
N=gets.to_i
puts primes[0..(N-1)].map(&:to_s).join(" ")
