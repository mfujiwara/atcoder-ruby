x,y,W=gets.chomp.split(" ")
X=x.to_i
Y=y.to_i
C=[]
9.times do 
    C.push(gets.chomp.split("").map(&:to_i))
end
D = {}
D["R"] = [0,1]
D["L"] = [0,-1]
D["U"] = [-1,0]
D["D"] = [1,0]
D["RU"] = [-1,1]
D["RD"] = [1,1]
D["LU"] = [-1,-1]
D["LD"] = [1,-1]

indexes = Array.new(4) {|i| [X-1+D[W][1]*i,Y-1+D[W][0]*i] }
rets = indexes.map do |x,y|
    if x < 0
        x *= -1
    elsif x > 8
        x = 16-x
    end
    if y < 0
        y *= -1
    elsif y > 8
        y = 16-y
    end
    C[y][x].to_s
end
puts rets.join("")
