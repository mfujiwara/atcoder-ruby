N=gets.to_i
array=gets.chomp.split(" ").map(&:to_i).sort
if array[0] >= 0
    sum=array.inject(&:+)
    puts sum-array[0]-array[0]
    tmp=array[0]
    (N-2).times do |i|
        puts "#{tmp} #{array[i+1]}"
        tmp-=array[i+1]
    end
    puts "#{array[N-1]} #{tmp}"
elsif array[N-1] < 0
    sum=array.inject(&:+)
    puts array[N-1]+array[N-1]-sum
    tmp=array[N-1]
    (N-1).times do |i|
        puts "#{tmp} #{array[i]}"
        tmp-=array[i]
    end
else
    positive_count=N
    sum=0
    array.each do |a|
        if a < 0
            sum-=a
            positive_count-=1
        else
            sum+=a
        end
    end
    puts sum
    tmp=array[0]
    (positive_count-1).times do |i|
        puts "#{tmp} #{array[N-1-i]}"
        tmp-=array[N-1-i]
    end
    puts "#{array[N-positive_count]} #{tmp}"
    tmp=array[N-positive_count]-tmp
    (N-positive_count-1).times do |i|
        puts "#{tmp} #{array[i+1]}"
        tmp-=array[i+1]
    end
end
