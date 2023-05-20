K=gets.to_i
if K.even?
    puts "-1"
    exit
end

c=1
n=7
loop do
    break if n%K==0 
    c+=1
    n=(n*10+7)%K
    if n==7 || c == K+1
        puts "-1"
        exit
    end
end
puts c
