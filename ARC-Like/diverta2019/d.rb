require 'prime'

def _divisors(primes, k)
  Enumerator.new do |y|
    if primes.size == k
      y << 1
    else
      p, e = primes[k]
      _divisors(primes, k + 1).each {|d|
        (e + 1).times {|e1|
          y << p ** e1 * d
        }
      }
    end
  end
end

def divisors(n)
  _divisors(Prime.prime_division(n), 0).to_a
end

N=gets.chomp.to_i
ret=0
divisors(N).each do |d|
    r=d-1
    next if r==0
    ret+=r if N/r==N%r
end
puts ret
