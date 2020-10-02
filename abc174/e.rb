N,K=gets.chomp.split(" ").map(&:to_i)
array=gets.chomp.split(" ").map(&:to_i).sort
low=1
high=array[-1]
loop do
    if low==high
        puts low
        exit
    end
    mid = (low+high)/2
    k = array.map{|a| (a-1)/mid }.inject(&:+)
    if k<=K
        high=mid
    else
        low=mid+1
    end
end
