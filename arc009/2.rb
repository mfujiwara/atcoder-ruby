b_array=gets.chomp.split(" ")
MAP={}
b_array.each_with_index do |b,i|
    MAP[b]=i.to_s
end
VALUES=[]
N=gets.to_i
N.times do
    a=gets.chomp
    value=""
    (0..(a.length-1)).each do |i|
        value[i]=MAP[a[i]]
    end
    value=value.to_i
    VALUES.push([a,value])
end
VALUES.sort_by{|a,v| v }.each do |a,v|
    puts a
end
