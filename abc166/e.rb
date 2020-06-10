N=gets.to_i
array=gets.chomp.split(" ").map(&:to_i)
ret=0
hash={}
array.each_with_index do |a,index|
    ret+= hash[a-index] || 0
    b=-a-index
    next if b + N <= 0
    hash[b] ||= 0
    hash[b] += 1
end
puts ret
