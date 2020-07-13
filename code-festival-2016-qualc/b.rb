K,T=gets.chomp.split(" ").map(&:to_i)
array=gets.chomp.split(" ").map(&:to_i)
a_max = array.max
ret = a_max*2-K-1
if ret > 0
    puts ret
else
    puts 0
end
