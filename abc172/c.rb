N,M,K=gets.chomp.split(" ").map(&:to_i)
a_array=gets.chomp.split(" ").map(&:to_i)
b_array=gets.chomp.split(" ").map(&:to_i)

b_sum=b_array.inject(&:+)
b_num=M
while b_sum > K do
    b_sum-=b_array[b_num-1]
    b_num-=1
end
ret=b_num

a_sum=0
(1..N).each do |a_num|
    a_sum+=a_array[a_num-1]
    break if a_sum > K
    while a_sum + b_sum > K && b_num > 0 do
        b_sum-=b_array[b_num-1]
        b_num-=1
    end
    r = a_num+b_num
    ret = r if ret < r
end
puts ret
