A,B,C=gets.chomp.split(" ").map(&:to_i).sort
DP={}
DP[[99,99,99]]=1
99.downto(C) do |a|
    a.downto(B) do |b|
        b.downto(A) do |c|
            next if a==99 && b==99 && c== 99
            sum= a.to_f + b.to_f + c.to_f
            if a==99 && b==99
                tmp=(c.to_f/sum)*(1+DP[[c+1,99,99]]) + (a.to_f + b.to_f)/sum
                DP[[a,b,c]]=tmp
                DP[[a,c,b]]=tmp
                DP[[c,b,a]]=tmp
            elsif a==99
                tmp=(c.to_f/sum)*(1+DP[[99,b,c+1]]) + (a.to_f/sum)+ (b.to_f/sum)*(1+DP[[99,b+1,c]])
                DP[[a,b,c]]=tmp
                DP[[a,c,b]]=tmp
                DP[[b,a,c]]=tmp
                DP[[b,c,a]]=tmp
                DP[[c,a,b]]=tmp
                DP[[c,b,a]]=tmp
            else
                tmp=(c.to_f/sum)*(1+DP[[a,b,c+1]]) + (a.to_f/sum)*(1+DP[[a+1,b,c]])+ (b.to_f/sum)*(1+DP[[a,b+1,c]])
                DP[[a,b,c]]=tmp
                DP[[a,c,b]]=tmp
                DP[[b,a,c]]=tmp
                DP[[b,c,a]]=tmp
                DP[[c,a,b]]=tmp
                DP[[c,b,a]]=tmp
            end
        end
    end
end
p DP[[A,B,C]]
