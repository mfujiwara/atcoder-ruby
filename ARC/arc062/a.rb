N=gets.to_i
ret_t=1
ret_a=1
N.times do
  t,a=gets.chomp.split(" ").map(&:to_i)
  n_t=(ret_t-1)/t+1
  n_a=(ret_a-1)/a+1
  n = n_t>n_a ? n_t : n_a
  ret_t=n*t
  ret_a=n*a
end
puts ret_t+ret_a
