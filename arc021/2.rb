L=gets.to_i
ret=[0]
L.times do 
  b=gets.to_i
  a=b^ret[-1]
  ret.push(a)
end
if ret[-1] != 0
  puts "-1"
else
  ret.pop
  ret.each {|r| puts r}
end
