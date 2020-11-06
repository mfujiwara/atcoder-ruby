n=gets.to_i
if n==0
    puts "0"
    exit
end
ret=""
while n!=0 do
    if n.even?
        ret="0"+ret
        n/=2
    else
        ret="1"+ret
        n/=2
        n+=1 if ret.length.even?
    end
end
puts ret
