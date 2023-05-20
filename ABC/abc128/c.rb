N,M=gets.chomp.split(" ").map(&:to_i)
bulbs=[]
M.times do
    array=gets.chomp.split(" ").map{|s| s.to_i - 1}
    k=array.shift
    bulbs.push(array)
end
p_array=gets.chomp.split(" ").map(&:to_i)
ret=0
[0,1].repeated_permutation(N) do |perm|
    r=true
    bulbs.each_with_index do |swiches, index|
        count=0
        swiches.each do |swich|
            count+=perm[swich]
        end
        if count%2!=p_array[index]
            r=false
            break
        end
    end
    ret+=1 if r
end
puts ret
