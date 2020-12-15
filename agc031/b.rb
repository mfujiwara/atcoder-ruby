N=gets.to_i
MOD=10**9+7
pre={}
dp=Array.new(N+1,0)
dp[0]=1
N.times do |i|
    c=gets.to_i
    dp[i+1]+=dp[i]
    j = pre[c] || i-1
    if j != i-1
        dp[i+1] += dp[j+1]
    end
    pre[c]=i
    dp[i+1]%=MOD
end
puts dp[N]
