A,B,X,Y=gets.chomp.split(" ").map(&:to_i)
if A==B
    puts X
    exit
end
INF=10**100
DPA=Array.new(101,INF)
DPB=Array.new(101,INF)
DPA[A]=0
DPB[A]=X
if A>B
    now = A-1
    while now >= B do
        b_from_b = DPB[now+1] + Y 
        b_from_a = DPA[now+1] + X
        DPB[now]= b_from_a < b_from_b ? b_from_a : b_from_b
        a_from_a = DPA[now+1] + Y
        a_from_b = DPB[now] + X
        DPA[now]= a_from_a < a_from_b ? a_from_a : a_from_b
        now-=1
    end
else
    now = A+1
    while now <= B do
        a_from_a = DPA[now-1] + Y
        a_from_b = DPB[now-1] + X
        DPA[now]= a_from_a < a_from_b ? a_from_a : a_from_b
        b_from_b = DPB[now-1] + Y 
        b_from_a = DPA[now] + X
        DPB[now]= b_from_a < b_from_b ? b_from_a : b_from_b
        now+=1
    end
end
puts DPB[B]
