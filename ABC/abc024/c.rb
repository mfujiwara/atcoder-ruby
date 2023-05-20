N,D,K=gets.chomp.split(" ").map(&:to_i)
LR=[]
D.times do |i|
    l,r=gets.chomp.split(" ").map(&:to_i)
    LR.push([l,r])
end
ST=[]
K.times do |i|
    s,t=gets.chomp.split(" ").map(&:to_i)
    ST.push([i,s,t])
end
RETS=Array.new(K,nil)
LR.each_with_index do |lr, lri|
    l,r=lr
    n=lri+1

    delete_ats=[]
    ST.each_with_index do |st, sti|
        i,s,t=st
        if (l..r).include?(s)
            if s < t
                if t <= r
                    RETS[i]=n
                    delete_ats.push(sti)
                elsif s < r
                    ST[sti] = [i,r,t]
                end
            else
                if l <= t
                    RETS[i]=n
                    delete_ats.push(sti)
                elsif l < s
                    ST[sti] = [i,l,t]
                end
            end
        end
    end
    delete_ats.reverse.each do |di|
        ST.delete_at(di)
    end
end
RETS.each do |ret|
    puts ret
end
