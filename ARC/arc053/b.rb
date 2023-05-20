S=gets.chomp
odd_size = S.split("").group_by{|c|c}.select{|k,v| v.length.odd? }.length
even_size = (S.length-odd_size)/2

if odd_size <= 1
    puts S.length
else
    puts (even_size/odd_size)*2 + 1
end
