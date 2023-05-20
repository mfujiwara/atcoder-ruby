N=gets.to_i
abs=[]
N.times do
    a,b=gets.chomp.split(" ").map(&:to_i)
    abs.push([a,b])
end
abs=abs.sort_by{|a,b| -a-b}

ret=0
abs.each_with_index do |ab, index|
    a,b=ab
    if index%2==0
        ret += a
    else
        ret -= b
    end
end
puts ret
