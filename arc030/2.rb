N,X=gets.chomp.split(" ").map(&:to_i)
if N==1
    puts 0
    exit
end
H_ARRAY=gets.chomp.split(" ").map(&:to_i)
EDGES={}
(N-1).times do
    a,b=gets.chomp.split(" ").map(&:to_i)
    EDGES[a]||=[]
    EDGES[a].push(b)
    EDGES[b]||=[]
    EDGES[b].push(a)
end
def calc(x, pre=nil, depth=0)
    r=0
    EDGES[x].each do |y|
        r+=calc(y, x, depth+1)  if y!=pre
    end
    r+=1 if r>0 || H_ARRAY[x-1]==1

    return r
end
ret = calc(X)
ret=1 if ret==0
puts ret*2-2
