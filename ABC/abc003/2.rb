S = gets.chomp.split("")
T = gets.chomp.split("")

atcoder = ['a','t','c','o','d','e','r', '@']
at = '@'

S.each_with_index do |s, index|
    t = T[index]
    next if s == t
    next if s == at && atcoder.include?(t)
    next if t == at && atcoder.include?(s)
    puts 'You will lose'
    exit
end

puts 'You can win'