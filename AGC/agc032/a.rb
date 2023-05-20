N=gets.to_i
array=gets.chomp.split(" ").map(&:to_i)
indexes=Array.new(N){|i|i}
rets=Array.new(N, nil)
N.downto(1) do |i|
    a = array[i-1]
    index=indexes.delete_at(a-1)
    if index == nil
        puts -1
        exit
    end
    rets[index]= a
end
rets.each do |r|
    puts r
end
