require 'prime'
like_2017s = Prime.each(100000).select {|n| Prime.prime?((n+1)/2) }

Q = gets.to_i
Q.times do
    l,r=gets.chomp.split(" ").map(&:to_i)
    l_index = like_2017s.bsearch_index { |x| x >= l }
    if l_index == nil
        puts 0
        next
    end
    r_index = like_2017s.bsearch_index { |x| x > r }
    if r_index == nil
        r_index = like_2017s.length
    end
    puts r_index - l_index
end
