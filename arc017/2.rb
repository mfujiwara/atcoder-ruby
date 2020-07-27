N,K=gets.chomp.split(" ").map(&:to_i)
ret = 0
pre=gets.to_i
length=1
(N-1).times do
    now=gets.to_i
    if now > pre
        length+=1
    else
        ret+=(length-K+1) if length >= K
        length=1
    end
    pre = now
end
ret+=(length-K+1) if length >= K
puts ret
