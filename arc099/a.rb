N,K=gets.chomp.split(" ").map(&:to_i)
array=gets.chomp.split(" ").map(&:to_i)

puts N==K ? 1 : 1+(N-2)/(K-1)
