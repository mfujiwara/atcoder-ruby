H,W=gets.chomp.split(" ").map(&:to_i)
C_h,C_w=gets.chomp.split(" ").map(&:to_i)
D_h,D_w=gets.chomp.split(" ").map(&:to_i)
S=[]
H.times do
    array=gets.chomp.split("").map{|s| s=="." }
    S.push(array)
end
 
ret=0
nows=[[C_h-1,C_w-1]]
while !nows.empty? do
    # walk
    edges = nows
    while !edges.empty? do
        edges_new = []
        edges.each do |edge_h,edge_w|
            if edge_h>0 && S[edge_h-1][edge_w]
                edges_new.push([edge_h-1,edge_w])
                nows.push([edge_h-1,edge_w])
                S[edge_h-1][edge_w]=false
            end
            if edge_w>0 && S[edge_h][edge_w-1]
                edges_new.push([edge_h,edge_w-1])
                nows.push([edge_h,edge_w-1])
                S[edge_h][edge_w-1]=false
            end
            if edge_h<H-1 && S[edge_h+1][edge_w]
                edges_new.push([edge_h+1,edge_w])
                nows.push([edge_h+1,edge_w])
                S[edge_h+1][edge_w]=false
            end
            if edge_w<W-1 && S[edge_h][edge_w+1]
                edges_new.push([edge_h,edge_w+1])
                nows.push([edge_h,edge_w+1])
                S[edge_h][edge_w+1]=false
            end
        end
        edges=edges_new
    end
    if !S[D_h-1][D_w-1]
        puts ret
        exit
    end
    # magic
    nows_new=[]
    nows.each do |now_h, now_w|
        5.times do |i|
            h=now_h-2+i
            next if h<0 || h>H-1
            5.times do |j|
                w=now_w-2+j
                next if w<0 || w>W-1
                next if (h==0 && w.abs<2) || (w==0 && h.abs<2)
                if S[h][w]
                    nows_new.push([h,w])
                    S[h][w]=false
                end
            end
        end
    end
    ret+=1
    nows=nows_new
end
puts "-1"