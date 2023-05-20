N,M=gets.chomp.split(" ").map(&:to_i)
input = []
output = []
N.times do
    input.push(gets.chomp.split("").map(&:to_i))
end

output.push(Array.new(M,0))
(1..(N-2)).each do |i|
    output.push([])
    (0..(M-1)).each do |j|
        if j==0 || j==M-1
            output[i].push(0)
        else
            n = input[i-1][j]
            output[i].push(n)
            input[i-1][j]-=n
            input[i+1][j]-=n
            input[i][j+1]-=n
            input[i][j-1]-=n
        end
    end
end
output.push(Array.new(M,0))

output.each do |line|
    puts line.join("")
end
