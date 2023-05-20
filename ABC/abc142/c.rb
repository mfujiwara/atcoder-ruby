N=gets.to_i
array=gets.chomp.split(" ").map(&:to_i)
sorted = array.map.with_index do |a,i|
    [a,i]
end.sort_by do |a,i|
    i
end.map do |a,i|
    a.to_s
end

puts sorted.join(" ")
