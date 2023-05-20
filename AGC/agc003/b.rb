N=gets.to_i
ret=0
pre_exsit=false
N.times do
    a=gets.to_i
    if pre_exsit && a>0
        a-=1
        ret+=1
    end
    ret+=a/2
    pre_exsit = a.odd?
end
puts ret
