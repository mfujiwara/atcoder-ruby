S=gets.to_i
MEMO={}
MEMO[1]=0
MEMO[2]=0
MEMO[3]=1
MEMO[4]=1
MEMO[5]=1
if S<6
    puts MEMO[S]
    exit
end
(6..S).each do |s|
    MEMO[s]=1
    (3..(s-3)).each do |t|
        MEMO[s]+=MEMO[t]
    end
    MEMO[s]
end
puts MEMO[S]%(10**9+7)
