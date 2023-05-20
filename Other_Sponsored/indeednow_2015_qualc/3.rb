N=gets.to_i
TREE=Array.new(N){{}}
(N-1).times do
    a,b=gets.chomp.split(" ").map(&:to_i)
    TREE[a-1][b-1]="1"
    TREE[b-1][a-1]="1"
end

class MinHeap
    def initialize(source)
      @arr = []
      source.each do |e|
        push(e)
      end
    end
  
    def size
      @arr.size
    end
  
    def empty?
      @arr.empty?
    end
  
    def top
      @arr.first
    end
  
    def push(value)
      @arr << value
      i = @arr.size - 1
  
      while i > 0
        parent = (i - 1) / 2
        break if @arr[parent] <= value
        @arr[parent], @arr[i] = @arr[i], @arr[parent]
        i = parent
      end
  
      @arr[i] = value
    end
  
    def pop
      min = top
  
      tmp_node = @arr.last
      @arr.pop
  
      i = 0
      while (i * 2 + 1) < size
        lhs_child = i * 2 + 1
        rhs_child = i * 2 + 2
        min_child = lhs_child
  
        if rhs_child < size
          if @arr[lhs_child] > @arr[rhs_child]
            min_child = rhs_child
          end
        end
  
        break if @arr[min_child] >= tmp_node
  
        @arr[i] = @arr[min_child]
        i = min_child
      end
  
      @arr[i] = tmp_node unless empty?
  
      min
    end
  end

rets=[0]
heap=MinHeap.new([])
TREE[0].each do |a,v|
    TREE[a].delete(0)
    heap.push(a)
end
(N-1).times do
    now=heap.pop
    rets.push(now)
    TREE[now].each do |a,v|
        TREE[a].delete(now)
        heap.push(a)
    end
end
puts rets.map{|i| (i+1).to_s }.join(" ")
