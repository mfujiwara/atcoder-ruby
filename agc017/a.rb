N,P=gets.chomp.split(" ").map(&:to_i)
array=gets.chomp.split(" ").map(&:to_i)
if array.all? {|a| a.even? }
    puts (P==0) ? 2**N : 0
else
    puts 2**(N-1)
end
