N=gets.to_i
RET=[]
def calc(n, rest, now)
    if n==0
        RET.push(rest/2 + now) if rest.even? && rest < 20
        return true
    else
        return false if 10**(n+1)-1+9*(n+1) < rest
        9.downto(0).each do |i|
            v = (10**n)*i+i
            next if rest < v
            r=calc(n-1, rest-v, now+(10**n)*i)
            break if r==false
        end
        return true
    end
end

calc(18,N,0)

puts RET.length
RET.sort.each do |r|
    puts r
end
