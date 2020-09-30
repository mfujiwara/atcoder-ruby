N=gets.to_i
a_array=gets.chomp.split(" ").map(&:to_i)
b_array=gets.chomp.split(" ").map(&:to_i)

a_add=0
b_add=0
N.times do |i|
    a=a_array[i]
    b=b_array[i]
    next if a==b
    if a>b
        b_add+=(a-b)
    else
        diff=b-a
        if diff.even?
            a_add+=diff/2
        else
            a_add+=(diff+1)/2
            b_add+=1
        end
    end
end
if a_add<b_add
    puts "No"
else
    puts "Yes"
end
