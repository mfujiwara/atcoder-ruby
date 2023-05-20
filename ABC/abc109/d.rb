H,W=gets.chomp.split(" ").map(&:to_i)
rets=[]
cf=false
H.times do |h|
    array=gets.chomp.split(" ").map(&:to_i)
    array[-1]+=1 if cf
    cf=false
    W.times do |w|
        break if h==H-1 && w==W-1
        if array[w].odd?
            if w+1==W
                cf=true
                rets.push("#{h+1} #{w+1} #{h+2} #{w+1}")
            else
                array[w+1]+=1
                rets.push("#{h+1} #{w+1} #{h+1} #{w+2}")
            end
        end
    end
end
puts rets.length
rets.each {|r| puts r}
