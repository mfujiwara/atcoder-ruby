N=gets.to_i
array=gets.chomp.split(" ").map(&:to_i)

b_array=Array.new(N,0)
N.downto(1) do |i|
    sum = 0
    target = i*2
    while target <= N do
        sum = (sum + b_array[target-1])%2
        target += i
    end
    if sum != array[i-1]
        b_array[i-1]=1
    end
end

m = 0
rets = []
b_array.each_with_index do |b,index|
    if b != 0
        m += 1
        rets.push(index+1)
    end
end
puts m
puts rets.join(" ") if m > 0
