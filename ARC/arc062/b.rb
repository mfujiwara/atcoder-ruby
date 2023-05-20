ret=0
gets.chomp.split("").each_with_index do |s,i|
    if i.even?
        ret-=1 if s=="p"
    else
        ret+=1 if s=="g"
    end
end
puts ret
