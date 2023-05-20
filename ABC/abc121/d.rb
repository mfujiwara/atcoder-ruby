A,B=gets.chomp.split(" ").map(&:to_i)
s=""
n=0
a,b=A-1,B
while 2**n <= b  do
    nn = 2**(n+1)
    va = ((a+nn)/nn)*2**n - [2**n, nn-a%nn-1].min
    vb = ((b+nn)/nn)*2**n - [2**n, nn-b%nn-1].min
    d=vb-va
    s = (d.odd? ? "1" : "0") + s
    n+=1
end
puts s.to_i(2)
