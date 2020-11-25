N=gets.to_i
abs=[]
N.times do
    a,b=gets.chomp.split(" ").map(&:to_i)
    abs.push([a,b])
end
abs=abs.sort_by {|a,b| a }
cds=[]
N.times do
    c,d=gets.chomp.split(" ").map(&:to_i)
    cds.push([c,d])
end
cds=cds.sort_by {|c,d| c}
ret=0
cds.each do |c,d|
    ab=nil
    abs.each do |a,b|
        next if c<a || d<b
        ab||=[a,b]
        ab = [a,b] if ab[1] < b
    end
    next if ab==nil
    abs.delete(ab)
    ret+=1
end
puts ret
