X,Y,A,B,C=gets.chomp.split(" ").map(&:to_i)
p_array=gets.chomp.split(" ").map(&:to_i).sort.reverse[0..(X-1)].reverse
q_array=gets.chomp.split(" ").map(&:to_i).sort.reverse[0..(Y-1)].reverse
r_array=gets.chomp.split(" ").map(&:to_i).sort.reverse

loop do
    if r_array.length == 0
        break
    elsif (p_array[0] || 0) > (q_array[0] || 0)
        if q_array[0] < r_array[0]
            q_array.shift
            q_array.push(r_array[0])
            r_array.shift
        else
            break
        end
    else
        if p_array[0] < r_array[0]
            p_array.shift
            p_array.push(r_array[0])
            r_array.shift
        else
            break
        end
    end
end

puts p_array.inject(&:+) + q_array.inject(&:+)
