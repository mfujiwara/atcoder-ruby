N=gets.to_i
ranges=[]
N.times do
  a,b=gets.chomp.split(" ").map(&:to_i)
  ranges.push(a..b)
end
if N.even?
  sorted_min=ranges.map(&:first).sort
  me_min_low=sorted_min[N/2-1]
  me_min_high=sorted_min[N/2]
  sorted_max=ranges.map(&:last).sort
  me_max_low=sorted_max[N/2-1]
  me_max_high=sorted_max[N/2]
  puts me_max_low+me_max_high-me_min_low-me_min_high+1
else
  me_min=ranges.map(&:first).sort[(N-1)/2]
  me_max=ranges.map(&:last).sort[(N-1)/2]
  puts me_max-me_min+1
end
