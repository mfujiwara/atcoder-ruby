N = gets.to_i
array=gets.chomp.split(" ").map.with_index {|a,index| [a.to_i, index+1] }

array.sort{|a, b| a[0] <=> b[0] }.reverse.each do |e|
    puts e[1]
end
