N,M=gets.chomp.split(" ").map(&:to_i)
s,t=gets.chomp.split(" ").map(&:to_i)
INF=10**10
def bellman_ford(edge_list, s, max_count)
  d = Array.new(N, INF)
  d[s] = 0
  c = 0
  loop do
    is_update = false
    edge_list.each do |(u, v, c)|
      if d[u] != INF && d[u] + c < d[v]
        d[v] = d[u] + c
        is_update = true
      end
    end
    return d if !is_update
    c += 1
    return nil if c == max_count
  end
end

edge_list=[]
M.times do
  x,y,d=gets.chomp.split(" ").map(&:to_i)
  edge_list.push([x-1,y-1,d])
  edge_list.push([y-1,x-1,d])
end

d_s=bellman_ford(edge_list,s-1,N)
d_t=bellman_ford(edge_list,t-1,N)

N.times do |i|
  if d_s[i]==d_t[i] && d_s[i]<10**10
    puts i+1
    exit
  end
end
puts "-1"
