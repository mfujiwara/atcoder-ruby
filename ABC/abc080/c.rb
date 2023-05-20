N=gets.to_i
F=[]
N.times do
    array=gets.chomp.split(" ").map(&:to_i)
    F.push(array)
end
P=[]
N.times do
    array=gets.chomp.split(" ").map(&:to_i)
    P.push(array)
end
ret= -(10**9)
all=[0, 1].repeated_permutation(10).to_a
all.shift
all.each do |g|
    r=0
    N.times do |n|
        count=0
        10.times do |i|
            count+=1 if F[n][i]==1 && F[n][i]==g[i]
        end
        r+=P[n][count]
    end
    ret=r if ret<r
end
puts ret
