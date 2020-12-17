H,W,N,M=gets.chomp.split(" ").map(&:to_i)
ret=0
MAP=Array.new(H){Array.new(W,0)}
BLOCK=Array.new(H){Array.new(W,false)}
N.times do
  a,b=gets.chomp.split(" ").map(&:to_i)
  MAP[a-1][b-1]=2**4-1
  ret+=1
end
M.times do
  c,d=gets.chomp.split(" ").map(&:to_i)
  BLOCK[c-1][d-1]=true
end
H.times do |i|
  W.times do |j|
    h,w = i,j
    if !BLOCK[h][w] && MAP[h][w]!=15
      if h!=0 && (MAP[h-1][w]&1)!=0
        ret+=1 if MAP[h][w]==0
        MAP[h][w]|=1
      end
      if w!=0 && (MAP[h][w-1]&2)!=0
        ret+=1 if MAP[h][w]==0
        MAP[h][w]|=2
      end
    end
    h,w = H-i-1,W-j-1
    if !BLOCK[h][w] && MAP[h][w]!=15
      if h!=H-1 && (MAP[h+1][w]&4)!=0
        ret+=1 if MAP[h][w]==0
        MAP[h][w]|=4
      end
      if w!=W-1 && (MAP[h][w+1]&8)!=0
        ret+=1 if MAP[h][w]==0
        MAP[h][w]|=8
      end
    end
  end
end
puts ret
