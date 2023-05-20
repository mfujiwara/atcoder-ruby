S=gets.chomp
ret=0
a_count=0
b_of_bc=false
S.length.times do |i|
    s=S[i]
    if s=="A"
        if b_of_bc
            a_count=1
        else
            a_count+=1
        end
        b_of_bc=false
    elsif s=="B"
        a_count=0 if b_of_bc
        b_of_bc=true
    else
        if b_of_bc
            ret+=a_count
        else
            a_count=0
        end
        b_of_bc=false
    end
end
puts ret
