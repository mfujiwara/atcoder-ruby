H,W=gets.chomp.split(" ").map(&:to_i)
S=[]
H.times do
    s=gets.chomp
    S.push(s)
end
def kuro?(r,c)
    if r<H-1
        return false if c<W-1 && S[r+1][c+1]=="."
        return false if S[r+1][c]=="."
        return false if 0<c && S[r+1][c-1]=="."
    end
    return false if c<W-1 && S[r][c+1]=="."
    return false if S[r][c]=="."
    return false if 0<c && S[r][c-1]=="."
    if 0<r
        return false if c<W-1 && S[r-1][c+1]=="."
        return false if S[r-1][c]=="."
        return false if 0<c && S[r-1][c-1]=="."
    end
    return true
end
def drawU(r,c)
    if r<H-1
        U[r+1][c+1]="#" if c<W-1
        U[r+1][c]="#"
        U[r+1][c-1]="#" if 0<c
    end
    U[r][c+1]="#" if c<W-1
    U[r][c]="#"
    U[r][c-1]="#" if 0<c
    if 0<r
        U[r-1][c+1]="#" if c<W-1
        U[r-1][c]="#"
        U[r-1][c-1]="#" if 0<c
    end
end
T=Array.new(H) { "."*W }
U=Array.new(H) { "."*W }
H.times do |h|
    W.times do |w|
        if kuro?(h,w)
            T[h][w]="#"
            drawU(h,w)
        end
    end
end
if S==U
    puts "possible"
    T.each do |t|
        puts t
    end
else
    puts "impossible"
end
