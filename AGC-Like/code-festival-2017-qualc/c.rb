S=gets.chomp
cursor_s=0
cursor_e=S.length-1
ret = 0
loop do
    break if cursor_s >= cursor_e
    s = S[cursor_s]
    e = S[cursor_e]
    if s==e
        cursor_s+=1
        cursor_e-=1
    elsif s=="x"
        cursor_s+=1
        ret+=1
    elsif e=="x"
        cursor_e-=1
        ret+=1
    else
        puts "-1"
        exit
    end
end
puts ret
