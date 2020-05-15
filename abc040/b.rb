n = gets.to_i

ans = n
(1..n).each do |i|
    (1..i).each do |j|
        break if n < i*j
        if n == i*j && i == j
            puts 0
            exit
        end
        ans = [ans, n-i*j+i-j].min
    end
end
puts ans
