S=gets.chomp.split("")
len = S.length
ret = 0
S.each_with_index do |s, index|
    if s == "U"
        ret += index*2
        ret += len-1-index
    else
        ret += index*1
        ret += (len-1-index)*2
    end
end
puts ret
