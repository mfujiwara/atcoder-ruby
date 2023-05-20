N=gets.to_i
a_array=gets.chomp.split(" ").map(&:to_i)
b_array=gets.chomp.split(" ").map(&:to_i)

d_array=[]
(0..(N-1)).each do |n|
    d_array.push(a_array[n] - b_array[n])
end
d_array = d_array.sort

minus_sum = 0
minus_count = 0
while d_array[minus_count] < 0 do
    minus_sum += d_array[minus_count]
    minus_count+=1
end

plus_count=0
while minus_sum < 0 do
    plus_count += 1
    break if d_array[-1 * plus_count] <= 0
    minus_sum += d_array[-1 * plus_count]
end

if minus_sum >= 0
    puts minus_count + plus_count
else
    puts "-1"
end
