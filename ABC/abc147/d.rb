N=gets.to_i
array=gets.chomp.split(" ").map(&:to_i)
bit_sum=Array.new(60, 0)
array.each do |a|
    i=0
    while a > 0 do
        if a%2==1
            bit_sum[i]+=1
        end
        a/=2
        i+=1
    end
end

MOD=10**9+7
ret=0
base=1
60.times do |i|
    r=(N-bit_sum[i])*bit_sum[i]
    ret+=r*base
    ret%=MOD
    base*=2
end
puts ret
