R,C=gets.chomp.split(" ").map(&:to_i)
SY,SX=gets.chomp.split(" ").map(&:to_i)
GY,GX=gets.chomp.split(" ").map(&:to_i)
M=[]
R.times do
    M.push(gets.chomp)
end
ret = 0
nows = [[SY,SX]]
M[SY-1][SX-1] = "#"
loop do
    nows.each do |y,x|
        if x==GX && y==GY
            puts ret
            exit
        end
    end
    nexts = []
    nows.each do |y,x|
        if M[y-1][x-2] == "."
            nexts.push([y,x-1])
            M[y-1][x-2] = "#"
        end
        if M[y-1][x] == "."
            nexts.push([y,x+1])
            M[y-1][x] = "#"
        end
        if M[y-2][x-1] == "."
            nexts.push([y-1,x])
            M[y-2][x-1] = "#"
        end
        if M[y][x-1] == "."
            nexts.push([y+1,x])
            M[y][x-1] = "#"
        end
    end
    nows = nexts
    ret += 1
end