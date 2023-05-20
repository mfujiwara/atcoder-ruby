N,A,B=gets.chomp.split(" ").map(&:to_i)
array=gets.chomp.split(" ").map(&:to_i)
ret=0
(1..(N-1)).each do |i|
    diff = array[i] - array[i-1]
    if diff * A < B
        ret+=A*diff
    else
        ret+=B
    end
end
puts ret
