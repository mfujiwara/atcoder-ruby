N=gets.to_i
count=0
count_a=0
count_b=0
count_ab=0
N.times do
    s=gets.chomp
    (0..(s.length-2)).each do |i|
        count+=1 if s[i] == "A" && s[i+1] == "B"
    end
    if s[-1] == "A"
        if s[0] == "B"
            count_ab+=1
        else
            count_a+=1
        end
    else
        if s[0] == "B"
            count_b+=1
        end
    end
end
if count_ab > 0
    if count_a > 0
        if count_b > 0
            count+=(count_ab+1)
            count += (count_a > count_b ? count_b-1 : count_a-1)
        else
            count+=count_ab
        end
    else
        if count_b > 0
            count+=count_ab
        else
            count+=(count_ab-1)
        end
    end
else
    count += (count_a > count_b ? count_b : count_a)
end
puts count
