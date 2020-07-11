N,C=gets.chomp.split(" ").map(&:to_i)
MEMO=Array.new(100,0)
N.times do |n|
    a=gets.to_i
    (1..10).each do |i|
        (1..10).each do |j|
            index = i*10+j-11
            if i == j
                MEMO[index] += C
            elsif n.even?
                MEMO[index] += C if a != i
            else
                MEMO[index] += C if a != j
            end
        end
    end
end
puts MEMO.min
