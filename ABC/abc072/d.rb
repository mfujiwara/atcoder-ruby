N = gets.to_i
array = gets.chomp.split(" ").map(&:to_i)

ret = 0
skip = false
array.each_with_index do |a, index|
    if skip
        skip = false
        next
    end

    if a == index+1
        skip = true
        ret += 1
    end
end
puts ret
