A,B=gets.chomp.split(" ").map(&:to_i)

ret = 0
ret += ( (B-A+1)/4 + ((A-1)%4>B%4 ? 1 : 0) )
ret -= ( (B-A+1)/100 + ((A-1)%100>B%100 ? 1 : 0) )
ret += ( (B-A+1)/400 + ((A-1)%400>B%400 ? 1 : 0) )
puts ret
