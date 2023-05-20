require 'prime'
N=gets.to_i

ret =0
(1..N).each do |n|
    y = N/n
    ret+=y*(y+1)*n/2
end
puts ret
