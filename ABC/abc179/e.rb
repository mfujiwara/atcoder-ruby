N,X,M=gets.chomp.split(" ").map(&:to_i)
MEMO=Array.new(M,nil)
ARRAY=[X]
ret=X
n=1
x=X
while n < N do
    r=x*x%M
    if MEMO[r] != nil
        d=ret-ARRAY[MEMO[r]-1]
        m=(N-n)/(n-MEMO[r])
        l=(N-n)%(n-MEMO[r])
        ret+=(d*m + ARRAY[MEMO[r]-1+l]-ARRAY[MEMO[r]-1])
        break
    else
        MEMO[r]=n
        ret+=r
        ARRAY.push(ret)
    end
    n+=1
    x=r
end
puts ret
