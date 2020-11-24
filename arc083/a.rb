A,B,C,D,E,F=gets.chomp.split(" ").map(&:to_i)
f100=F/100
waters=Array.new(f100+1,false)
waters[0]=true
(0..f100).each do |i|
    if waters[i]
        waters[i+A]=true if i+A<=f100
        waters[i+B]=true if i+B<=f100
    end
end
ws=[]
(1..(F-1)).each do |i|
    ws.push(i) if waters[i]
end
sugars=Array.new(F,false)
sugars[0]=true
(0..(F-1)).each do |i|
    if sugars[i]
        sugars[i+C]=true if i+C<F
        sugars[i+D]=true if i+D<F
    end
end
ss=[]
(0..(F-1)).each do |i|
    ss.push(i) if sugars[i]
end
ss=ss.reverse
ret=0.0
rets=[A*100, 0]
ws.each do |w|
    rs = ss.bsearch {|s| s <= w*E && s+100*w<=F}
    next unless rs
    r=rs.to_f/(rs+100*w)
    if ret<r
        ret=r
        rets=[rs+w*100, rs]
    end
end
puts "#{rets[0]} #{rets[1]}"
