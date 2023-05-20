N,X,Y=gets.chomp.split(" ").map(&:to_i)
rets = Array.new(N-1, 0)
(1..(N-1)).each do |s|
    ((s+1)..(N)).each do |t|
        direct = t-s
        bypass = (X-s).abs + (Y-t).abs + 1
        if direct > bypass
            rets[bypass-1]+=1
        else
            rets[direct-1]+=1
        end
    end
end
rets.each {|r| puts r }
