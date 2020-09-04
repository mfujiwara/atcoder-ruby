N,K=gets.chomp.split(" ").map(&:to_i)
ret=0
if K==0
    puts N*N
    exit
end
((K+1)..N).each do |b|
    n=(N+1)/b
    ret+=(b-K)*n
    rest=N-n*b
    if rest-K+1 > 0
        ret+= rest-K+1
    end
end
puts ret
