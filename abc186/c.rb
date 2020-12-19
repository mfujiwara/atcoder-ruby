N=gets.to_i
ret=0
(1..N).each do |n|
  ret+=1 if !n.to_s.include?("7") && !n.to_s(8).include?("7")
end
puts ret
