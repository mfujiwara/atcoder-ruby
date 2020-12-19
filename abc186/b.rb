H,W=gets.chomp.split(" ").map(&:to_i)
minimum=100
sum=0
H.times do
  array=gets.chomp.split(" ").map(&:to_i)
  sum += array.inject(&:+)
  m = array.min
  minimum = m if minimum > m
end
puts sum - minimum*H*W
