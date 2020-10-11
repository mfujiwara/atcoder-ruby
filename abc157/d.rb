N,M,K=gets.chomp.split(" ").map(&:to_i)
class UnionFind
    def initialize(size)
      @rank = Array.new(size, 0)
      @parent = Array.new(size, &:itself)
    end
  
    def unite(id_x, id_y)
      x_parent = get_parent(id_x)
      y_parent = get_parent(id_y)
      return if x_parent == y_parent
  
      if @rank[x_parent] > @rank[y_parent]
        @parent[y_parent] = x_parent
      else
        @parent[x_parent] = y_parent
        @rank[y_parent] += 1 if @rank[x_parent] == @rank[y_parent]
      end
    end
  
    def get_parent(id_x)
      @parent[id_x] == id_x ? id_x : (@parent[id_x] = get_parent(@parent[id_x]))
    end
  
    def same_parent?(id_x, id_y)
      get_parent(id_x) == get_parent(id_y)
    end
  
    def size
      @parent.map { |id_x| get_parent(id_x) }.uniq.size
    end

    def grouped_size
        rets = Array.new(@parent.length) {[]}
        (0..(@parent.length-1)).each do |i|
            rets[i]=rets[get_parent(i)]
            rets[i].push(i)
        end
        rets.map{|g| g.length}
    end
end
union=UnionFind.new(N)
friends=[]
M.times do
    a,b=gets.chomp.split(" ").map(&:to_i)
    union.unite(a-1,b-1)
    friends.push([a-1,b-1])
end
friened=Array.new(N,0)
friends.each do |f|
    if union.same_parent?(f[0],f[1])
        friened[f[0]]+=1
        friened[f[1]]+=1
    end
end
blocked=Array.new(N,0)
K.times do
    c,d=gets.chomp.split(" ").map(&:to_i)
    if union.same_parent?(c-1,d-1)
        blocked[c-1]+=1
        blocked[d-1]+=1
    end
end
grouped_size = union.grouped_size
rets=Array.new(N,0)
N.times do |i|
    rets[i] = grouped_size[i] - 1 - friened[i] - blocked[i]
end
puts rets.join(" ")
