N=gets.to_i
array=gets.chomp.split(" ").map(&:to_i)
ret=[0,0]
COUNT={}
array.each do |a|
  COUNT[a]||=0
  COUNT[a]+=1
  if COUNT[a]==2 || COUNT[a]==4
    if ret[0] < a
      ret.shift
      ret.push(a)
      ret = ret.sort
    end
  end
end
puts ret[0]*ret[1]
