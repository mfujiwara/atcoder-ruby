N=gets.to_i
S=gets.chomp
ret=""
h=0
(N-1).downto(0) do |n|
    if S[n]=="("
        if h>0
            ret="("+ret
            h-=1
        else
            ret="("+ret+")"
        end
    else
        h+=1
        ret=")"+ret
    end
end
puts "("*h+ret
