N=gets.to_i
start_days=[0,31,60,91,121,152,182,213,244,274,305,335]
days=Array.new(366,false)
N.times do
    m,d=gets.chomp.split("/").map(&:to_i)
    days[start_days[m-1]+d-1]=true
end
stock=0
count=0
count_max=0
days.each_with_index do |day, index|
    if day
        count+=1
        stock+=1 if index%7==0 || index%7==6
    else
        if index%7==0 || index%7==6
            count+=1
        elsif stock > 0
            stock-=1
            count+=1
        else
            count_max = count if count_max < count
            count = 0
        end
    end
end
count_max = count if count_max < count
puts count_max
