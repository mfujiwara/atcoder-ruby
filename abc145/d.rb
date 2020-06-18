X,Y=gets.chomp.split(" ").map(&:to_i)
x=2*X-Y
y=2*Y-X
if x<0 || y<0 || x%3!=0 || y%3!=0
    puts 0
    exit
end
x/=3
y/=3
MOD=10**9+7
def ppow(x, n)
    return 1 if n == 0
    return ppow(x**2 % MOD, n / 2) if (n % 2) == 0
    return ppow(x**2 % MOD, n / 2) * x if (n % 2) == 1
end

def kaijou(a, b)
    (b..a).inject(1) {|i,j| i*j % MOD }
end

puts (kaijou(y+x,y+1) * ppow(kaijou(x,1),MOD-2)) % MOD
