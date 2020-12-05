require 'prime'
N=gets.to_i
r=1
(2..N).each do |n|
    Prime.prime_division(n).each do |p,e|
        pe=p**e
        while r%pe!=0 do
            r*=p
        end
    end
end
puts r+1
