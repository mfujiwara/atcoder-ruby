H,N=gets.chomp.split(" ").map(&:to_i)
MAGICS={}
N.times do
    a,b=gets.chomp.split(" ").map(&:to_i)
    if MAGICS[a] == nil
        MAGICS[a] = b
    else
        MAGICS[a] = [MAGICS[a],b].min
    end
end
MEMO=Array.new(H+1,(1 << 31) - 1)
MEMO[H]=0
cursor=H
loop do
    break if cursor==0
    m=MEMO[cursor]
    MAGICS.each do |a,b|
        c = cursor - a
        if c < 0
            c = 0
        end
        if MEMO[c] > m+b
            MEMO[c]= m+b
        end
    end
    cursor-=1
end
puts MEMO[0]
