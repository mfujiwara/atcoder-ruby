require "prime"

def sum_divisors(n)
  Prime.prime_division(n).map {|p, e| (p ** (e + 1) - 1) / (p - 1) }.inject(:*)
end

N=gets.to_i
ret=sum_divisors(N)-N
if ret==N
    puts "Perfect"
elsif ret<N
    puts "Deficient"
else
    puts "Abundant"
end
