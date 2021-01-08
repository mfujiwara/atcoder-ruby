class UnionFind
  def initialize(size)
    @rank = Array.new(size, 0)
    @parent = Array.new(size, &:itself)
    @counts = Array.new(size, 1)
  end

  def unite(id_x, id_y)
    x_parent = get_parent(id_x)
    y_parent = get_parent(id_y)
    return if x_parent == y_parent

    if @rank[x_parent] > @rank[y_parent]
      @parent[y_parent] = x_parent
      @counts[x_parent] += @counts[y_parent]
    else
      @parent[x_parent] = y_parent
      @counts[y_parent] += @counts[x_parent]
      @rank[y_parent] += 1 if @rank[x_parent] == @rank[y_parent]
    end
  end

  def get_parent(id_x)
    @parent[id_x] == id_x ? id_x : (@parent[id_x] = get_parent(@parent[id_x]))
  end

  def same_parent?(id_x, id_y)
    get_parent(id_x) == get_parent(id_y)
  end

  def same_parent_conut(id_x)
    x_parent = get_parent(id_x)
    @counts[x_parent]
  end

  def size
    @parent.map { |id_x| get_parent(id_x) }.uniq.size
  end
end

N,M=gets.chomp.split(" ").map(&:to_i)
bridges=[]
M.times do
  a,b=gets.chomp.split(" ").map(&:to_i)
  bridges.push([a-1,b-1])
end
rets=[N*(N-1)/2]
union=UnionFind.new(N)
(M-1).downto(1) do |m|
  a,b=bridges[m]
  if union.same_parent?(a,b)
    rets.unshift(rets[0])
  else
    benri=union.same_parent_conut(a)*union.same_parent_conut(b)
    rets.unshift(rets[0]-benri)
  end
  union.unite(a,b)
end
puts rets
