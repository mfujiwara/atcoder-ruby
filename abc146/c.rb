A,B,X=gets.chomp.split(" ").map(&:to_i)
r = (1..10**9).bsearch{|x| A*x + B*x.to_s.length > X } || 10**9+1
puts r-1
