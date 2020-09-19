N=gets.to_i
array=gets.chomp.split(" ").map(&:to_i)
t_max=-2500
N.times do |i|
    a_max=-2500
    t_tmp=nil
    N.times do |j|
        next if i==j
        t_point=0
        a_point=0
        if i<j
            (i..j).each_with_index do |a,index|
                if index.even?
                    t_point+=array[a]
                else
                    a_point+=array[a]
                end
            end
        else
            (j..i).each_with_index do |a,index|
                if index.even?
                    t_point+=array[a]
                else
                    a_point+=array[a]
                end
            end
        end
        if a_max < a_point
            a_max=a_point
            t_tmp=t_point
        end
    end
    if t_max < t_tmp
        t_max=t_tmp
    end
end
puts t_max
