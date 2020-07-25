N=gets.to_i
XL=[]
N.times do
    x,l=gets.chomp.split(" ").map(&:to_i)
    XL.push([x-l,x+l])
end
ranges = XL.sort_by {|s,t| t }

ret = 0
max_x = -1 * 10**10
ranges.each do |s,t|
    if max_x <= s
        max_x = t
        ret += 1
    end
end
puts ret
