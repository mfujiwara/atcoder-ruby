N=gets.to_i
num_to_index = {}
sorted_array = []
(0..(N-1)).each do |i|
    a=gets.to_i
    num_to_index[a] ||= []
    num_to_index[a].push(i)

    index = sorted_array.bsearch_index{|x| x>=a } || sorted_array.length
    if sorted_array[index] != a
        sorted_array.insert(index, a)
    end
end

ret = Array.new(N, nil)
sorted_array.each_with_index do |n,sorted_index|
    indexes = num_to_index[n]
    indexes.each do |index|
        ret[index] = sorted_index
    end
end

ret.each do |r|
    puts r
end
