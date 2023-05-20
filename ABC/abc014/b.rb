N,X=gets.chomp.split(" ").map(&:to_i)
B=X.to_s(2)
array=gets.chomp.split(" ").map(&:to_i)
ret = 0
(0..(B.length-1)).each do |i|
    next if B[i] == "0"
    index = B.length - 1 - i
    ret += array[index]
end
puts ret
