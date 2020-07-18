N=gets.to_i

queue357 = [3, 5, 7]
queue35 = [3, 5]
queue37 = [3, 7]
queue57 = [5, 7]
queue3 = [3]
queue5 = [5]
queue7 = [7]

count357 = 0
while !queue357.empty? do
    n = queue357.shift
    if n <= N
        count357 += 1
        queue357.push(n*10+3)
        queue357.push(n*10+5)
        queue357.push(n*10+7)
    end
end

count35 = 0
while !queue35.empty? do
    n = queue35.shift
    if n <= N
        count35 += 1
        queue35.push(n*10+3)
        queue35.push(n*10+5)
    end
end

count37 = 0
while !queue37.empty? do
    n = queue37.shift
    if n <= N
        count37 += 1
        queue37.push(n*10+3)
        queue37.push(n*10+7)
    end
end

count57 = 0
while !queue57.empty? do
    n = queue57.shift
    if n <= N
        count57 += 1
        queue57.push(n*10+5)
        queue57.push(n*10+7)
    end
end

count3 = 0
while !queue3.empty? do
    n = queue3.shift
    if n <= N
        count3 += 1
        queue3.push(n*10+3)
    end
end

count5 = 0
while !queue5.empty? do
    n = queue5.shift
    if n <= N
        count5 += 1
        queue5.push(n*10+5)
    end
end

count7 = 0
while !queue7.empty? do
    n = queue7.shift
    if n <= N
        count7 += 1
        queue7.push(n*10+7)
    end
end

puts count357 - count35 - count37 - count57 + count3 + count5 + count7
