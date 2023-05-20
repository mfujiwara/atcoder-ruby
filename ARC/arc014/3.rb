N=gets.to_i
S=gets.chomp
r=0
g=0
b=0
N.times do |i|
    if S[i]=="R"
        r+=1
        r%=2
    elsif S[i]=="G"
        g+=1
        g%=2
    else
        b+=1
        b%=2
    end
end
puts r+g+b
