N,M=gets.chomp.split(" ").map(&:to_i)
P=gets.chomp.split(" ").map {|p| (p.to_i)-1}
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
end
union=UnionFind.new(N)
M.times do
    x,y=gets.chomp.split(" ").map(&:to_i)
    union.unite(x-1,y-1)
end
ret=0
N.times do |i|
    ret+=1 if union.same_parent?(P[i], P[P[i]])
end
puts ret
