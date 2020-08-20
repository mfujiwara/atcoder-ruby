N,x=gets.chomp.split(" ").map(&:to_i)
array=gets.chomp.split(" ").map(&:to_i)
ret=0
pre=0
array.each do |a|
    diff=pre+a-x
    if diff > 0
        pre = a-diff
        ret+=diff
    else
        pre = a
    end
end
puts ret
