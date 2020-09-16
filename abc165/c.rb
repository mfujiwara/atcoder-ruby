N,M,Q=gets.chomp.split(" ").map(&:to_i)
AS=(1..M).to_a.repeated_combination(N).to_a
rets=Array.new(AS.length,0)
ret=0
Q.times do
    a,b,c,d=gets.chomp.split(" ").map(&:to_i)
    AS.each_with_index do |array,i|
        rets[i]+=d if array[b-1]-array[a-1]==c
        ret=rets[i] if ret<rets[i]
    end
end
puts ret
