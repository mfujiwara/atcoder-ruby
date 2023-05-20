MOD=10**9+7
H,W=gets.chomp.split(" ").map(&:to_i)
MAP=[]
H.times do
    s=gets.chomp
    MAP.push(s)
end
X=Array.new(H){Array.new(W,0)}
Y=Array.new(H){Array.new(W,0)}
Z=Array.new(H){Array.new(W,0)}
RETS=Array.new(H){Array.new(W,0)}
RETS[0][0]=1
MAP.each_with_index do |ss, h|
    ss.each_char.with_index do |ch, w|
        next if (h==0 && w==0) || ch==?#
        if w>0
            X[h][w]=(X[h][w-1]+RETS[h][w-1])%MOD
        end
        if h>0
            Y[h][w]=(Y[h-1][w]+RETS[h-1][w])%MOD
        end
        if w>0 && h>0
            Z[h][w]=(Z[h-1][w-1]+RETS[h-1][w-1])%MOD
        end
        RETS[h][w]=(X[h][w]+Y[h][w]+Z[h][w])%MOD
    end
end
puts RETS[-1][-1]
