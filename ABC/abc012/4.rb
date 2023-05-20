N,M=gets.chomp.split(" ").map(&:to_i)
nodes=(0..(N-1)).to_a
edges=[]
M.times do
    a,b,t=gets.chomp.split(" ").map(&:to_i)
    edges.push([a-1,b-1,t])
    edges.push([b-1,a-1,t])
end
 
INF=300000
def warshall_floyd(node_list, edge_list)
    d = Array.new(node_list.length) { Array.new(node_list.length,INF) }
    node_list.each do |n|
        d[n][n]=0
    end
    edge_list.each do |u, v, c|
        d[u][v] = c
    end
  
    node_list.each do |k|
        node_list.each do |i|
            node_list.each do |j|
                d[i][j] = [d[i][j], d[i][k] + d[k][j]].min
            end
        end
    end
    d
end
 
d=warshall_floyd(nodes, edges)
puts d.map {|dd| dd.max}.min
