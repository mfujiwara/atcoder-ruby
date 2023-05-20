s=gets.chomp
T=gets.chomp
found = false
(s.length-T.length).downto(0) do |i|
    check = true
    T.length.times do |j|
        next if s[i+j] == T[j] || s[i+j] == "?"
        check = false
        break
    end
    if check
        T.length.times do |j|
            s[i+j] = T[j]
        end
        found = true
        break
    end
end
if found
    puts s.gsub(/\?/, 'a') 
else
    puts "UNRESTORABLE"
end
