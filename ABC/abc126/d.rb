N=gets.to_i
TREE=Array.new(N) { [] }
(N-1).times do
    u,v,w=gets.chomp.split(" ").map(&:to_i)
    TREE[u-1].push([v-1,w])
    TREE[v-1].push([u-1,w])
end
rets=Array.new(N,nil)
rets[0]=0
nows=[0]
while !nows.empty? do
    nexts=[]
    nows.each do |u|
        TREE[u].each do |v,w|
            next if rets[v]!=nil
            if w.even?
                rets[v]=rets[u]
            else
                rets[v]=(rets[u]+1)%2
            end
            nexts.push(v)
        end
    end
    nows=nexts
end
rets.each {|r| puts r}
