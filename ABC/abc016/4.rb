Ax,Ay,Bx,By=gets.chomp.split(" ").map(&:to_i)
N=gets.to_i
DOTS=[]
N.times do
    x,y=gets.chomp.split(" ").map(&:to_i)
    DOTS.push([x,y])
end
def intersect(p1, p2, p3, p4)
    tc1 = (p1[0] - p2[0]) * (p3[1] - p1[1]) + (p1[1] - p2[1]) * (p1[0] - p3[0])
    tc2 = (p1[0] - p2[0]) * (p4[1] - p1[1]) + (p1[1] - p2[1]) * (p1[0] - p4[0])
    td1 = (p3[0] - p4[0]) * (p1[1] - p3[1]) + (p3[1] - p4[1]) * (p3[0] - p1[0])
    td2 = (p3[0] - p4[0]) * (p2[1] - p3[1]) + (p3[1] - p4[1]) * (p3[0] - p2[0])
    return tc1*tc2<0 && td1*td2<0
end
intersect_count=0
N.times do |i|
    intersect_count+=1 if intersect([Ax,Ay],[Bx,By],DOTS[i],DOTS[i-1])
end
puts intersect_count/2+1
