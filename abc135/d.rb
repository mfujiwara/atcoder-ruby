MOD=10**9+7
S=gets.chomp
DP=Array.new(S.length+1) {Array.new(13,0)}
DP[0][0]=1
mod_base=1
(1..S.length).each do |i|
  ch = S[-i]
  if ch=="?"
    13.times do |n|
      next if DP[i-1][n]==0
      mm=n
      10.times do |m|
        DP[i][mm] += DP[i-1][n]
        DP[i][mm] %= MOD
        mm+=mod_base
        mm%=13
      end
    end
  else
    m=ch.to_i
    mm=mod_base*m%13
    13.times do |n|
      DP[i][mm] = DP[i-1][n]
      mm+=1
      mm%=13
    end
  end
  mod_base = mod_base*10%13
end
puts DP[-1][5]
