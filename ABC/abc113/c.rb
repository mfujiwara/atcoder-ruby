N,M=gets.chomp.split(" ").map(&:to_i)
KEYS=[]
M.times do
    x,y=gets.chomp.split(" ").map(&:to_i)
    KEYS.push([x,y])
end
groups={}
KEYS.each do |x,y|
    groups[x] ||= []
    groups[x].push(y)
end
ORDERS={}
groups.keys.each do |x|
    groups[x] = groups[x].sort
    groups[x].each_with_index do |y,index|
        key="#{x}_#{y}"
        ORDERS[key]=index+1
    end
end
KEYS.each do |x,y|
    key="#{x}_#{y}"
    puts "#{format('%06d', x)}#{format('%06d', ORDERS[key])}"
end
