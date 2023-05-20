H,W,D=gets.chomp.split(" ").map(&:to_i)
A=[]
MAP=Array.new(H*W,[])
H.times do |h|
    array=gets.chomp.split(" ").map(&:to_i)
    array.each_with_index do |a, w|
        MAP[a-1]=[h,w]
    end
    A.push(array)
end
distances=[0]*D
(D..(H*W-1)).each do |i|
    lc=MAP[i-D]
    rc=MAP[i]
    d=(lc[0]-rc[0]).abs + (lc[1]-rc[1]).abs
    distances[i]=distances[i-D]+d
end

Q=gets.to_i
Q.times do
    l,r=gets.chomp.split(" ").map(&:to_i)
    puts distances[r-1]-distances[l-1]
end
