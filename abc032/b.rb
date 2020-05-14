s = gets.chomp
k = gets.to_i

set = {}
(0..(s.length-k)).each do |i|
    set[s[i, k]] = "dummy"
end
puts set.size
