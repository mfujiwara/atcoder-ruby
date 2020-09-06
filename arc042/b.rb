X,Y=gets.chomp.split(" ").map(&:to_i)
N=gets.to_i
ts=[]
N.times do
    x,y=gets.chomp.split(" ").map(&:to_i)
    ts.push([x,y])
end
ret=200
N.times do |i|
    x1,y1=ts[i]
    x2,y2=ts[(i+1)%N]
    a=y2-y1
    b=x1-x2
    c=(x2-x1)*y1-(y2-y1)*x1
    d=(a*X+b*Y+c).abs/(a**2+b**2)**(0.5)
    ret=d if d < ret
end
puts ret
