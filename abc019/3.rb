N=gets.to_i
array=gets.chomp.split(" ").map(&:to_i).sort.reverse
ret=0
MEMO={}
array.each do |a|
    if MEMO[a]
        next
    else
        MEMO[a]=1
        while a.even? do
            a=a/2
            MEMO[a]=1
        end
        ret+=1
    end
end
puts ret
