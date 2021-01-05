N=gets.to_i
k = ((N*2)**(0.5)).floor + 1
if k*(k-1)/2 != N
  puts "No"
  exit
end
puts "Yes"
puts k
rets=Array.new(k){[]}
c=1
(1..k).to_a.combination(2) do |a,b|
  rets[a-1].push(c)
  rets[b-1].push(c)
  c+=1
end
rets.each do |ret|
  print k-1
  print " "
  puts ret.join(" ")
end
