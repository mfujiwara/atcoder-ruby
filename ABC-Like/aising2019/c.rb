H,W=gets.chomp.split(" ").map(&:to_i)
MAP=[]
WHITES={}
H.times do |i|
    array=[]
    gets.chomp.split("").each_with_index do |a,j|
        if a=="."
            array.push(true)
            WHITES[[i,j]]="1"
        else
            array.push(false)
        end
    end
    MAP.push(array)
end
ret=0
while !WHITES.empty? do
    nows=[WHITES.shift[0]]
    MAP[nows[0][0]][nows[0][1]]=nil
    w_count=1
    b_count=0
    turn_w=false
    while !nows.empty? do
        nexts=[]
        nows.each do |i,j|
            if i>0 && MAP[i-1][j]==turn_w
                nexts.push([i-1,j])
                MAP[i-1][j]=nil
                if turn_w
                    WHITES.delete([i-1,j])
                    w_count+=1
                else
                    b_count+=1
                end
            end
            if i<H-1 && MAP[i+1][j]==turn_w
                nexts.push([i+1,j])
                MAP[i+1][j]=nil
                if turn_w
                    WHITES.delete([i+1,j])
                    w_count+=1
                else
                    b_count+=1
                end
            end
            if j>0 && MAP[i][j-1]==turn_w
                nexts.push([i,j-1])
                MAP[i][j-1]=nil
                if turn_w
                    WHITES.delete([i,j-1])
                    w_count+=1
                else
                    b_count+=1
                end
            end
            if j<W-1 && MAP[i][j+1]==turn_w
                nexts.push([i,j+1])
                MAP[i][j+1]=nil
                if turn_w
                    WHITES.delete([i,j+1])
                    w_count+=1
                else
                    b_count+=1
                end
            end
        end
        nows=nexts
        turn_w= !turn_w
    end
    ret+=w_count*b_count
end
puts ret
