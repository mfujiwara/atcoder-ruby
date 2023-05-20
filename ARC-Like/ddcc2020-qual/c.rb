H,W,K=gets.chomp.split(" ").map(&:to_i)
rets=[]
count=1
H.times do
    ret=[]
    s=gets.chomp
    ss=s.split("#", -1)
    if ss.length > 1
        ret.push(Array.new(ss[0].length,count))
        (1..(ss.length-1)).each do |i|
            ret.push(Array.new(ss[i].length+1,count))
            count+=1
        end
    else
        ret = rets[-1] if !rets.empty?
    end
    rets.push(ret.flatten)
end
c=0
while rets[c].empty? do
    c+=1
end
c.times do
    puts rets[c].join(" ")
end
(c..(H-1)).each do |i|
    puts rets[i].join(" ")
end
