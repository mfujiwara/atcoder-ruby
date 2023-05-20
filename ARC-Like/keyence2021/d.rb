N=gets.to_i
puts [1,3,7,15,31,63,127,255][N-1]
rets = [[0,1]]
(N-1).times do |i|
  nexts = []
  rets.each do |r|
    nexts.push(r+r.dup)
  end
  rets.each do |r|
    rev = r.map{|a| a==0 ? 1 : 0 }
    nexts.push(r+rev)
  end
  nexts.push([0]*2**(i+1) + [1]*2**(i+1))
  rets=nexts
end
rets.each do |r|
  r.each do |a|
    print a==0 ? "A" : "B"
  end
  puts ""
end
