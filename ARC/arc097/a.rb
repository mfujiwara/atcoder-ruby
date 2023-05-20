S=gets.chomp
K=gets.chomp.to_i
subs=[]
S.length.times do |i|
    l=0
    while l<K && i+l < S.length do
        subs.push(S[i..(i+l)])
        l+=1
    end
end
puts subs.sort.uniq[K-1]
