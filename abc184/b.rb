N,X=gets.chomp.split(" ").map(&:to_i)
S=gets.chomp
ret=X
N.times do |i|
    if S[i]=="o"
        ret+=1
    elsif ret > 0
        ret-=1
    end
end
puts ret
