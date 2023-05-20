N=gets.to_i
pre=nil
ret=0
N.times do
    limit= (pre || -1) + 1
    a=gets.to_i
    if limit < a
        puts "-1"
        exit
    end
    if a==limit && a>0
        ret+=1
    else
        ret+=a
    end
    pre=a
end
puts ret
