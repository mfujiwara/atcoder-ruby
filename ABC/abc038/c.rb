N=gets.to_i
array=gets.chomp.split(" ").map(&:to_i)
pre=10**5
c=0
ret=0
(0..(N-1)).each do |i|
    if array[i] > pre
        c+=1
    else
        c=1
    end
    ret+=c
    pre = array[i]
end
puts ret
