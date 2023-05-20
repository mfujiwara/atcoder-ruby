N,M=gets.chomp.split(" ").map(&:to_i)
paths=Array.new(N-1,0)
M.times do
    a,b=gets.chomp.split(" ").map(&:to_i)
    if a==1
        paths[b-2]+=1
    elsif b==1
        paths[a-2]+=1
    else
        paths[b-2]+=1
        paths[a-2]+=1
    end
end
puts paths.all?{|i| i.even? } ? "YES" : "NO"
