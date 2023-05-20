N,M = gets.chomp.split(" ").map(&:to_i)
array_a = gets.chomp.split(" ").map(&:to_i)
array_b = gets.chomp.split(" ").map(&:to_i)

sorted_a = array_a.sort.reverse
sorted_b = array_b.sort.reverse

sorted_b.each_with_index do |b, index|
    a = sorted_a[index]
    if a == nil || b > a
        puts 'NO'
        exit
    end
end

puts 'YES'
