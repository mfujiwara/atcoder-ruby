N=gets.to_i
CSFS=[]
(N-1).times do
    c,s,f=gets.chomp.split(" ").map(&:to_i)
    CSFS.push([c,s,f])
end

MEMO={}
def calc(n, second)
    key = "#{n}_#{second}"
    return MEMO[key] if MEMO[key]

    c,s,f=CSFS[n]
    if s >= second
        ret = s+c
        MEMO[key] = ret
        return ret
    else
        rest=second%f
        ret = rest==0 ? second+c : second+f-rest+c
        MEMO[key] = ret
        return ret
    end
end

rets=[0]
while rets.length < N do
    rets = rets.map {|r| calc(rets.length-1, r) }
    rets.push(0)
end
rets.each do |r|
    puts r
end
