K=gets.to_i

MEMO={}
MEMO[1]=1
MEMO[2]=1
def fib(n)
    return MEMO[n] if MEMO[n]
    r=fib(n-1)+fib(n-2)
    MEMO[n]=r
    r
end

fib(K+1)

puts "#{MEMO[K]} #{MEMO[K+1]}"

# 確認用
# $counter=0
# def gcd(a, b)
#     return a if b==0
#     $counter+=1
#     gcd(b, a%b)
# end

# gcd(MEMO[K+1],MEMO[K])
# puts $counter
