N,M=gets.chomp.split(" ").map(&:to_i)
ORD={}
LOW={}
EDGES={}
edeges = []
M.times do
    a,b=gets.chomp.split(" ").map(&:to_i)
    edeges.push([a,b])
    EDGES[a] ||= []
    EDGES[b] ||= []
    EDGES[a].push(b)
    EDGES[b].push(a)
end

$k=0
def dfs(u, pre)
    ORD[u] = $k
    $k += 1
    LOW[u] = ORD[u]
    EDGES[u].each do |v|
        if ORD[v] == nil
            dfs(v, u)
            LOW[u] = (LOW[u] < LOW[v]) ? LOW[u] : LOW[v]
        elsif v != pre
            LOW[u] = (LOW[u] < ORD[v]) ? LOW[u] : ORD[v]
        end
    end
end
dfs(edeges[0][0], nil)

ret = 0
edeges.each do |a,b|
    ret += 1 if ORD[a] < LOW[b] || ORD[b] < LOW[a]
end
puts ret
