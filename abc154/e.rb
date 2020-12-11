N=gets.chomp
K=gets.to_i

DP_EQUL=Array.new(N.length+1){Array.new(K+1,0)}
DP_LESS=Array.new(N.length+1){Array.new(K+1,0)}
DP_EQUL[0][0]=1
N.each_char.with_index do |ch, i|
    x=ch.to_i
    (K+1).times do |k|
        DP_EQUL[i+1][k]+=DP_EQUL[i][k] if x==0
        DP_LESS[i+1][k]+=DP_LESS[i][k]
        DP_LESS[i+1][k]+=DP_EQUL[i][k] if x!=0
        if k>0
            DP_EQUL[i+1][k]+=DP_EQUL[i][k-1] if x>0
            DP_LESS[i+1][k]+=DP_LESS[i][k-1]*9
            DP_LESS[i+1][k]+=DP_EQUL[i][k-1]*(x-1) if x>0
        end
    end
end
puts DP_LESS[N.length][K]+DP_EQUL[N.length][K]
