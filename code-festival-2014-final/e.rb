N=gets.to_i
array=gets.chomp.split(" ").map(&:to_i)
b=[array[0], true, 1]
c=[array[0], false, 1]
(1..(N-1)).each do |i|
    [b,c].each do |a|
        if a[1]
            if a[0] < array[i]
                a[0] = array[i]
                a[1] = false
                a[2] += 1
            elsif a[0] > array[i]
                a[0] = array[i]
            end
        else
            if a[0] > array[i]
                a[0] = array[i]
                a[1] = true
                a[2] += 1
            elsif a[0] < array[i]
                a[0] = array[i]
            end
        end
    end
end
maxim = b[2] > c[2] ? b[2] : c[2]
puts  maxim >= 3 ? maxim : 0
