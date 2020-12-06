N=gets.to_i
array=[]
N.times do
    array.push(gets.to_i)
end
r=0
streak=0
pre=false
first=nil
last=nil
N.times do |i|
    if array[i-2]==array[i-1] && array[i-1]==array[i]
        streak+=1
        r=streak if r<streak
        per=true
    else
        first ||= i
        last=i
        streak=0
        pre=false
    end
end
if streak==N
    puts "-1"
    exit
end
rr= N-last+first-1
r = rr if r<rr
puts (r+1)/2+1
