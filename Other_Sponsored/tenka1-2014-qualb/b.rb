N=gets.to_i
S=gets.chomp
PHRASES={}
N.times do
    t=gets.chomp
    PHRASES[t]="1"
end
MOD=10**9+7
DP=Array.new(S.length+1, 0)
DP[0]=1
S.length.times do |i|
    next if DP[i]==0
    (0..(S.length-i-1)).each do |j|
        sub=S[i..(i+j)]
        if PHRASES[sub]
            DP[i+j+1]+=DP[i]
            DP[i+j+1]%=MOD
        end
    end
end
puts DP[-1]
