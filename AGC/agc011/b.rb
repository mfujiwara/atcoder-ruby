N=gets.to_i
array=gets.chomp.split(" ").map(&:to_i).sort
sum=0
ret = N
array.each_with_index do |a, index|
    if sum*2 < a
        ret = N-index
    end
    sum+=a
end
puts ret
