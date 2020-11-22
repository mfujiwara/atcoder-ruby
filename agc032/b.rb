N=gets.to_i
point= N.even? ? N+1 : N
count=0
(1..(N-1)).each do |i|
    ((i+1)..N).each do |j|
        count+=1 unless i+j==point
    end
end
puts count
(1..(N-1)).each do |i|
    ((i+1)..N).each do |j|
        puts "#{i} #{j}" unless i+j==point
    end
end
