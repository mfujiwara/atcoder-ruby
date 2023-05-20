K=gets.to_i

MEMO={}
COUNT={}
L_MAX={}
def count(k, n)
    return 1 if k == 0
    key = "#{k}_#{n}"
    return COUNT[key] if COUNT[key]

    ret = 0
    ret += count(k-1, n+1) if n != 9
    ret += count(k-1, n)
    ret += count(k-1, n-1) if n != 0
    COUNT[key] = ret
    return ret
end

def lunlun_max(k,n)
    return n if k == 0
    key = "#{k}_#{n}"
    return L_MAX[key] if L_MAX[key]

    base = n*10**k
    ret = nil
    if n == 9
        ret = base + lunlun_max(k-1,9)
    else
        ret = base + lunlun_max(k-1,n+1)
    end
    L_MAX[k] = ret
    return ret
end

MEMO[0] = 0
max_i = 0
max_pre_i = 0
break_flg = false
k=0
loop do
    (1..9).each do |i|
        c = count(k,i)
        max_i = lunlun_max(k,i)
        ret = MEMO[max_pre_i] + count(k,i)
        MEMO[max_i] = ret
        max_pre_i = max_i

        if ret >= K
            break_flg = true
            break
        end
    end
    break if break_flg
    k+=1
end

sup = max_i
inf = max_pre_i
rets = Array.new(k+1, nil)
rets[k] = max_i.to_s[0].to_i
k -= 1
memo = MEMO[sup]
loop do
    break if k < 0
    if rets[k+1] != 9
        c = count(k, rets[k+1]+1)
        if memo -c < K
            rets[k] = rets[k+1]+1
            k-=1
            next
        end
        memo -= c
    end

    c = count(k, rets[k+1])
    if memo -c < K
        rets[k] = rets[k+1]
        k-=1
        next
    end
    memo -= c

    c = count(k, rets[k+1])
    if rets[k+1] != 0
        c = count(k, rets[k+1]-1)
        rets[k] = rets[k+1]-1
        k-=1
        next
    end
end

ret = 0
rets.reverse.each do |i|
    ret *= 10
    ret += i
end
puts ret
