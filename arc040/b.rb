N,R=gets.chomp.split(" ").map(&:to_i)
S=gets.chomp
last=nil
(N-1).downto(0).each do |i|
    if S[i] == "."
        last = i-R+1
        break
    end
end
if last == nil
    puts 0
    exit
end
last = 0 if last < 0
ret=0
c=0
while c < last do
    if S[c] == "."
        c+=R
        ret+=(R+1)
    else
        c+=1
        ret+=1
    end
end
if last < c
    ret -= (c-last)
end
puts ret+1
