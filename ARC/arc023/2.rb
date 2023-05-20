R,C,D=gets.chomp.split(" ").map(&:to_i)
ret=0
R.times do |r|
    array=gets.chomp.split(" ").map(&:to_i)
    array.each_with_index do |a,index|
        break if index + r > D
        if (r+index+D)%2==0
            ret=a if ret < a
        end
    end
end
puts ret
