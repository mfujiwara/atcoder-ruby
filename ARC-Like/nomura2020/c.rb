N=gets.to_i
def min(a,b)
  return a<b ? a : b
end
array=gets.chomp.split(" ").map(&:to_i)
leaf_rest=array.inject(&:+)
node_count=1
ret=1
array.each_with_index do |a,i|
  if a > node_count
    puts "-1"
    exit
  end
  leaf_rest-=a
  node_count-=a
  node_count=min(node_count*2, leaf_rest)
  ret+=node_count
end
puts ret
