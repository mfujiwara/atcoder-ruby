N,h=gets.chomp.split(" ").map(&:to_i)
array=[]
max_a = 0
sorted_b = []
N.times do
    a,b=gets.chomp.split(" ").map(&:to_i)
    if max_a < a
        max_a = a
    end
    index = sorted_b.bsearch_index {|x|x>=b} || -1
    sorted_b.insert(index, b)
end

ret = 0
sorted_b.reverse.each do |b|
    break if b < max_a
    h -= b
    ret+=1
    if h <= 0
        puts ret
        exit
    end
end
ret += h/max_a
ret += 1 if h%max_a != 0
puts ret
