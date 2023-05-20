N=gets.to_i
G={}
(N-1).times do
    a,b,c=gets.chomp.split(" ").map(&:to_i)
    G[a-1]||={}
    G[a-1][b-1]=c
    G[b-1]||={}
    G[b-1][a-1]=c
end
Q,K=gets.chomp.split(" ").map(&:to_i)
D=Array.new(N)
D[K-1]=0
targets=[K-1]
while !targets.empty? do
    nexts=[]
    targets.each do |v|
        G[v].each do |key,value|
            if D[key]==nil
                D[key]=D[v]+value
                nexts.push(key)
            end
        end
    end
    targets=nexts
end

Q.times do
    x,y=gets.chomp.split(" ").map(&:to_i)
    puts D[x-1]+D[y-1]
end
