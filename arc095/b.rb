N=gets.to_i
array=gets.chomp.split(" ").map(&:to_i)
n=array[0]
r=array[1]
N.times do |i|
    n = array[i] if n < array[i]
end
N.times do |i|
    next if array[i] == n || array[i] == r
    r = array[i] if (n-2*r).abs > (n-array[i]*2).abs
end
puts "#{n} #{r}"
