N=gets.to_i
array=Array.new(1000002,0)
N.times do
    a,b=gets.chomp.split(" ").map(&:to_i)
    array[a]+=1
    array[b+1]-=1
end
ret=0
i=0
array.each do |a|
    i+=a
    ret=i if ret<i
end
puts ret
