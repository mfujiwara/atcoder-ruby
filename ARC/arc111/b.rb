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
N=gets.to_i
color_num=-1
color_map={}
converted_cards=[]
N.times do
  a,b=gets.chomp.split(" ").map(&:to_i)
  aa = if color_map[a]
    color_map[a]
  else
    color_num+=1
    color_map[a]=color_num
  end
  bb = if color_map[b]
    color_map[b]
  else
    color_num+=1
    color_map[b]=color_num    
  end
  converted_cards.push([aa,bb])
end
color_num+=1
union=UnionFind.new(color_num)
color_counts=Array.new(color_num,0)
converted_cards.each do |a,b|
  union.unite(a,b)
  color_counts[a]+=1
  color_counts[b]+=1
end
edge_counts={}
color_num.times do |i|
  parent=union.get_parent(i)
  edge_counts[parent]||=0
  edge_counts[parent]+=color_counts[i]
end

tree_num = edge_counts.count do |key,val|
  union.same_parent_conut(key) == val/2 + 1
end
puts color_num-tree_num
