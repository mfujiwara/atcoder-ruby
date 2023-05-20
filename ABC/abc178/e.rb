N=gets.to_i
x,y=gets.chomp.split(" ").map(&:to_i)
s1=[x,y]
s2=[x,y]
s3=[x,y]
s4=[x,y]
(N-1).times do
    x,y=gets.chomp.split(" ").map(&:to_i)
    if x+y >= s1[0]+s1[1]
        s1=[x,y]
    end
    if x-y >= s4[0]-s4[1]
        s4=[x,y]
    end
    if x+y <= s3[0]+s3[1]
        s3=[x,y]
    end
    if x-y <= s2[0]-s2[1]
        s2=[x,y]
    end
end
r1 = (s1[0]-s3[0]).abs + (s1[1]-s3[1]).abs
r2 = (s2[0]-s4[0]).abs + (s2[1]-s4[1]).abs
puts r1>r2 ? r1 : r2
