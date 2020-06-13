X=gets.chomp
s_num = 0
t_num = 0
(0..(X.length-1)).each do |i|
    if X[i] == "T"
        if s_num > 0
            s_num-=1
        else
            t_num+=1
        end
    else
        s_num+=1
    end
end
puts s_num*2
