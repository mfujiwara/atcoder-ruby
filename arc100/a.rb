N=gets.to_i
array=gets.chomp.split(" ").map.with_index{|n,index| n.to_i-index }.sort
base=array[N/2]
ret=0
array.each do |a|
    ret+=(a-base).abs
end
puts ret
