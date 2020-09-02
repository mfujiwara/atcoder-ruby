N=gets.to_i
ret=0
c=1
nobori=true
pre=gets.to_i
(N-1).times do
    h=gets.to_i
    if nobori
        c+=1
        if pre > h
            nobori=false
        end
    else
        if h < pre
            c+=1
        else
            ret=c if ret<c
            c=2
            nobori=true
        end
    end
    pre=h
end
ret=c if ret<c
puts ret
