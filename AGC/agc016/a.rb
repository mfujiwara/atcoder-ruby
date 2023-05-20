s = gets.chomp
array = s.split("").map {|c| 2**(c.ord - 97) }

ret = 0
while array.length > 1 do
    r = array[0]
    (1..(array.length-1)).each do |i|
        r = r & array[i]
        break if r == 0
    end
    if r != 0
        break
    else
        ret+=1
        next_array = []
        (0..(array.length-2)).each do |i|
            next_array.push(array[i] | array[i+1])
        end
        array = next_array
    end
end
puts ret
