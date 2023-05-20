N = gets.to_i
array = gets.chomp.split(" ").map(&:to_i)
sorted = array.sort.reverse
puts (1..N).map {|i| sorted[2*i-1] }.inject(:+)
