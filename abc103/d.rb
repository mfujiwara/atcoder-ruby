N,M=gets.chomp.split(" ").map(&:to_i)
MEMO_A=Array.new(N){ [] }
MEMO_B=Array.new(N){ {} }
M.times do
    a,b=gets.chomp.split(" ").map(&:to_i)
    MEMO_A[a-1].push(b-1)
    MEMO_B[b-1][a-1]=1
end
ret=0
pre = 0
N.times do |i|
    next if MEMO_B[i].empty?
    ret+=1
    (pre..(i-1)).each do |a|
        MEMO_A[a].each do |b|
            MEMO_B[b].delete(a)
        end
    end
    pre=i-1
end
puts ret
