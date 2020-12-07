N,K=gets.chomp.split(" ").map(&:to_i)
def min(a,b)
    return a > b ? b : a
end
def max(a,b)
    return a > b ? a : b
end
array=gets.chomp.split(" ").map(&:to_i)
K.times do
    nexts=Array.new(N+1,0)
    array.each_with_index do |a,i|
        lower = max(i-a,0)
        upper = min(i+a,N-1)
        nexts[lower]+=1
        nexts[upper+1]-=1
    end
    c=0
    (0..(N-1)).each do |i|
        c+=nexts[i]
        array[i]=c
    end
    break if array.all?{ |a| a==N }
end
puts array.join(" ")
