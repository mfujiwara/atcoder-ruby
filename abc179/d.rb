N,K=gets.chomp.split(" ").map(&:to_i)
S=[]
K.times do
    l,r=gets.chomp.split(" ").map(&:to_i)
    S.push([l,r])
end
DP=Array.new(N+1,0)
SUM=Array.new(N+1,0)
DP[1]=1
SUM[1]=1
(2..N).each do |i|
    S.each do |l,r|
        l = (0 > i-l) ? 0 : i-l
        r = (0 > i-r-1) ? 0 : i-r-1
        DP[i]+=SUM[l]-SUM[r]
        DP[i]=DP[i]%998244353
    end
    SUM[i]=DP[i]+SUM[i-1]
end
puts DP[N]
