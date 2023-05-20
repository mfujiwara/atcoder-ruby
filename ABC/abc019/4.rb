N=gets.to_i
a=(2..N).map do |i|
  puts "? 1 #{i}"
  STDOUT.flush
  [gets.to_i, i]
end.max{|l,r| l[0]<=>r[0] }[1]
ret=(1..N).map do |i|
  if i==a
    0
  else
    puts "? #{a} #{i}"
    STDOUT.flush
    gets.to_i
  end
end.max
puts "! #{ret}"
