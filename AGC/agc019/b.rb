A=gets.chomp
n=A.length
ret=n*(n-1)/2+1
A.each_char.group_by{|x|x}.inject(0) do |sum,obj|
  m=obj[1].length
  ret-=m*(m-1)/2
end
puts ret
