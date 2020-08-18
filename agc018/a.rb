N,K=gets.chomp.split(" ").map(&:to_i)
array=gets.chomp.split(" ").map(&:to_i).sort
if K > array[-1]
    puts "IMPOSSIBLE"
    exit
end
all_gcd=array[0]
if all_gcd == K
    puts "POSSIBLE"
    exit
end
(1..(N-1)).each do |i|
    all_gcd = all_gcd.gcd(array[i])
    if K%all_gcd==0
        puts "POSSIBLE"
        exit
    end
end
puts "IMPOSSIBLE"
