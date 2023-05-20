N=gets.to_i
array=gets.chomp.split(" ").map(&:to_i)
MEMO={}
MEMO[0] = 1
now=0
array.each do |a|
    now += a
    MEMO[now] ||= 0
    MEMO[now] += 1
end
ret = 0
MEMO.each do |k,v|
    ret += (v-1)*v/2
end
puts ret
