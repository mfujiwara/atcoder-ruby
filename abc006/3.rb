N,M=gets.chomp.split(" ").map(&:to_i)
r2,r3,r4=0,0,0
n=N
m=M
if M.odd?
    r3=1
    n-=1
    m-=3
end
if m < n*2 || n*4 < m
    puts "-1 -1 -1 "
    exit
end
r4=(m-n*2)/2
r2=n-r4
puts "#{r2} #{r3} #{r4}"
