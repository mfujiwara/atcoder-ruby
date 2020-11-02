N,K=gets.chomp.split(" ").map(&:to_i)
A=[]
B=Array.new(N) { [] }
N.times do
    array=gets.chomp.split(" ").map(&:to_i)
    A.push(array)
    array.each_with_index do |a,i|
        B[i].push(a)
    end
end
MOD=998244353
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
  
    def sizes
      @parent.group_by { |id_x| get_parent(id_x) }.map{|k,v| v.length }
    end
end
union_row=UnionFind.new(N)
union_col=UnionFind.new(N)
(0..(N-2)).each do |i|
    ((i+1)..(N-1)).each do |j|
        r_row=true
        N.times do |k|
            if A[i][k]+A[j][k] > K
                r_row=false
                break
            end
        end
        if r_row
            union_row.unite(i,j)
        end

        r_col=true
        N.times do |k|
            if A[k][i]+A[k][j] > K
                r_col=false
                break
            end
        end
        if r_col
            union_col.unite(i,j)
        end
    end
end
def kaijou(a)
    return 1 if a==0
    (1..a).inject(1) {|i,j| i*j % MOD }
end
ret=1
union_row.sizes.each do |s|
    ret*=kaijou(s)
    ret%=MOD
end
union_col.sizes.each do |s|
    ret*=kaijou(s)
    ret%=MOD
end
puts ret
