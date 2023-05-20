X_a,Y_a,X_b,Y_b,T,V=gets.chomp.split(" ").map(&:to_i)
n = gets.to_i
L=T*V
def check(x,y)
    return L >= ((X_a-x)**2 + (Y_a-y)**2)**0.5 + ((X_b-x)**2 + (Y_b-y)**2)**0.5
end

n.times do
    x,y=gets.chomp.split(" ").map(&:to_i)
    if check(x,y)
        puts 'YES'
        exit
    end
end
puts 'NO'
