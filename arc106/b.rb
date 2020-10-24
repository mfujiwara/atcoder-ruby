N,M=gets.chomp.split(" ").map(&:to_i)
a_array=gets.chomp.split(" ").map(&:to_i)
b_array=gets.chomp.split(" ").map(&:to_i)

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
    c,d=gets.chomp.split(" ").map(&:to_i)
    union.unite(c-1,d-1)
end

A=Array.new(N,0)
B=Array.new(N,0)
N.times do |i|
    parent = union.get_parent(i)
    A[parent]+=a_array[i]
    B[parent]+=b_array[i]
end

if A==B
    puts "Yes"
else
    puts "No"
end
