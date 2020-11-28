N,K=gets.chomp.split(" ").map(&:to_i)
s=gets.chomp.split("")
K.times do
    ss = s + s
    s = (0..(N-1)).to_a.map do |i|
        a=ss[i*2]
        b=ss[i*2+1]
        if a==b
            a
        else
            if a=="R"
                if b=="P"
                    b
                else
                    a
                end
            elsif a=="P"
                if b=="R"
                    a
                else
                    b
                end
            else
                if b=="R"
                    b
                else
                    a
                end
            end
        end
    end
end
puts s[0]
