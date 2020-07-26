N=gets.to_i

MEMO=Array.new(10) { Array.new(10,0) }
(1..N).each do |n|
    ns=n.to_s
    MEMO[ns[0].to_i][ns[-1].to_i]+=1
end

ret = 0
(1..9).each do |i|
    (1..9).each do |j|
        ret += MEMO[i][j] * MEMO[j][i]
    end
end
puts ret
