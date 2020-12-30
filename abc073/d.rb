INF=10**8
N,M,R=gets.chomp.split(" ").map(&:to_i)
array=gets.chomp.split(" ").map(&:to_i)
edge_list=[]
M.times do
  a,b,c=gets.chomp.split(" ").map(&:to_i)
  edge_list.push([a-1,b-1,c])
  edge_list.push([b-1,a-1,c])
end

def warshall_floyd(node_size, edge_list)
  d = Array.new(node_size) { Array.new(node_size,INF) }
  edge_list.each do |u, v, c|
    d[u][v] = c
  end

  node_size.times do |k|
    node_size.times do |i|
      node_size.times do |j|
        d[i][j] = [d[i][j], d[i][k] + d[k][j]].min
      end
    end
  end
  d
end

d = warshall_floyd(N,edge_list)
ret=INF
array.permutation do |perm|
  r=0
  perm.each_cons(2) do |i,j|
    r+=d[i-1][j-1]
  end
  ret=r if ret>r
end
puts ret
