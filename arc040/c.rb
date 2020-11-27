N=gets.to_i
ret=0
pre=N
N.times do
    s=gets.chomp
    done=false
    (pre-1).downto(0) do |i|
        if s[i]=="."
            pre=i
            ret+=1
            done=true
            break
        end
    end
    pre=N unless done
end
puts ret
