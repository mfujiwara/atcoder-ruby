N,K=gets.chomp.split(" ").map(&:to_i)
S=gets.chomp

c=1
lands=[]
ret=0
sum=0
(1..(N-1)).each do |i|
    if S[i]==S[i-1]
        c+=1
    else
        lands.push(c)
        sum+=c
        if S[i]=="0"
            sum -= lands[-2*K-2] if lands.length > 2*K+1
            sum -= lands[-2*K-3] if lands.length > 2*K+2
            ret = sum if ret < sum
        end
        c=1
    end
end
lands.push(c)
sum+=c
if S[N-1]=="0"
    sum -= lands[-2*K-1] if lands.length > 2*K
    sum -= lands[-2*K-2] if lands.length > 2*K+1
    ret = sum if ret < sum
else
    sum -= lands[-2*K-2] if lands.length > 2*K+1
    sum -= lands[-2*K-3] if lands.length > 2*K+2
    ret = sum if ret < sum
end
puts ret
