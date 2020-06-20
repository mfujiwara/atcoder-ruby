N=gets.to_i
array=gets.chomp.split(" ").map(&:to_i)

ret0=0
e=1
array.each do |a|
    ret0 = ret0 + a*e
    e*=-1
end
rets=[ret0]
(1..(N-1)).each do |n|
    rets[n] = 2*array[n-1] - rets[n-1]
end
puts rets.join(" ")
