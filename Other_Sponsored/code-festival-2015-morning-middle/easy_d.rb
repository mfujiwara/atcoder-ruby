N=gets.to_i
S=gets.chomp
ret=N
(N-1).times do |i|
    ls = S[0..i]
    rs = S[(i+1)..(N-1)]

    dp=Array.new(ls.length+1) {Array.new(rs.length+1,0)}
    
    ls.each_char.with_index do |lc, li|
        rs.each_char.with_index do |rc, ri|
            dp[li+1][ri+1] = dp[li][ri+1] > dp[li+1][ri] ? dp[li][ri+1] : dp[li+1][ri]
            x = dp[li][ri]
            x+=1 if lc == rc
            dp[li+1][ri+1] = x if dp[li+1][ri+1] < x
        end
    end
    r = N - dp[-1][-1]*2
    ret = r if ret > r
end
puts ret
