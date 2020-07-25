a,b,c=gets.chomp.split(" ").map(&:to_i)
k=gets.to_i
while a >= b && k > 0 do
    b *= 2
    k -= 1
end
while b >= c && k > 0 do
    c *= 2
    k -= 1
end

if a<b && b<c
    puts "Yes"
else
    puts "No"
end
