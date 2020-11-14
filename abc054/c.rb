N,M=gets.chomp.split(" ").map(&:to_i)
EDGES=Array.new(N) {Array.new(N,false)}
M.times do
    a,b=gets.chomp.split(" ").map(&:to_i)
    EDGES[a-1][b-1]=true
    EDGES[b-1][a-1]=true
end
ret=0
(1..(N-1)).to_a.permutation(N-1) do |perm|
    next unless EDGES[0][perm[0]]
    r=true
    pre=0
    perm.each do |d|
        unless EDGES[pre][d]
            r=false
            break
        end
        pre=d
    end
    ret+=1 if r
end
puts ret
