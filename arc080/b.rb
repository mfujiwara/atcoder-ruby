H,W=gets.chomp.split(" ").map(&:to_i)
N=gets.to_i
array=gets.chomp.split(" ").map(&:to_i)
rets=array.map.with_index {|a,index| Array.new(a,index+1) }
    .flatten
    .each_slice(W).to_a
rets.each_with_index do |ret, index|
    ret=ret.reverse if index.odd?
    puts ret.join(" ")
end
