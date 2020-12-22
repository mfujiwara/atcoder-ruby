N=gets.to_i
XY=[]
N.times do
  x,y=gets.chomp.split(" ").map(&:to_i)
  XY.push([x,y])
end
ret=0
XY.combination(3) do |xy1,xy2,xy3|
  x1,y1=xy1
  x2,y2=xy2
  x3,y3=xy3
  double_area = ((x1-x3)*(y2-y3)-(x2-x3)*(y1-y3))
  ret+=1 if double_area.even? && double_area!=0
end
puts ret
