N,X=gets.chomp.split(" ").map(&:to_i)
eaten=0
n=N
x=X
loop do
    nn = 2**(n+2)-3
    bottom = n
    center = 2**(n+1)-1
    upper = nn-n
    if x == center
        puts eaten + 2**n-1 + 1
        exit
    elsif x <= n
        puts eaten + 0
        exit
    elsif x > upper
        puts eaten + 2**(n+1)-1
        exit
    elsif x > center
        eaten += 2**n
        n-=1
        x-=center
    else
        n-=1
      	x-=1
    end
end
