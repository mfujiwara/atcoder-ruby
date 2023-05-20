N=gets.to_i
array=gets.chomp.split(" ").map(&:to_i)
money = 1000

index = 0
while index < N do
    mini = array[index]
    loop do
        if index < N-1 && array[index] > array[index+1]
            index += 1
            break if index >= N
            mini = array[index]
        else
            break
        end
    end

    index += 1
    break if index >= N
    

    maxi = array[index]
    loop do
        if index < N-1 && array[index] < array[index+1]
            index += 1
            break if index >= N
            maxi = array[index]
        else
            num = money / mini
            money += num*(maxi-mini)
            break
        end
    end
end
puts money
