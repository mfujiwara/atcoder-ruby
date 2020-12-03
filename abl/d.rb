N,K=gets.chomp.split(" ").map(&:to_i)
INF=10**6
class SegmentTree
    def initialize(size)
      @n=1
      while @n < size do
        @n *= 2
      end
      @node = Array.new(2*@n, 0)
    end
  
    def update(index, val)
      i = index + @n - 1
      @node[i] = val
      while i > 0 do
        i = (i - 1)/2
        l = @node[2*i+1]
        r = @node[2*i+2]
        @node[i] = l > r ? l : r
      end
    end
  
    def get_max(left, right)
        ret=0
        left+=@n-1
        right+=@n-1
        while left<right
          if left.even?
            ret=@node[left] if ret<@node[left]
            left+=1
          end
          if right.even?
            right-=1
            ret=@node[right] if ret<@node[right]
          end
          left/=2
          right/=2
        end
        return ret
    end
end

ret=0
tree=SegmentTree.new(300001)
N.times do
    a=gets.to_i
    lower= a >= K ? a-K : 0
    upper= a <= 300000-K ? a+K : 300000
    r = tree.get_max(lower, upper+1) + 1
    tree.update(a, r)
    ret = r if ret < r
end
puts ret