N,K=gets.chomp.split(" ").map(&:to_i)
array=gets.chomp.split(" ").map(&:to_i)
ret=0
(0..(N-1)).each do |i|
    a = array[i]
    s = i >= K ? K : i+1
    t = i <= N-K ? 0 : K-N+i
    ret+=a*(s-t)
end
puts ret
