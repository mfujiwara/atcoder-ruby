N,K=gets.chomp.split(" ").map(&:to_i)
array=gets.chomp.split(" ").map(&:to_i)
grouped=array.group_by{|x| x}
ret=0
max_num=K
now=0
loop do
  gg = grouped[now]
  break if gg==nil || gg.empty?
  max_num = [gg.length,max_num].min
  ret+=max_num
  now+=1
end
puts ret
