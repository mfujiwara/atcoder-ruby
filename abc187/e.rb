N=gets.to_i
nodes=Array.new(N){[]}
edges=[]
(N-1).times do |i|
  a,b=gets.chomp.split(" ").map(&:to_i)
  nodes[a-1].push(b-1)
  nodes[b-1].push(a-1)
  edges.push([a-1,b-1])
end
depth=Array.new(N,-1)
depth[0]=0
targets=[0]
while !targets.empty? do
  t=targets.pop
  nodes[t].each do |s|
    if depth[s]==-1
      depth[s]=depth[t]+1
      targets.push(s)
    end
  end
end
Q=gets.to_i
memo=Array.new(N,0)
Q.times do
  t,e,x=gets.chomp.split(" ").map(&:to_i)
  a,b=edges[e-1]
  if t==1
    if depth[a]<depth[b]
      memo[0]+=x
      memo[b]-=x
    else
      memo[a]+=x
    end
  else
    if depth[a]<depth[b]
      memo[b]+=x
    else
      memo[0]+=x
      memo[a]-=x
    end
  end
end

targets=[0]
while !targets.empty? do
  t=targets.pop
  nodes[t].each do |s|
    next if depth[t]>depth[s]
    memo[s]+=memo[t]
    targets.push(s)
  end
end
puts memo
