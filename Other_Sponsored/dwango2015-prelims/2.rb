S=gets.chomp
ret=0
c=0
pre2=false
pre5=false
S.each_char do |s|
    if pre2
        if s=="5"
            pre2=false
            pre5=true
            c+=1
            ret+=c
        elsif s=="2"
            pre2=true
            c=0
        else
            pre2=false
            c=0
        end
    elsif pre5
        if s=="2"
            pre2=true
            pre5=false
        else
            pre5=false
            c=0
        end
    else
        pre2=true if s=="2"
    end
end
puts ret
