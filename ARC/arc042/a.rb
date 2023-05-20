N,M=gets.chomp.split(" ").map(&:to_i)
array=Array.new(N) {|i| [i,N-i] }
M.times do |i|
    index=N+i
    a=gets.to_i
    array[a-1][1]=index
end
array.sort_by {|a| a[1] }.reverse.each do |a,index|
    puts a+1
end
