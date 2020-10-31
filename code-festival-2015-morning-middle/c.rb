N,K,M,R=gets.chomp.split(" ").map(&:to_i)
req=K*R
ss=[]
(N-1).times do
    s=gets.to_i
    ss.push(s)
end
if K==N
    sum=ss.inject(&:+) || 0
    if sum >= req
        puts 0
    else
        diff=req-sum
        if diff>M
            puts -1
        else
            puts diff
        end
    end
else
    ss=ss.sort.reverse
    sum=ss[0..(K-1)].inject(&:+) || 0
    if sum>= req
        puts 0
    else
        diff=req-sum
        if diff>M-ss[K-1]
            puts -1
        else
            puts diff+ss[K-1]
        end
    end
end
