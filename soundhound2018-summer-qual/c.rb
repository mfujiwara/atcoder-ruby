n,m,d=gets.chomp.split(" ").map(&:to_i)
r=0.0
if d==0
    r+=n
else
    r+=2*n
    r-=2*d
end
puts r*(m-1)/n/n
