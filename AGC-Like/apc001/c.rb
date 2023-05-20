N=gets.to_i
puts 0
STDOUT.flush
s=gets.chomp
exit if s=="Vacant"
start = s=="Male" ? 0 : 1

low=1
high=N-1
loop do
    mid = (low+high)/2
    puts mid
    STDOUT.flush
    s=gets.chomp
    exit if s=="Vacant"
    r = s=="Male" ? 0 : 1
    if start==0 && (mid+r).even? || start==1 && (mid+r).odd?
        low = mid+1
    else
        high = mid
    end
end
