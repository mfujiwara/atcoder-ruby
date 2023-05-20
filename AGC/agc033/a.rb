H,W=gets.chomp.split(" ").map(&:to_i)
MAP=[]
fronts=[]
H.times do |i|
    array=gets.chomp.split("").map{|a| a=="." }
    MAP.push(array)
    W.times do |j|
        fronts.push([i,j]) unless array[j]
    end
end

ret=-1
while !fronts.empty? do
    nexts=[]
    fronts.each do |i,j|
        if i > 0 && MAP[i-1][j]
            nexts.push([i-1,j])
            MAP[i-1][j]=false
        end
        if j > 0 && MAP[i][j-1]
            nexts.push([i,j-1])
            MAP[i][j-1]=false
        end
        if i < H-1 && MAP[i+1][j]
            nexts.push([i+1,j])
            MAP[i+1][j]=false
        end
        if j < W-1 && MAP[i][j+1]
            nexts.push([i,j+1])
            MAP[i][j+1]=false
        end
    end
    fronts=nexts
    ret+=1
end
puts ret
