N=gets.to_i
counts=Array.new(N,0)
edges=Array.new(N){[]}
(N-1).times do
  a,b=gets.chomp.split(" ").map(&:to_i)
  counts[a-1]+=1
  counts[b-1]+=1
  edges[a-1].push(b-1)
  edges[b-1].push(a-1)
end
c_array=gets.chomp.split(" ").map(&:to_i).sort

puts c_array.inject(&:+) - c_array[-1]

rets=Array.new(N)
c_array.each_with_index do |c, c_index|
  index=counts.index(1)
  break if index==nil
  rets[index]=c
  edges[index].each do |b|
    edges[b].delete(index)
    counts[b]-=1
    if c_index==N-2
      rets[b]=c_array[-1]
    end
  end
  edges[index]=[]
  counts[index]=0
end
puts rets.join(" ")
