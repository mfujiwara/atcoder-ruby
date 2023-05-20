N=gets.to_i
max_count=0
MEMO=Array.new(N+1,0)
N.times do
    p=gets.to_i
    MEMO[p]=MEMO[p-1]+1
    max_count = MEMO[p] if max_count < MEMO[p]
end
puts N-max_count
