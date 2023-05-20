N = gets.to_i
march = [0,0,0,0,0]
N.times do
    s = gets.chomp
    march[0] += 1 if s[0] == "M"
    march[1] += 1 if s[0] == "A"
    march[2] += 1 if s[0] == "R"
    march[3] += 1 if s[0] == "C"
    march[4] += 1 if s[0] == "H"
end
ret = 0
march.combination(3) do |array|
    ret += array[0] * array[1] * array[2]
end
puts ret
