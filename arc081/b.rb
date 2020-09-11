N=gets.to_i
S1=gets.chomp
S2=gets.chomp
MOD=10**9+7
pre=nil
c=0
ret=1
while c < N do
    if pre=="tate"
        if S1[c]==S2[c]
            ret*=2
            c+=1
        else
            ret*=2
            c+=2
            pre="yoko"
        end
    elsif pre=="yoko"
        if S1[c]==S2[c]
            ret*=1
            c+=1
            pre="tate"
        else
            ret*=3
            c+=2
        end
    else
        if S1[c]==S2[c]
            ret*=3
            c+=1
            pre="tate"
        else
            ret*=6
            c+=2
            pre="yoko"
        end
    end
    ret%=MOD
end
puts ret
