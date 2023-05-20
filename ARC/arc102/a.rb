N,K=gets.chomp.split(" ").map(&:to_i)
ret = 0
# a mod k = 0
ret += (N/K)**3

# a mod k != 0 && 2a mod k = 0
if K.even?
    k=K/2
    ret += ((N+k)/K)**3
end

puts ret
