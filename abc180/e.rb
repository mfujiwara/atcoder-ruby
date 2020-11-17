N=gets.to_i
DOTS=[]
N.times do
    x,y,z=gets.chomp.split(" ").map(&:to_i)
    DOTS.push([x,y,z])
end
INF=10**7
DP={}
DP[0]={}
DP[0][0]=0
s=2
while s<2**N do
    tmp=s/2
    d=1
    while tmp > 0 do
        if tmp%2==1
            DP[s]||={}
            x,y,z=DOTS[d]
            DP[s][d]=DP[s-2**d].map do |key,value|
                a,b,c=DOTS[key]
                value + (x-a).abs + (y-b).abs + (z<c ? 0 : z-c)
            end.min
        end
        tmp/=2
        d+=1
    end
    s+=2
end

x,y,z=DOTS[0]
ret = DP[2**N-2].map do |key,value|
    a,b,c=DOTS[key]
    value + (x-a).abs + (y-b).abs + (z<c ? 0 : z-c)
end.min

puts ret
