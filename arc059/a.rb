N = gets.to_i
array=gets.chomp.split(" ").map(&:to_i)
x2=0.0
x1=0.0
array.each do |a|
    x2 += 1.0
    x1 -= 2*a
end
x = (x1/x2/-2.0).round
puts array.inject(0) {|result,a| result + (x-a)**2 }
