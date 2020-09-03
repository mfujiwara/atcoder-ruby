S=gets.chomp.split("").map(&:to_i)
if S.length==1
    puts S
    exit
end
ret=0
S.each_with_index do |s,index|
    count=2**index

    ret+=s*(10**(S.length-index-1))*count
    (S.length-index-2).downto(0) do |l|
        ret+=s*(10**l)*count
        count*=2
    end
end
puts ret
