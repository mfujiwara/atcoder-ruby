N=gets.to_i
array=gets.chomp.split(" ").map(&:to_i)
l_gcd=[array[0]]
r_gcd=[array[-1]]
(1..(N-2)).each do |i|
    l_gcd.push(l_gcd[i-1].gcd(array[i]))
    r_gcd.unshift(r_gcd[0].gcd(array[N-1-i]))
end
M=[]
N.times do |i|
    if i==0
        M.push(r_gcd[i])
    elsif i==N-1
        M.push(l_gcd[i-1])
    else
        M.push(l_gcd[i-1].gcd(r_gcd[i]))
    end
end
puts M.max
