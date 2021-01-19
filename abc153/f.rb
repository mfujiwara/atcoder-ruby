N,D,A=gets.chomp.split(" ").map(&:to_i)
min_x=10**9
max_x=0
max_h=0
monsters=[]
N.times do
  x,h=gets.chomp.split(" ").map(&:to_i)
  monsters.push([x,h])
  min_x=x if min_x>x
  max_x=x if max_x<x
  max_h=h if max_h<h
end
monsters=monsters.sort_by{|x,h| x }
out_of_d=monsters.map do |x,h|
  monsters.bsearch_index{|bx,bh| x+2*D<bx } || N
end

ret=0
damage=0
damages=Array.new(N+1,0)
monsters.each_with_index do |monster,i|
  x,h=monster
  damage+=damages[i]
  h-=damage
  if h>0
    n=(h+A-1)/A
    ret+=n
    damage+=A*n
    damages[out_of_d[i]]-=A*n
  end
end
puts ret
