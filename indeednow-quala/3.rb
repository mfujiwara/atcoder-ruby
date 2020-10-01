N=gets.to_i
points=[]
N.times do
    s=gets.to_i
    points.push(s) if s>0
end
points=points.sort
points_r=points.reverse

Q=gets.to_i
Q.times do
    k=gets.to_i
    if points.empty?
        puts "0"
        next
    end
    if points.length <= k
        puts "0"
        next
    end
    out_border=points_r[k]
    puts out_border+1
end
