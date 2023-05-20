N,M=gets.chomp.split(" ").map(&:to_i)
edges={}
M.times do
    u,v=gets.chomp.split(" ").map(&:to_i)
    edges[u]||=[]
    edges[u].push(v)
    edges[v]||=[]
    edges[v].push(u)
end
vs=Array.new(N,nil)
ret=0
(1..N).each do |n|
    next if vs[n]
    is_tree=true
    vs[n]=0
    targets = [n]
    while !targets.empty? do
        nexts=[]
        targets.each do |t|
            edges[t]||=[]
            edges[t].each do |v|
                next if vs[v]==0 || vs[t]==v
                if vs[v]
                    is_tree=false
                else
                    nexts.push(v)
                    vs[v]=t
                end
            end
        end
        targets=nexts
    end
    ret+=1 if is_tree
end
puts ret
