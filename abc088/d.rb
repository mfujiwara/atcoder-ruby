H,W=gets.chomp.split(" ").map(&:to_i)
S=[]
dot_count = 0
H.times do
    s = gets.chomp
    dot_count += s.count(".")
    S.push(s)
end

nows=[[0,0]]
turn = 0
loop do
    nexts = []
    if nows.empty?
        puts -1
        exit
    end
    break if nows.include?([H-1,W-1])
    nows.each do |x,y|
        S[x][y] = "#"
        if x!=H-1 && S[x+1][y]=="."
            nexts.push([x+1,y])
            S[x+1][y] = "#"
        end
        if x!=0 && S[x-1][y]=="."
            nexts.push([x-1,y])
            S[x-1][y] = "#"
        end
        if y!=W-1 && S[x][y+1]=="."
            nexts.push([x,y+1])
            S[x][y+1] = "#"
        end
        if y!=0 && S[x][y-1]=="."
            nexts.push([x,y-1])
            S[x][y-1] = "#"
        end
    end
    nows = nexts
    turn+=1
end
puts dot_count - turn -1
