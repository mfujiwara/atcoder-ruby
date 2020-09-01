MAP=[]
10.times do
    MAP.push(gets.chomp)
end
# colorize
def colorize(color,row,col)
    MAP[row][col]=color
    targets=[[row,col]]
    while !targets.empty? do
        new_targets=[]
        targets.each do |r,c|
            if r>0 && MAP[r-1][c]=="o"
                MAP[r-1][c]=color
                new_targets.push([r-1,c])
            end
            if r<9 && MAP[r+1][c]=="o"
                MAP[r+1][c]=color
                new_targets.push([r+1,c])
            end
            if c>0 && MAP[r][c-1]=="o"
                MAP[r][c-1]=color
                new_targets.push([r,c-1])
            end
            if c<9 && MAP[r][c+1]=="o"
                MAP[r][c+1]=color
                new_targets.push([r,c+1])
            end
        end
        targets=new_targets
    end
end

land_count=0

10.times do |r|
    10.times do |c|
        if MAP[r][c]=="o"
            colorize(land_count.to_s,r,c)
            land_count+=1
        end
    end
end

# judge
if land_count <= 1
    puts "YES"
    exit
end
10.times do |r|
    10.times do |c|
        if MAP[r][c]=="x"
            lands=[]
            lands.push(MAP[r-1][c]) if r>0 && MAP[r-1][c]!="x"
            lands.push(MAP[r+1][c]) if r<9 && MAP[r+1][c]!="x"
            lands.push(MAP[r][c-1]) if c>0 && MAP[r][c-1]!="x"
            lands.push(MAP[r][c+1]) if c<9 && MAP[r][c+1]!="x"
            if lands.sort.uniq.length==land_count
                puts "YES"
                exit
            end
        end
    end
end
puts "NO"
