N=gets.to_i
array=gets.chomp.split(" ").map(&:to_i).sort
ret=0
base=0
array.each do |a|
  base+=a
end
ret=0
array.each_with_index do |a,i|
  ret+=(base-a*(N-i))
  base-=a
end
puts ret
