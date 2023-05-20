N=gets.to_i
array=gets.chomp.split(" ").map(&:to_i)
MOD=10**9+7
sum=Array.new(N,0)
array.each do |a|
    sum[a]+=1
end
ret = 1
sum.each_with_index do |s, i|
    if N.even?
        if i.even?
            if s != 0
                puts 0
                exit
            end
        else
            if s != 2
                puts 0
                exit
            end
            ret *= 2
            ret %= MOD
        end
    else
        if i == 0
            if s != 1
                puts 0
                exit
            end
        elsif i.even?
            if s != 2
                puts 0
                exit
            end
            ret *= 2
            ret %= MOD
        else
            if s != 0
                puts 0
                exit
            end            
        end        
    end
end
puts ret