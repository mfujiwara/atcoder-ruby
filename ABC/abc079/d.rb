H,W=gets.chomp.split(" ").map(&:to_i)
C=[]
(0..9).each do |i|
    c = gets.chomp.split(" ").map(&:to_i)
    C.push(c)
end
min_c = Array.new(10, 10**4)
min_c[1] = 0
nows = [1]
while !nows.empty? do
    nexts = []
    nows.each do |n|
        (0..9).each do |i|
            c = C[i][n] + min_c[n]
            if min_c[i] > c
                min_c[i] = c
                nexts.push(i)
            end
        end
    end
    nows = nexts
end
ret = 0
H.times do
    array = gets.chomp.split(" ").map(&:to_i)
    array.each do |a|
        next if a == 1 || a == -1
        ret += min_c[a]
    end
end
puts ret
