N=gets.to_i
if N.odd?
    puts 0
    exit
end
ret=0
(1..25).each do |e|
    ret+=(N/5**e)/2
end
puts ret
