N = gets.to_i

array = []
N.times do
    w = gets.to_i
    index = array.bsearch_index { |x| x >= w }
    if index 
        array[index] = w
    else
        array.push(w)
    end
end
puts array.length