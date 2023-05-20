N=gets.to_i
array=[]
N.times do
    a=gets.to_i
    array.push(a)
end
array=array.sort
ret1=0
array.each_with_index do |a, i|
    if (i+1)*2 < N
        ret1-=2*a
    elsif (i+1)*2 == N
        ret1-=a
    elsif i*2-1<=N
        ret1+=a
    else
        ret1+=2*a
    end
end
ret2=0
array.reverse.each_with_index do |a, i|
    if (i+1)*2 < N
        ret2+=2*a
    elsif (i+1)*2 == N
        ret2+=a
    elsif i*2-1<=N
        ret2-=a
    else
        ret2-=2*a
    end
end
puts ret1 > ret2 ? ret1 : ret2
