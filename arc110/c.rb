N=gets.to_i
array=gets.chomp.split(" ").map(&:to_i)
pre=nil
nexts=nil
rets=[]
r=[]
target=1
array.each_with_index do |a,index|
    if pre!=nil
        if target==a
            nexts=pre
            pre=nil
            rets.push(r)
            r=[]
        else
            puts "-1"
            exit
        end
    end

    if nexts!=nil
        a=nexts
        nexts=nil
        target=index+1
    end
    
    if index+1==a
        puts "-1"
        exit
    elsif index+2==a
        r.push(index+1)
        next
    else
        r.push(index+1)
        pre=a
    end
end
r.pop
rets.push(r)
rets.each do |rr|
    (rr.length-1).downto(0).each do |i|
        puts rr[i]
    end
end
