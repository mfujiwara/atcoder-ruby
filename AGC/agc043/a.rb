H,W=gets.chomp.split(" ").map(&:to_i)
MEMO = Array.new(H) { Array.new(W,nil) }
S=[]
H.times do |h|
    s=gets.chomp
    S.push(s)
    W.times do |w|
        if h==0
            if w==0
                MEMO[0][0] = s[0]=="." ? 0 : 1
            else
                MEMO[0][w] = ((s[w]=="." || s[w]==s[w-1]) ? 0 : 1) + MEMO[0][w-1]
            end
        else
            if w==0
                MEMO[h][0] = ((s[0]=="." || s[0]==S[h-1][0]) ? 0 : 1) + MEMO[h-1][0]
            else
                from_up = ((s[w]=="." || s[w]==S[h-1][w]) ? 0 : 1) + MEMO[h-1][w]
                from_left= ((s[w]=="." || s[w]==s[w-1]) ? 0 : 1) + MEMO[h][w-1]
                MEMO[h][w] = (from_up < from_left) ? from_up : from_left
            end
        end
    end
end
puts MEMO[H-1][W-1]
