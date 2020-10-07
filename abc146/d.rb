N=gets.to_i
T={}
ARRAY=[]
(N-1).times do |i|
    a,b=gets.chomp.split(" ").map(&:to_i)
    ARRAY.push([a,b])
    T[a]||={}
    T[b]||={}
    T[a][b]=i
end
RET=Array.new(N-1)
PARENT={}
max=T[1].keys.length
c=1
T[1].each do |key,value|
    PARENT[key]=c
    RET[value]=c
    c+=1
end
(2..(N-1)).each do |i|
    mm=T[i].keys.length+1
    max=mm if max<mm
    c=1
    T[i].each do |key,value|
        c+=1 if PARENT[i]==c
        PARENT[key]=c
        RET[value]=c
        c+=1
    end
end
puts max
RET.each {|r| puts r}
