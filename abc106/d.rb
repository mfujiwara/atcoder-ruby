N,M,Q=gets.chomp.split(" ").map(&:to_i)
MEMO=Array.new(N){ Array.new(N,0) }
M.times do
    l,r=gets.chomp.split(" ").map(&:to_i)
    l.times do |i|
        MEMO[i][r-1]+=1
    end
end
SUM=Array.new(N) { Array.new(N,0) }
N.times do |i|
    (i..(N-1)).each do |j|
        if j==0 || i==j
            SUM[i][j]=MEMO[i][j]
        else
            SUM[i][j]=MEMO[i][j]+SUM[i][j-1]
        end
    end
end
Q.times do
    pp,qq=gets.chomp.split(" ").map(&:to_i)
    puts SUM[pp-1][qq-1]
end
