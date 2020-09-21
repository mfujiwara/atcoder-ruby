H,W=gets.chomp.split(" ").map(&:to_i)
A={}
H.times do
    array=gets.chomp.split("")
    array.each do |a|
        A[a]||=0
        A[a]+=1
        A[a]%=4
    end
end
values=A.map{|_,v|v}.sort
values.delete(0)
if H.odd? && W.odd?
    found=false
    values.each_with_index do |v,i|
        if v.odd?
            found=true
            values[i]-=1
            values.delete(0)
            break
        end
    end
    if !found
        puts "No"
        exit
    end
end
values.each do |v|
    if v.odd?
        puts "No"
        exit
    end
end
if H.odd?
    (W/2).times do
        values[0]-=2
        values.delete(0)
        if values.empty?
            puts "Yes"
            exit
        end
    end
end
if W.odd?
    (H/2).times do
        values[0]-=2
        values.delete(0)
        if values.empty?
            puts "Yes"
            exit
        end
    end
end
values.each do |v|
    if v%4==2
        puts "No"
        exit
    end
end
puts "Yes"
