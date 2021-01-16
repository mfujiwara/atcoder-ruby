N=gets.to_i
a_array=gets.chomp.split(" ").map(&:to_i)
b_array=gets.chomp.split(" ").map(&:to_i)
a_max=a_array[0]
b_max=b_array[0]
ab_max=a_max*b_max
puts ab_max
(1..(N-1)).each do |i|
  if a_max<a_array[i]
    a_max=a_array[i]
    b_max=b_array[i]
  elsif b_max<b_array[i]
    b_max=b_array[i]
  end
  ab=a_max*b_max
  if ab>ab_max
    ab_max=ab
  end
  puts ab_max
end
