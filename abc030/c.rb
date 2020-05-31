N,M=gets.chomp.split(" ").map(&:to_i)
X,Y=gets.chomp.split(" ").map(&:to_i)
array_a=gets.chomp.split(" ").map(&:to_i)
array_b=gets.chomp.split(" ").map(&:to_i)
now = 0
ret = 0
loop do
    a_i = array_a.find_index {|n| n>=now }
    break if a_i== nil
    a = array_a.shift(a_i+1)[-1]
    now = a+X
    b_i = array_b.find_index {|n| n>=now }
    break if b_i == nil
    b = array_b.shift(b_i+1)[-1]
    now = b+Y
    ret+=1
end
puts ret
